"""
Simple Shopping List App

A basic command-line shopping list application that demonstrates:
- Basic Python classes
- Simple data structures (lists and dictionaries)
- User input handling
- Basic error handling
"""

class ShoppingItem:
    """Represents an item in a shopping list."""
    
    def __init__(self, name):
        self.name = name
        self.purchased = False
    
    def mark_purchased(self):
        """Mark this item as purchased."""
        self.purchased = True
    
    def display(self):
        """Return a string representation of the item."""
        status = "✓ -" if self.purchased else "X -"
        return f"{status} {self.name}"


class ShoppingList:
    """Manages a collection of shopping items."""
    
    def __init__(self, name):
        self.name = name
        self.items = []  # List to store items
    
    def add_item(self, item_name):
        """Add a new item to the list."""
        # Check if item already exists
        for item in self.items:
            if item.name.lower() == item_name.lower():
                print(f"Item '{item_name}' already exists in the list!")
                return
        
        # Create and add new item
        new_item = ShoppingItem(item_name)
        self.items.append(new_item)
        print(f"Added '{item_name}' to '{self.name}'")
    
    def mark_item_purchased(self, item_name):
        """Mark an item as purchased."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                item.mark_purchased()
                print(f"Marked '{item_name}' as purchased!")
                return
        print(f"Item '{item_name}' not found in the list.")
    
    def display(self):
        """Display all items in the list."""
        print(f"\n--- {self.name} ---")
        if not self.items:
            print("(No items in this list)")
        else:
            for item in self.items:
                print(f"  {item.display()}")


class ShoppingApp:
    """Main application to manage multiple shopping lists."""
    
    def __init__(self):
        self.lists = {}  # Dictionary to store shopping lists
    
    def create_list(self, name):
        """Create a new shopping list."""
        if name in self.lists:
            print(f"A list named '{name}' already exists!")
            return
        
        self.lists[name] = ShoppingList(name)
        print(f"Created shopping list: '{name}'")
    
    def add_item(self, list_name, item_name):
        """Add an item to a specific list."""
        if list_name not in self.lists:
            print(f"List '{list_name}' not found!")
            return
        
        self.lists[list_name].add_item(item_name)
    
    def mark_purchased(self, list_name, item_name):
        """Mark an item as purchased in a specific list."""
        if list_name not in self.lists:
            print(f"List '{list_name}' not found!")
            return
        
        self.lists[list_name].mark_item_purchased(item_name)
    
    def show_all_lists(self):
        """Display all shopping lists."""
        if not self.lists:
            print("No shopping lists created yet.")
            return
        
        print("\n=== ALL SHOPPING LISTS ===")
        for list_name, shopping_list in self.lists.items():
            shopping_list.display()
    
    def run(self):
        """Run the interactive shopping list application."""
        print("Welcome to Simple Shopping List App!")
        print("=" * 40)
        
        while True:
            print("\nWhat would you like to do?")
            print("1. Create a new shopping list")
            print("2. Add item to a list")
            print("3. Mark item as purchased")
            print("4. Show all lists")
            print("5. Exit")
            
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == "1":
                name = input("Enter list name: ").strip()
                if name:
                    self.create_list(name)
                else:
                    print("List name cannot be empty!")
            
            elif choice == "2":
                if not self.lists:
                    print("No lists exist yet. Create a list first!")
                    continue
                
                list_name = input("Enter list name: ").strip()
                item_name = input("Enter item name: ").strip()
                if item_name:
                    self.add_item(list_name, item_name)
                else:
                    print("Item name cannot be empty!")
            
            elif choice == "3":
                if not self.lists:
                    print("No lists exist yet. Create a list first!")
                    continue
                
                list_name = input("Enter list name: ").strip()
                item_name = input("Enter item name: ").strip()
                if item_name:
                    self.mark_purchased(list_name, item_name)
                else:
                    print("Item name cannot be empty!")
            
            elif choice == "4":
                self.show_all_lists()
            
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Please enter a valid choice (1-5).")


def demo():
    """Show a quick demo of the shopping list app."""
    print("=== SHOPPING LIST APP DEMO ===\n")
    
    app = ShoppingApp()
    
    # Create some lists
    app.create_list("Groceries")
    app.create_list("Hardware")
    
    # Add some items
    app.add_item("Groceries", "Milk")
    app.add_item("Groceries", "Bread")
    app.add_item("Groceries", "Eggs")
    app.add_item("Hardware", "Hammer")
    app.add_item("Hardware", "Nails")
    
    # Mark some items as purchased
    app.mark_purchased("Groceries", "Milk")
    app.mark_purchased("Hardware", "Hammer")
    
    # Show all lists
    app.show_all_lists()
    
    print("\n" + "=" * 40)
    print("Demo completed! Now you can try it yourself.")


if __name__ == "__main__":
    # Run the demo first
    demo()
    
    # Then start the interactive app
    print("\nStarting interactive mode...")
    app = ShoppingApp()
    app.run()


