"""
Command-line Shopping List application

This module implements a small CLI utility to manage multiple shopping lists.

Core features:
    - Create shopping lists with unique names
    - Add items to lists (item names are unique within a list)
    - Mark items as purchased
    - Display all lists and their items with purchased status

Run this file directly to use the interactive CLI or to see a short demo.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class ShoppingItem:
    """Represents a single item in a shopping list."""

    name: str
    purchased: bool = False

    def mark_as_purchased(self) -> None:
        """Mark the item as purchased."""
        self.purchased = True

    def __str__(self) -> str:  # pragma: no cover - string formatting helper
        status = "(purchased)" if self.purchased else "(pending)"
        return f"- {self.name} {status}"


class ShoppingList:
    """Container for `ShoppingItem` instances under a named list."""

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("Shopping list name cannot be empty.")
        self.name: str = name.strip()
        # Map item name (lower-cased) to item for quick lookup and uniqueness
        self._items_by_key: Dict[str, ShoppingItem] = {}

    # ---------- Query helpers ----------
    def _normalize_key(self, item_name: str) -> str:
        # Normalize item names to a consistent key (trim + lowercase)
        return item_name.strip().lower()

    def has_item(self, item_name: str) -> bool:
        # Fast membership check without constructing exceptions
        return self._normalize_key(item_name) in self._items_by_key

    def get_item(self, item_name: str) -> ShoppingItem:
        key = self._normalize_key(item_name)
        if key not in self._items_by_key:
            raise KeyError(f"Item '{item_name}' does not exist in list '{self.name}'.")
        return self._items_by_key[key]

    def list_items(self) -> List[ShoppingItem]:
        # Return a snapshot list of items (caller can't mutate internal dict)
        return list(self._items_by_key.values())

    # ---------- Mutations ----------
    def add_item(self, item_name: str) -> ShoppingItem:
        # Validate input and enforce uniqueness inside a list
        if not item_name.strip():
            raise ValueError("Item name cannot be empty.")
        key = self._normalize_key(item_name)
        if key in self._items_by_key:
            raise ValueError(
                f"Item '{item_name}' already exists in list '{self.name}'."
            )
        item = ShoppingItem(name=item_name.strip())
        self._items_by_key[key] = item
        return item

    def mark_item_as_purchased(self, item_name: str) -> None:
        item = self.get_item(item_name)
        if item.purchased:
            # Idempotent behavior: if already purchased, nothing to change
            return
        item.mark_as_purchased()

    # ---------- Presentation ----------
    def __str__(self) -> str:  # pragma: no cover - string formatting helper
        header = f"Shopping List: {self.name}"
        if not self._items_by_key:
            return f"{header}\n  (no items)"
        # Build a multi-line, readable block listing all items
        lines = [header]
        for item in self.list_items():
            lines.append(f"  {str(item)}")
        return "\n".join(lines)


class ShoppingListApp:
    """High-level application service that manages multiple shopping lists."""

    def __init__(self) -> None:
        # Registry of lists keyed by normalized name; enforces uniqueness
        self._lists_by_key: Dict[str, ShoppingList] = {}

    # ---------- Internals ----------
    def _normalize_key(self, name: str) -> str:
        # Normalize list names to a consistent lookup key
        return name.strip().lower()

    def _require_list(self, list_name: str) -> ShoppingList:
        key = self._normalize_key(list_name)
        if key not in self._lists_by_key:
            raise KeyError(f"Shopping list '{list_name}' does not exist.")
        return self._lists_by_key[key]

    # ---------- API ----------
    def create_shopping_list(self, name: str) -> ShoppingList:
        # Create a new list after validating input and duplicates
        if not name.strip():
            raise ValueError("Shopping list name cannot be empty.")
        key = self._normalize_key(name)
        if key in self._lists_by_key:
            raise ValueError(f"A list named '{name}' already exists.")
        new_list = ShoppingList(name=name.strip())
        self._lists_by_key[key] = new_list
        return new_list

    def add_item_to_list(self, list_name: str, item_name: str) -> ShoppingItem:
        # Find target list and delegate item creation
        target_list = self._require_list(list_name)
        return target_list.add_item(item_name)

    def mark_item_as_purchased(self, list_name: str, item_name: str) -> None:
        # Find target list and mark specific item as purchased
        target_list = self._require_list(list_name)
        target_list.mark_item_as_purchased(item_name)

    def display_all_lists(self) -> str:
        """Return a string representation for all lists and items."""
        if not self._lists_by_key:
            return "No shopping lists created yet."
        # Join the string blocks of each list with a blank line between
        blocks = []
        for shopping_list in self._lists_by_key.values():
            blocks.append(str(shopping_list))
        return "\n\n".join(blocks)

    # ---------- CLI ----------
    def run_cli(self) -> None:  # pragma: no cover - interactive
        menu = (
            "\nChoose an action:\n"
            "  1) Create shopping list\n"
            "  2) Add item to a list\n"
            "  3) Mark item as purchased\n"
            "  4) Display all lists\n"
            "  5) Exit\n"
        )
        print("Shopping List App\n-------------------")
        while True:
            try:
                # Read user menu choice (strip spaces for safety)
                choice = input(menu + "> ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting...")
                return

            if choice == "1":
                name = _prompt_non_empty("Enter list name: ")
                try:
                    self.create_shopping_list(name)
                    print(f"Created list '{name}'.")
                except ValueError as exc:
                    print(f"Error: {exc}")

            elif choice == "2":
                list_name = _prompt_non_empty("Enter target list name: ")
                item_name = _prompt_non_empty("Enter item name: ")
                try:
                    self.add_item_to_list(list_name, item_name)
                    print(f"Added '{item_name}' to list '{list_name}'.")
                except (KeyError, ValueError) as exc:
                    print(f"Error: {exc}")

            elif choice == "3":
                list_name = _prompt_non_empty("Enter target list name: ")
                item_name = _prompt_non_empty("Enter item name to mark purchased: ")
                try:
                    self.mark_item_as_purchased(list_name, item_name)
                    print(f"Marked '{item_name}' as purchased in list '{list_name}'.")
                except KeyError as exc:
                    print(f"Error: {exc}")

            elif choice == "4":
                # Render current state of all lists
                print("\n" + self.display_all_lists() + "\n")

            elif choice == "5":
                print("Goodbye!")
                return

            else:
                print("Please choose a valid option (1-5).")


def _prompt_non_empty(prompt_text: str) -> str:  # pragma: no cover - interactive
    """Input helper that ensures the user cannot submit an empty string."""
    while True:
        try:
            value = input(prompt_text)
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            raise SystemExit(0)
        if value.strip():
            return value.strip()
        print("Input cannot be empty. Try again.")


def _demo() -> None:  # pragma: no cover - side-effectful demo
    """Showcase the core functionality with informative prints."""
    app = ShoppingListApp()
    print("\n--- Demo: creating lists, adding items, marking purchased ---")
    groceries = app.create_shopping_list("Groceries")
    hardware = app.create_shopping_list("Hardware")

    app.add_item_to_list(groceries.name, "Milk")
    app.add_item_to_list(groceries.name, "Eggs")
    app.add_item_to_list(hardware.name, "Nails")
    app.add_item_to_list(hardware.name, "Hammer")

    app.mark_item_as_purchased("Groceries", "Milk")

    print(app.display_all_lists())


if __name__ == "__main__":  # pragma: no cover - manual run only
    # First, demonstrate functionality as requested
    _demo()

    # Then, allow the user to continue interactively
    print("\nYou can now use the interactive menu. Press Ctrl+C to exit at any time.")
    ShoppingListApp().run_cli()


