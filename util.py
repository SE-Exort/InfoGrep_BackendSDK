def header_cleanup(headers):
    if not isinstance(headers, dict):
        headers = dict(headers)
    
    headers.pop("content-type", None)
    headers.pop("content-length", None)

    return headers