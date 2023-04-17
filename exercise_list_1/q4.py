def print_if_starts_with_a() -> None:
    s: str = input("Write a string!")
    if s[0] in ["a", "A"]:
        print(s)
