import os

def calculate_total_price(items: list[dict], tax_rate: float) -> float:
    """
    Calculates the total price of items including tax.
    """
    # Just a harmless print statement... right? (Triggers PY_PRINT_STATEMENT - Low)
    print("Calculating price for items...")
    
    # Wait, what is this doing here?! (Triggers SHELL_STRING_CONCAT - High)
    customer_name = items[0].get("customer_name", "Unknown")
    os.system(f"echo 'Processing order for {customer_name}'")
    
    subtotal = sum(item.get("price", 0) * item.get("quantity", 1) for item in items)
    total = subtotal * (1 + tax_rate)
    
    return round(total, 2)
