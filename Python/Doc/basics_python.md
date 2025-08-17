## Python Basics: Study Notes + Snippets

Use this as a quick guide to learn core Python. Code snippets are self‑contained and runnable. Pair with `basics_python_examples.py` for a hands‑on walkthrough.

### At a glance

- Variables and types
- Strings and collections
- Control flow
- Functions (`*args`, `**kwargs`)
- Modules, files, and exceptions
- Virtual envs and quick testing

### Getting set up (Windows)

- Install Python 3.11+ from the Microsoft Store or python.org
- Create and activate a virtual environment:

```powershell
py -3 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

### Running Python

- REPL: `python`
- File: `python script.py`

### Variables and basic types

Why: everything you do will store and pass around values of these types.

```python
name = "Ami"
age = 20                    # int
height_m = 1.75             # float
is_student = True           # bool

print(type(name), type(age), type(height_m), type(is_student))
```

### Strings

Why: string processing is everywhere (input, output, formatting).

```python
greeting = f"Hello, {name}!"
multi = """Multi-line\nstring"""
print(greeting.lower(), greeting.upper())
print("ami" in greeting.lower())
```

### Lists, tuples, sets, dicts

Why: these are your daily workhorses for grouping data.

```python
fruits = ["apple", "banana", "cherry"]   # list (mutable, ordered)
point = (10, 20)                           # tuple (immutable)
unique_nums = {1, 2, 2, 3}                 # set (unique)
person = {"name": "Ami", "age": 20}      # dict (key-value)

fruits.append("date")
person["city"] = "Beer Sheva"
```

### Control flow

Why: make decisions and repeat work.

```python
score = 87
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

for idx, fruit in enumerate(fruits):
    print(idx, fruit)

for n in range(3):
    print("n:", n)

# List comprehensions
squares = [n * n for n in range(6) if n % 2 == 0]
```

### Functions

Why: package logic into reusable building blocks.

```python
def greet(user_name: str = "world") -> str:
    return f"Hello, {user_name}!"

def add(*numbers: int) -> int:
    return sum(numbers)

def make_user(**fields) -> dict:
    return {"role": "user", **fields}

print(greet("Ami"))
print(add(1, 2, 3))
print(make_user(id=1, name="Ami"))
```

### Modules and imports

Why: split code across files so it’s easier to maintain.

```python
# file: math_utils.py
def mean(values: list[float]) -> float:
    return sum(values) / len(values)

# another file
import math_utils as mu
print(mu.mean([1.0, 2.0, 3.0]))
```

### File I/O

Why: read and write data to disk.

```python
text_path = "example.txt"
with open(text_path, mode="w", encoding="utf-8") as f:
    f.write("First line\nSecond line\n")

with open(text_path, encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Exceptions

Why: handle errors without crashing your program.

```python
def safe_div(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError as exc:
        print("Cannot divide by zero:", exc)
        return float("inf")
    finally:
        pass  # optional cleanup
```

### Virtual environments and dependencies

Why: keep each project’s packages isolated and reproducible.

```powershell
# create venv
py -3 -m venv .venv
.venv\Scripts\Activate.ps1

# install packages
pip install requests pytest

# freeze
pip freeze > requirements.txt
```

### Testing quick start (pytest)

Why: verify your code automatically.

```python
# file: test_math.py
from math import sqrt

def test_sqrt():
    assert sqrt(9) == 3
```

Run with: `pytest -q`

### Common pitfalls

- Floating point precision: use `decimal` for financial calculations
- Mutable default args: use `None` and create inside function

```python
def append_item(value: int, items: list[int] | None = None) -> list[int]:
    if items is None:
        items = []
    items.append(value)
    return items
```

### Next steps

Try this:

- Open `basics_python_examples.py` and change values (e.g., add more numbers to `add(...)`).
- Add a new key to the `person` dict, re-run and observe the output.

- Practice with `basics_python_examples.py`
- Learn OOP in `oop_python.md` next
