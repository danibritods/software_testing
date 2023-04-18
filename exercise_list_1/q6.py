from typing import Dict, Union, Tuple, List


def read_names_return_youngest_n_oldest() -> str:
    youngest: Dict[str, Union[str, int]] = {"name": "", "age": 0}
    oldest: Dict[str, Union[str, int]] = {"name": "", "age": 0}
    while True:
        input_name: str = input("Enter a name: ")
        if input_name == "-1":
            break
        input_age: int = int(input(f"Enter {input_name}'s age: "))

        if input_age < 0:
            break
        if input_age > oldest["age"]:
            oldest["age"] = input_age
            oldest["name"] = input_name
        if input_age < youngest["age"] or youngest["age"] == 0:
            youngest["age"] = input_age
            youngest["name"] = input_name
    result_string: str = f"youngest: {youngest['name']}:{youngest['age']}, oldest: {oldest['name']}:{oldest['age']}."
    print(result_string)


def read_names_return_youngest_n_oldest_tuples() -> None:
    name_age: List[Tuple[str, int]] = []
    while True:
        input_name: str = input("Enter a name: ")
        if input_name == "-1":
            break
        input_age: int = int(input(f"Enter {input_name}'s age: "))
        if input_age < 0:
            break
        name_age.append((input_name, input_age))
    oldest = max(name_age, key=lambda t: t[1])
    youngest = min(name_age, key=lambda t: t[1])
    result_string: str = (
        f"youngest: {youngest[0]}:{youngest[1]}, oldest: {oldest[0]}:{oldest[1]}."
    )
    print(result_string)
