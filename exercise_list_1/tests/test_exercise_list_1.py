import pytest
from exercise_list_1 import q1, q2

def helper_assert_in_out(function, in_text, out_text, monkeypatch, capsys):
    # Simulate user input
    monkeypatch.setattr("builtins.input", lambda _: f"{in_text}")

    # Call function that prints something
    function()

    # Check if output is correct
    captured = capsys.readouterr()
    assert captured.out == f"{out_text}\n"

def test_q1( monkeypatch, capsys):
    in_text = "test_string"
    out_text = "test_string"
    helper_assert_in_out(q1.main, in_text, out_text, monkeypatch, capsys)


