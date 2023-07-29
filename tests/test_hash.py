import pytest

from package.hash import b64d, b64e, sha256, md5


@pytest.mark.parametrize(
    "given, expected",
    [
        (b"VGhpcyBpcyBhIHNlY3JldA==", "This is a secret"),
    ],
)
def test_b64d(given, expected):
    assert b64d(given) == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        ("This is a secret", b"VGhpcyBpcyBhIHNlY3JldA=="),
    ],
)
def test_b64e(given, expected):
    assert b64e(given) == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        (
            "This is a secret",
            "f2d9ad12c972f3f76c37268514de20f74d70603cd369f55f70b52472c1de1065",
        ),
    ],
)
def test_sha256(given, expected):
    assert sha256(given) == expected


@pytest.mark.parametrize(
    "given, expected",
    [
        (
            "This is a secret",
            "f8158b240153f4dec10ff3852e7e9c17",
        ),
    ],
)
def test_md5(given, expected):
    assert md5(given) == expected
