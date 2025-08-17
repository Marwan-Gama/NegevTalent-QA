## Python OOP: Concepts + Examples

Pair this with the runnable `oop_python_examples.py`.

### Core ideas

- **Class**: blueprint for objects
- **Object**: instance of a class
- **Encapsulation**: hide internal data/behavior
- **Inheritance**: reuse/extending behavior
- **Polymorphism**: same interface, different behavior
- **Composition**: build complex objects from simpler ones

### Defining classes

What: a class bundles state (attributes) and behavior (methods).

```python
class User:
    def __init__(self, user_id: int, name: str) -> None:
        self.user_id = user_id
        self.name = name

    def greet(self) -> str:
        return f"Hello, I'm {self.name}"
```

### Encapsulation and properties

What: hide internal data, expose controlled access.

```python
class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self._owner = owner          # convention: protected/private
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("amount must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
```

### Inheritance

When: use to specialize behavior of a more general base.

```python
class Animal:
    def speak(self) -> str:
        return "..."

class Dog(Animal):
    def speak(self) -> str:
        return "Woof"

class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

def make_it_speak(animal: Animal) -> str:
    return animal.speak()
```

### Composition

When: prefer composition to assemble behavior from parts.

```python
class Engine:
    def start(self) -> str:
        return "engine-started"

class Car:
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def drive(self) -> str:
        return self.engine.start() + ": driving"
```

### Dunder methods and dataclasses

Why: customize built-in behavior (`+`, `str`, equality) with minimal code.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)
```

### Abstract base classes (interfaces)

Why: declare required methods without providing an implementation.

```python
from abc import ABC, abstractmethod

class Repository(ABC):
    @abstractmethod
    def get(self, key: str) -> str: ...

class MemoryRepository(Repository):
    def __init__(self) -> None:
        self._data: dict[str, str] = {}

    def get(self, key: str) -> str:
        return self._data.get(key, "")
```

### Errors, invariants, and validation

Keep class invariants true after every method call.

- Validate inputs in constructors and methods
- Keep class invariants true after every operation

### Testing OOP code

Small, focused tests help you evolve designs safely.

```python
def test_dog_speaks():
    assert Dog().speak() == "Woof"
```

### Next steps

Try this:

- Add a new animal (e.g., `Bird`) and implement `speak()`.
- Extend `MemoryRepository` with a `set(key, value)` method and test it.

- Run `oop_python_examples.py`
- Apply concepts to your own project
