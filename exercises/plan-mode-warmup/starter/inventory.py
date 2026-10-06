"""Simple inventory management module for interaction and testing exercises."""


def add_item(inventory, name, quantity, price):
    """Add an item to inventory. Overwrites if item already exists."""
    inventory[name] = {"quantity": quantity, "price": price}


def remove_item(inventory, name):
    """Remove an item from inventory, doing nothing if the item is missing."""
    inventory.pop(name, None)


def get_total_value(inventory):
    """Calculate total value of all items in inventory."""
    total = 0
    for item in inventory:
        total += inventory[item]["quantity"] * inventory[item]["price"]
    return total


def apply_discount(inventory, name, percent):
    """Apply a percentage discount to an item's price.

    Args:
        inventory: Mapping of item names to quantity and price records.
        name: Name of the existing item to discount.
        percent: Percentage to subtract; for example, 25 means a 25% discount.

    Raises:
        KeyError: If the item is missing from inventory.
    """
    item = inventory[name]
    item["price"] = item["price"] - (item["price"] * percent / 100)


def find_low_stock(inventory, threshold):
    """Find items with quantity below threshold."""
    results = []
    for name in inventory:
        if inventory[name]["quantity"] < threshold:
            results.append(name)
    return results


def restock(inventory, name, amount):
    """Add stock to an existing item."""
    inventory[name]["quantity"] = inventory[name]["quantity"] + amount


def generate_report(inventory):
    """Generate a simple text report of inventory."""
    lines = []
    lines.append("=== Inventory Report ===")
    lines.append(f"{'Item':<20} {'Qty':>5} {'Price':>8} {'Value':>10}")
    lines.append("-" * 45)
    for name in sorted(inventory.keys()):
        item = inventory[name]
        value = item["quantity"] * item["price"]
        lines.append(f"{name:<20} {item['quantity']:>5} {item['price']:>8.2f} {value:>10.2f}")
    lines.append("-" * 45)
    lines.append(f"{'Total':<20} {'':>5} {'':>8} {get_total_value(inventory):>10.2f}")
    return "\n".join(lines)
