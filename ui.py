class UserInterface:
  def _init_(self,expense_manager,debt_calculator):
    self.manager=expense_manager
    self.calculator=deft_calculator
 def run(self):
   """Main program loop"""
   while True:
     self.show_menu()
     choice=input("enter choice from 1-4").strip()
     if choice=="1":
       self.add_expense_ui()
     elif  choice=="2":
       self.view_expense_ui()
     elif  choice=="3":
      self.calculate_debts_ui()
     elif  choice=="4":
       print("thanks for using expense splitter")
       break
else:
print("invalid choice")
 def show_menu(self):
   ""show the menu ""
   print("\n" + "="*40)
    print("WHAT DO YOU WANT TO DO?")
        print("1.  ADD NEW EXPENSE")
        print("2.  VIEW ALL EXPENSES") 
        print("3.  CALCULATE WHO OWES WHOM")
        print("4. EXIT")
        print("="*40)
     def add_expense_ui(self):
     "'get expense details from user""
     print("ADD NEW EXPENSE !")
     paid_by=input("who paid").strip()
     #get amount with error checking 
     while True:
       amount_str=input("how much ?"
       )
       try:
       amount=float(amount_str)
       if amount<=0:
         print(" Amount must be positive! Try again.")
                    continue
                break
            except ValueError:
                print(" Please enter a valid number! Try again.")
            description =input("reason").strip()
            #add th expense
            
            if self.manager.add_expense(paid_by,amount,description):
             print("{paid_by} paid {amount} for {description}")
       def view_expenses_ui(self):
         """Show all expenses"""
        print("\n--- ALL EXPENSES ---")
        expenses = self.manager.get_all_expenses()
        
        if not expenses:
            print("No expenses recorded yet. Add some first!")
            return
            total=0
            print("your expense history")
            for i in enumerate (expenses,1):
             print({i}.{expenses['paid_by']} paid {expense['amount']} for]}")
             total+=expense['amount']
             print("TOTAL SPENT: {total}")
             def calculate_debts_uni(self):
             """Calculate and show who owes whom"""
             print("settelement calc")
             expenses=self.manager.get_all_expenses()
             if not expenses:
             print("no expense to calculate")
             return 
             settlements=self.calculator.calculate_settlements(expenses)
             if not settlements:
             print(" everyone is settled!")
             return 
             print("who owes whom")
             print("time to settle")
             for settlements in settlements:
             print({settlement['from']} should pay {settlement['to']}:{settlement['amount']}")
             
             
        
    

