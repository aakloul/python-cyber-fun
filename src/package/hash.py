import base64
import hashlib


def b64e(arg: str) -> bytes:
    return base64.b64encode(arg.encode())


def b64d(arg: bytes) -> str:
    return base64.b64decode(arg).decode()


def sha256(arg: str) -> str:
    return hashlib.sha256(arg.encode()).hexdigest()


def md5(arg: str) -> str:
    return hashlib.md5(arg.encode()).hexdigest()


if __name__ == "__main__":
    statement = "This is a secret"
    encoded = md5(statement)
    print(encoded)
    # decoded = b64d(encoded)
    # print(decoded)
