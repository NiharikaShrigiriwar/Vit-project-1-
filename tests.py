# tests.py - THE QUALITY CHECKER
from expense_manager import ExpenseManager
from calculator import DebtCalculator

def test_expense_manager():
    """Test if expense manager works correctly"""
    print(" TESTING EXPENSE MANAGER...")
    
    manager = ExpenseManager()
    
    # Test adding expenses
    manager.add_expense("Alice", 1000, "Rent")
    manager.add_expense("Bob", 500, "Food")
    
    expenses = manager.get_all_expenses()
    
    # Check if we have 2 expenses
    if len(expenses) == 2:
        print(" PASS: Can add and retrieve expenses")
    else:
        print(" FAIL: Wrong number of expenses")
        return False
    
    # Check total calculation
    total = manager.get_total_spent()
    if total == 1500:
        print(" PASS: Total calculation works")
    else:
        print(" FAIL: Wrong total calculation")
        return False
    
    return True

def test_debt_calculator():
    """Test if debt calculator works correctly"""
    print(" TESTING DEBT CALCULATOR...")
    
    calculator = DebtCalculator()
    
    # Test data - Alice paid more, Bob paid less
    test_expenses = [
        {"paid_by": "Alice", "amount": 1200, "for": "Internet"},
        {"paid_by": "Bob", "amount": 800, "for": "Food"}
    ]
    
    settlements = calculator.calculate_settlements(test_expenses)
    
    # Should have at least one settlement
    if len(settlements) > 0:
        print("PASS: Can calculate settlements")
    else:
        print(" FAIL: No settlements calculated")
        return False
    
    # Check if Bob owes Alice money (he should!)
    bob_owes_alice = False
    for settlement in settlements:
        if settlement["from"] == "Bob" and settlement["to"] == "Alice":
            bob_owes_alice = True
            break
    
    if bob_owes_alice:
        print("PASS: Correct debt relationship found")
    else:
        print(" FAIL: Wrong debt relationship")
        return False
    
    return True

def run_all_tests():
    """Run all tests"""
    print(" RUNNING ALL TESTS...")
    print()
    
    success1 = test_expense_manager()
    print()
    success2 = test_debt_calculator()
    print()
    
    if success1 and success2:
        print(" ALL TESTS PASSED! YOUR CODE IS AWESOME! ")
        return True
    else:
        print(" SOME TESTS FAILED! CHECK YOUR CODE!")
        return False

if __name__ == "__main__":
    run_all_tests()
