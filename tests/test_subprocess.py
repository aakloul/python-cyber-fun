from package.subprocess import (
    ls_check_output,
    ls_subprocess,
)


def test_ls_check_output():
    output = ls_check_output()
    assert b"README.md" in output


def test_ls_subprocess(capsys):
    ls_subprocess()
    stdout = capsys.readouterr().out
    assert "Finished!\n" in stdout
