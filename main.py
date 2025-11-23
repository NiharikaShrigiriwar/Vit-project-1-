from expense_manager import ExpenseManager
from calculator import DebtCalculator
from ui import UserInterFcae
def main():
  print("==COLLEGE EXPENSE SPLITTER==")
  PRINT("NO MORE MONEY CONFLICTS !  :) ")
  expense_tracker=ExpenseManager()
  math_genius=DebtCalculator
  talker=UserInterFace(expense_tracker,math_genius)
  talker.run()

if _name_=="_main_":
  main()
  
