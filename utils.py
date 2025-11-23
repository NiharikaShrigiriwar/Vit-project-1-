
def validate_number(input_str):
    """Check if input is a valid positive number"""
    try:
        number = float(input_str)
        if number <= 0:
            return False, "Number must be positive"
        return True, number
    except ValueError:
        return False, "Please enter a valid number"

def format_money(amount):
    """Format money nicely"""
    return f"₹{amount:.2f}"

def print_separator():
    """Print a nice separator line"""
    print("=" * 50)
