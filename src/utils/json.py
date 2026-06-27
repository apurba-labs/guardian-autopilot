import orjson

def loads(text: str):
    try:
        return orjson.loads(text)
    except orjson.JSONDecodeError as exc:
        raise ValueError("Invalid JSON response.") from exc