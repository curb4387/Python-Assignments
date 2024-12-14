# This program creates a GUI for a tax calculator

### Field types
# addIntegerField
# addFloatField
# addTextField

### Add content
# addButton
# addLabel

from breezypythongui import EasyFrame

class taxCalculator(EasyFrame):
    # init = initialization - allows creation of object of the taxCalculator class
    # for this program, this will create the window for the Tax Calculator
    def __init__(self):
        EasyFrame.__init__(self, title = "Tax Calculator", width = 300, height = 200)
        # Coordinates 0,0 will always be the top-left of the window
        self.addLabel(text = "Gross income", row = 0, column = 0)
        self.addLabel(text = "Dependents", row = 1, column = 0)
        # Assign the input fields to a variable so they get stored somewhere
        # value indicates the default value that is shown when the window first starts up
        self.incomeField = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)
        self.depField = self.addIntegerField(value = 0, row = 1, column = 1)
        # Radio buttons
        self.addLabel(text = "Filing Status", row = 2, column = 0)
        self.fileStatus = self.addRadiobuttonGroup(row = 2, column = 1, rowspan = 3)
        self.singleFile = self.fileStatus.addRadiobutton(text = "Single")
        self.marriedFile = self.fileStatus.addRadiobutton(text = "Married")
        self.divorcedFile = self.fileStatus.addRadiobutton(text = "Divorced")
        self.fileStatus.setSelectedButton(self.singleFile)
        # Add a button: the command attribute is assigned to the calculate method that will handle the event when the button is clicked
        self.addButton(text = "Compute", row = 5, column = 1, command = self.calculate)
        self.addLabel(text = "Total tax", row = 6, column = 0)
        self.totalTax = self.addFloatField(value = 0.0, row = 6, column = 1, precision = 2)

    def calculate(self):
        # Variables from the taxform.py that is already written
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0
        taxRate = self.findTaxRate()
        # Get the numbers from the inputs set by the user in __init__ method
        grossIncome = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()
        # Variables from the taxform.py that is already written
        taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
        incomeTax = taxableIncome * taxRate
        # This is what makes sure that when the button is clicked the total tax is set in the last box
        self.totalTax.setNumber(incomeTax)

    def findTaxRate(self):
        status = self.fileStatus.getSelectedButton()
        if status == self.singleFile:
            tax = 0.20
        elif status == self.marriedFile:
            tax = 0.15
        elif status == self.divorcedFile:
            tax = 0.10
        return tax

def main():
    taxCalculator()

if __name__ == "__main__":
    main()

input("pythongui")