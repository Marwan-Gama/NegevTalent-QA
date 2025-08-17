"""
Runnable OOP examples.

How to use:
1) Each section prints a title first
2) Read the short output and tweak code to experiment

Run: python Python/Doc/oop_python_examples.py
"""

from __future__ import annotations
from dataclasses import dataclass
from abc import ABC, abstractmethod


class User:
    """Simple class with state (id, name) and a behavior (greet)."""
    def __init__(self, user_id: int, name: str) -> None:
        if user_id <= 0:
            raise ValueError("user_id must be positive")
        self.user_id = user_id
        self.name = name

    def greet(self) -> str:
        return f"Hello, I'm {self.name}"


class BankAccount:
    """Encapsulates balance with validation and a read-only property."""
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("balance cannot be negative")
        self._owner = owner
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


class Animal:
    """Base class to demonstrate inheritance/polymorphism."""
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


class Engine:
    """A small component that a Car can use (composition)."""
    def start(self) -> str:
        return "engine-started"


class Car:
    """Composed of an Engine; calls into it to perform work."""
    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def drive(self) -> str:
        return self.engine.start() + ": driving"


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def __add__(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)


class Repository(ABC):
    """An interface-like abstract base class for data access."""
    @abstractmethod
    def get(self, key: str) -> str:  # interface method
        raise NotImplementedError


class MemoryRepository(Repository):
    def __init__(self) -> None:
        self._data: dict[str, str] = {"hello": "world"}

    def get(self, key: str) -> str:
        return self._data.get(key, "")


def main() -> None:
    print("\n=== CLASSES & METHODS ===")
    user = User(1, "Ami")
    print(user.greet())

    print("\n=== ENCAPSULATION & PROPERTIES ===")
    acct = BankAccount("Ami", 100)
    acct.deposit(50)
    acct.withdraw(20)
    print("balance:", acct.balance)

    print("\n=== INHERITANCE & POLYMORPHISM ===")
    print(make_it_speak(Dog()), make_it_speak(Cat()))

    print("\n=== COMPOSITION ===")
    car = Car(Engine())
    print(car.drive())

    print("\n=== DUNDER METHODS & DATACLASS ===")
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    print("Point + Point:", p1 + p2)

    print("\n=== ABSTRACT BASE CLASS (INTERFACE) ===")
    repo: Repository = MemoryRepository()
    print("lookup:", repo.get("hello"))


if __name__ == "__main__":
    main()


