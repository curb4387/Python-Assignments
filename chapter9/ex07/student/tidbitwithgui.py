from breezypythongui import EasyFrame

class tidbit(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "TidBit Credit Plan", width = 400, height = 225)
        self.addLabel(text = "Purchase Price", row = 0, column = 0)
        self.purchasePrice = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)
        self.addLabel(text = "Annual Interest Rate", row = 1, column = 0)
        self.annualRate = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
        self.addButton(text = "Calculate", row = 2, column = 1, command = self.calculate)
        self.creditPlanTable = self.addTextArea("", row = 3, column = 0, columnspan = 2, height = 5)

    def calculate(self):
        DOWN_PAY = 0.10
        annualRate = self.annualRate.getNumber() / 100
        purchasePrice = self.purchasePrice.getNumber()

        monthly_rate = annualRate / 12
        monthly_pay = purchasePrice * 0.05
        month = 1
        balance = purchasePrice - (purchasePrice * DOWN_PAY)

        result = "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n"

        while balance > 0:
            if monthly_pay > balance:
                monthly_pay = balance
                interest_owed = 0
            else:
                interest_owed = balance * monthly_rate
            principal_owed = monthly_pay - interest_owed
            remaining = balance - monthly_pay
            result += "%3d%15.2f%16.2f%18.2f%14.2f%12.2f\n" % (month, balance, interest_owed, principal_owed, monthly_pay, abs(remaining))
            month += 1
            balance = remaining

        self.creditPlanTable["state"] = "normal"
        self.creditPlanTable.setText(result)
        self.creditPlanTable["state"] = "disabled"

def main():
    tidbit()

if __name__ == "__main__":
    main()

input("pythongui")