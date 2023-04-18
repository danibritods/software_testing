import pytest
from exercise_list_1 import q1, q2, q3, q4, q5, q6


def enter_input(input_text, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: f"{input_text}")


def enter_input_sequence(input_list, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: input_list.pop(0))


def test_enter_input_sequence(monkeypatch):
    enter_input_sequence([1, 2, 3], monkeypatch)
    a = input("a")
    b = input("b")
    c = input("c")
    assert [a, b, c] == [1, 2, 3]


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
    expected_text = f"{expected_size}\n"

    q2.string_length(test_string)
    captured = capture_print(capsys)
    assert captured == expected_text, "Should be 5."


def test_q3():
    test_string = "0011001"
    expected_count_1 = 3
    received = q3.count_ones(test_string)
    assert received == expected_count_1, "Should be 3."


@pytest.mark.parametrize(
    "test_string, expected_text", [("foo", ""), ("abar", "abar\n")]
)
def test_q4(monkeypatch, capsys, test_string, expected_text):
    enter_input(test_string, monkeypatch)
    q4.print_if_starts_with_a()
    captured = capture_print(capsys)
    assert captured == expected_text


@pytest.mark.parametrize(
    "test_string, expected_text", [(" t e s t ", "test"), ("test", "test")]
)
def test_q5(test_string, expected_text):
    received = q5.remove_spaces(test_string)
    assert received == expected_text, f"Should be {expected_text}"

@pytest.mark.parametrize(
    "input_sequence, expected_text",
    [
        (
            ["Daniel", "25", "João", "21", "José", "20", "-1"],
            "youngest: José:20, oldest: Daniel:25.\n",
        ),
        (
            ["Pedro", "20", "-1"],
            "youngest: Pedro:20, oldest: Pedro:20.\n",
        ),
    ],
)
def test_read_names_return_youngest_and_oldest(
    monkeypatch,
    capsys,
    input_sequence,
    expected_text,
):
    enter_input_sequence(input_sequence, monkeypatch)
    q6.read_names_return_youngest_n_oldest()
    captured = capture_print(capsys)
    assert captured == expected_text
