DOWN_PAY = 0.10

purchase_price = float(input("Enter the purchase price: "))
annual_rate = float(input("Enter the annual interest rate: "))
annual_rate = annual_rate / 100

monthly_rate = annual_rate / 12
monthly_pay = purchase_price * 0.05
month = 1
balance = purchase_price - (purchase_price * DOWN_PAY)

print("Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance")

while balance > 0:
    if monthly_pay > balance:
        monthly_pay = balance
        interest_owed = 0
    else:
        interest_owed = balance * monthly_rate
    principal_owed = monthly_pay - interest_owed
    remaining = balance - monthly_pay
    print("%3d" % month, "%15.2f" % balance, "%15.2f" % interest_owed, "%16.2f" % principal_owed, "%13.2f" % monthly_pay, "%16.2f" % abs(remaining))
    month += 1
    balance = remaining