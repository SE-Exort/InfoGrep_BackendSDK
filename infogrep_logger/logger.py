import logging
from typing import Dict, Any
from datetime import datetime, timezone

from pythonjsonlogger import jsonlogger
from pydantic import BaseModel
from elasticsearch import Elasticsearch
from elastic_transport import (
    ConnectionError as EsConnectionError, 
)

from ..service_endpoints import es_port, es_host, es_password, es_username

class ElasticSearchConfig(BaseModel):
    port: int
    username: str
    password: str
    host: str

class LogstoreHandler(logging.StreamHandler):
    def __init__(self, es_config: ElasticSearchConfig):
        super().__init__()

        es_url = f'http://{es_config.username}:{es_config.password}@{es_config.host}:{es_config.port}'
        self.es_client = Elasticsearch(es_url)
        if not self.es_client.ping():
            raise EsConnectionError("Cannot reach Elasticsearch")

    def emit(self, record):
        msg = self.format(record)
        self.es_client.index(index="logs", document=msg)

class CustomJsonFormatter(jsonlogger.JsonFormatter):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def add_fields(self, log_record: Dict[str, Any], record: logging.LogRecord, message_dict: Dict[str, Any]):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

        log_record["timestamp"] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        log_record["level"] = record.levelname.upper()
        log_record["level_num"] = record.levelno
        log_record["logger_name"] = record.name
        log_record["file_name"] = record.pathname
        log_record["func_name"] = record.funcName
        log_record["line_num"] = record.lineno
        log_record["msecs"] = record.msecs

        self.set_extra_keys(record, log_record, self._skip_fields)
    
    @staticmethod
    def set_extra_keys(record, log_record, reserved):
        """
        Add the extra data to the log record as extra dict
        """
        new_record_dict = {}
        record_items = list(record.__dict__.items())
        records_filtered_reserved = [item for item in record_items if item[0] not in reserved]

        for key, value in records_filtered_reserved:
            log_record.pop(key, None)
            new_record_dict[key] = value
        
        log_record["extra"] = new_record_dict
    
class Logger(logging.Logger):
    """
    Usage:

    mylogger = Logger("my_logger_name") #param for debug defaults to false
    mylogger.info("What is going on")
    mylogger.error("error message", extra={
        "error_code": 500,
        "whatever": "something" 
    })

    Log Format:
    {
        "message": "What is going on",
        "timestamp": "2024-07-09T19:08:27.667206Z",
        "level": "INFO",
        "level_num": 20,
        "logger_name": "testlogger",
        "file_name": "/Users/tyronehe/code/infogrep/InfoGrep-CoreUtility/test.py",
        "func_name": "test_logger",
        "line_num": 5,
        "msecs": 666.0,
        "extra": {
            "extra_key1": "v1",
            "extra_key2": "v2"
        }
    }
    """
    def __init__(
            self, name: str, 
            debug: bool = False, 
            level: int | str = 0) -> None:
        super().__init__(name, level)

        stream_handler = logging.StreamHandler()
        formatter = CustomJsonFormatter(json_indent=4, json_ensure_ascii=True, timestamp=True)
        stream_handler.setFormatter(formatter)

        if debug: 
            super().addHandler(stream_handler)
            return 

        try:
            es_config = ElasticSearchConfig(
                port=es_port,
                host=es_host,
                username=es_username,
                password=es_password
            )
            es_handler = LogstoreHandler(es_config)
            es_handler.setFormatter(formatter)
            super().addHandler(es_handler)
        except EsConnectionError as e:
            super().log(level=40, msg=f"{'*'*10}\n ERROR: Connection to Elasticsearch cannot be established for the logger, defaulting to stream handler. \n{'*'*10}\n")
            super().addHandler(stream_handler)