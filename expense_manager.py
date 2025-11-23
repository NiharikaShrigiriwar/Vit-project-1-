#expense_manager.py=memory bank 
class ExpenseManager:
  def _init_(self):
    self.expenses=[]
 def add_expense(self,paid_by,amount,description):
   ""remember a new expense""
   expense={
     "paid_by":paid_by,
     "amount": amount,
     "for":description
     }
     
       self.expense.append(expense)
       return True

  def get_total_spent(self):
  ""calculate total money spent""
  total=0
  for expense in self.expenses:
  total+=expenses["amount"]
  return total


  def get_all_people(self):
  ""find all people who spent money""
  people=set()
  for expense in self.expense
   people.add(expense["paid_by"])
   return list(people)
