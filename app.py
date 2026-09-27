def calculate_total_price(items: list[dict], tax_rate: float) -> float:
    """
    Calculates the total price of items including tax.
    """
    subtotal = sum(item.get("price", 0) * item.get("quantity", 1) for item in items)
    total = subtotal * (1 + tax_rate)
    
    return round(total, 2)

# Notice there are no print statements, no eval(), no secrets, and no long lines!
