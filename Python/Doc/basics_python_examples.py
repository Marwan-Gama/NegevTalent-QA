"""
Hands-on examples for Python basics.

How to use:
1) Read a section title printed to the console
2) Skim the short code and output
3) Tweak values and re-run to learn by doing

Run: python Python/Doc/basics_python_examples.py
"""

from __future__ import annotations

def demo_types() -> None:
    """Show core built-in types and how to inspect them."""
    print("\n=== TYPES ===")
    name: str = "Ami"        # string
    age: int = 20            # integer
    height_m: float = 1.75   # floating-point number
    is_student: bool = True  # boolean
    print(type(name), type(age), type(height_m), type(is_student))


def demo_collections() -> None:
    """Lists, tuples, sets, dicts at a glance."""
    print("\n=== COLLECTIONS ===")
    fruits: list[str] = ["apple", "banana", "cherry"]  # ordered, mutable
    fruits.append("date")
    point: tuple[int, int] = (10, 20)                     # fixed-size pair
    uniq: set[int] = {1, 2, 2, 3}                         # unique values -> {1,2,3}
    person: dict[str, object] = {"name": "Ami", "age": 20}  # key/value map
    person["city"] = "Beer Sheva"
    print("fruits:", fruits)
    print("point:", point)
    print("set:", uniq)
    print("dict:", person)


def demo_flow() -> None:
    """If/elif/else, loops, and a list comprehension."""
    print("\n=== CONTROL FLOW ===")
    score: int = 87
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
    print("grade:", grade)

    for idx, fruit in enumerate(["apple", "banana", "cherry"]):
        print("fruit", idx, fruit)

    squares = [n * n for n in range(6) if n % 2 == 0]
    print("even squares:", squares)


def greet(user_name: str = "world") -> str:
    """Return a friendly greeting; default to 'world'."""
    return f"Hello, {user_name}!"


def add(*numbers: int) -> int:
    """Sum any number of integers using *args."""
    return sum(numbers)


def make_user(**fields) -> dict[str, object]:
    """Build a user dict with arbitrary keyword fields."""
    return {"role": "user", **fields}


def demo_functions() -> None:
    """Demonstrate defaults, *args, and **kwargs."""
    print("\n=== FUNCTIONS ===")
    print("greet:", greet("Ami"))
    print("add:", add(1, 2, 3))
    print("make_user:", make_user(id=1, name="Ami"))


def safe_div(a: float, b: float) -> float:
    """Divide a by b; on divide-by-zero return +inf instead of crashing."""
    try:
        return a / b
    except ZeroDivisionError:
        return float("inf")


def demo_exceptions() -> None:
    """Show try/except behavior with a safe division function."""
    print("\n=== EXCEPTIONS ===")
    print("10/2:", safe_div(10, 2))
    print("5/0:", safe_div(5, 0))


def append_item(value: int, items: list[int] | None = None) -> list[int]:
    """Correct pattern for mutable defaults (use None then create a new list)."""
    if items is None:
        items = []
    items.append(value)
    return items


def main() -> None:
    """Run all mini-demos in a readable order."""
    demo_types()
    demo_collections()
    demo_flow()
    demo_functions()
    demo_exceptions()
    print("\n=== MUTABLE DEFAULTS ===")
    print("append_item calls:", append_item(1), append_item(2))


if __name__ == "__main__":
    main()


