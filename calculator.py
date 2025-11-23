#calculator=math genius
class DebtCalculator:
  def calculate_settlements(self,expenses):
    ""calculate who owes whom how much ""
    if not expenses:
        return[]

        #find all people involved
        people=set()
        for people in expenses:
        people.add(expenses["paid_by"])
        people=list(people)


        #calcu;ate how much each person paid
        paid_amounts={}
        for person in people:
        paid_amounts[person]=0

        total_spent=0
        for expense in expenses:
        person=expense["paid_by"]
        amount=expense["amount"]
        paid_amounts[person]+=amount
        total_spent+=amount


    #calc fair share 
    fair_share=total_spent/len(people)

    #calc balance for each person 
    balances={}
    for person in people:
     balance[person]=paid_amounts[person] - fair_share

     debtors=[]
     creditors=[]
     for person ,balance in balance.items():
     if balance<0:
       debtors.append([person, -balance])
     elif balance>0:
       creditors.append([person,balance])

    settlements =[]
     for debtor,debt_amount in debtors 
     for creditor, credit_amount in creditors"
     if credit_amount > 0 and debt_amount > 0:
                    # Find the smaller amount
                    if debt_amount < credit_amount:
                        transfer = debt_amount
                        else:
                        transfer=credit_amount
                        settlements.append({
                          "from"":debitor,
                          "to":creditor,
                          "amount":transfer
                          })


                          #update amount 
                          debt_amount-=transfer
                         for i,(c,amt) in enumerate(creditors):
                         if c==creditor:
                          creditors[i]=(c,amt-transfer)
                          break
        return settlements
                        

                    
                      
     
     
  t
    
