import pytest
from exercise_list_1 import q1, q2


def enter_input(input_text, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: f"{input_text}")


def capture_print(capsys):
    captured_text = capsys.readouterr()
    return captured_text.out


def test_q1(monkeypatch, capsys):
    in_text = "test_string"
    out_text = "test_string\n"
    enter_input(in_text, monkeypatch)
    q1.main()
    captured = capture_print(capsys)
    assert out_text == captured


def test_q2(capsys):
    test_string = "12345"
    expected_size = 5

    q2.string_length(test_string)
    captured = capture_print(capsys)
    assert expected_size == captured
