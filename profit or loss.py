actual_cost=float(input("enter actual cost or else... : "))
sale_amount=float(input("enter sale amount or else... : "))

if sale_amount>actual_cost:
    profit= sale_amount - actual_cost
    print("your profit is: ",format (profit))
else:
    print("no profit")
