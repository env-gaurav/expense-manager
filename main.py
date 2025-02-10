expenses = {"Total":0}
count = 3
while count:
    expense=input("Enter Expenditure: ")
    amount=float(input("Enter amount of Expenditure: "))
    expenses['Total']+= amount
    count -= 1
    if expense == "Exit":
        break
    elif expense in expenses:
        expenses[expense]+= amount
    else:
        expenses[expense]= amount
print(expenses)
print("Total expenses", expenses.get("Total"))