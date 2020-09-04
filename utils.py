import mimetypes
import settings
from errors import NotFound
from custom_types import User

from urllib.parse import parse_qs


# def normalize_path(path: str) -> str:
#     if not path:
#         return "/"

#     normalized_path = path

#     if normalized_path[-1] != "/":
#         normalized_path = f"{normalized_path}/"

#     return normalized_path


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


def get_content_type(file_path: str) -> str:
    """
    Calculates content-type against given path. Default is "text/html"
    :param file_path: hypothetical path to file
    :return: content-type value
    """

    if not file_path:
        return "text/html"
    content_type, _ = mimetypes.guess_type(file_path)
    return content_type    



def get_user_data(qs: str) -> User:
    qp = parse_qs(qs)

    default_names = ["world"]
    default_ages = [0]

    name_values = qp.get("name", default_names)
    age_values = qp.get("age", default_ages)

    name = name_values[0]
    age = int(age_values[0])

    return User(name=name, age=age)    					    		