def header_cleanup(headers):
    if not isinstance(headers, dict):
        headers = dict(headers)
    
    headers.pop("content-type")
    headers.pop("content-length")

    return headers