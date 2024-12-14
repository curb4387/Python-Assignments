from breezypythongui import EasyFrame

class tempCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Temperature Converter", width = 400, height = 175)
        self.addLabel(text = "Fahrenheit", row = 0, column = 0)
        self.fahrenheit = self.addFloatField(value = 32.0, row = 1, column = 0, precision = 2)
        self.addButton(text = ">>>>>", row = 2, column = 0, command = self.calculateF)

        self.addLabel(text = "Celcius", row = 0, column = 1)
        self.celcius = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
        self.addButton(text = "<<<<<", row = 2, column = 1, command = self.calculateC)

    def calculateF(self):
        fahrenheit = self.fahrenheit.getNumber()
        celcius = (fahrenheit - 32) * 5 / 9
        self.celcius.setNumber(celcius)

    def calculateC(self):
        celcius = self.celcius.getNumber()
        fahrenheit = (celcius * 9 / 5) + 32
        self.fahrenheit.setNumber(fahrenheit)

def main():
    tempCalculator()

if __name__ == "__main__":
    main()

input("pythongui")