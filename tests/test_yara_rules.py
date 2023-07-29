import yara


def test_yara_1():
    rules = yara.compile(
        filepaths={
            "namespace1": "./sample/always_true.yara",
            "namespace2": "./sample/always_false.yara",
        }
    )
    matches = rules.match(data="./hello.txt")
    assert len(matches) == 1
    for m in matches:
        assert m.rule == "dummy_true"


def test_yara_2():
    rules = yara.compile(
        sources={
            "namespace1": "rule dummy_true { condition: true }",
            "namespace2": "rule dummy_false { condition: false }",
        }
    )
    matches = rules.match(data="./hello.txt")
    assert len(matches) == 1
    for m in matches:
        assert m.rule == "dummy_true"
