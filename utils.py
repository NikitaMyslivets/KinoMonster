import settings
from typing import AnyStr
from errors import NotFound


def to_bytes(text) -> bytes:
    if isinstance(text, bytes):
        return text

    if not isinstance(text, str):
        msg = f"cannot convert {type(text)} to bytes"
        raise ValueError(msg)

    result = text.encode()
    return result	


def read_static(path: str) -> bytes:
    static = settings.STATIC_DIR / path
    if not static.is_file():
        full_path = static.resolve().as_posix()
        msg = f"file <{full_path}> not found"
        raise NotFound(msg)

    with static.open("rb") as fp:
        result = fp.read()

    return result		


def to_str(text: AnyStr) -> str:
    """
    Safely converts any string to str.
    :param text: any string
    :return: str
    """

    result = text

    if not isinstance(text, (str, bytes)):
        result = str(text)

    if isinstance(result, bytes):
        result = result.decode()

    return result