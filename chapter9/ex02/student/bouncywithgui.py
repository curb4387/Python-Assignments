from breezypythongui import EasyFrame

class bouncy(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Bouncy", width = 350, height = 200)
        self.addLabel(text = "Height Dropped", row = 0, column = 0)
        self.addLabel(text = "Bouncy Index", row = 1, column = 0)
        self.addLabel(text = "Number of Bounces", row = 2, column = 0)
        self.heightField = self.addFloatField(value = 0.0, row = 0, column = 1, precision = 2)
        self.bouncyField = self.addFloatField(value = 0.0, row = 1, column = 1, precision = 2)
        self.numBounceField = self.addIntegerField(value = 0, row = 2, column = 1)
        self.addButton(text = "Compute", row = 3, column = 1, command = self.calcBouncy)
        self.addLabel(text = "Distance traveled", row = 4, column = 0)
        self.totalDistance = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2)

    def calcBouncy(self):
        totalDistance = self.heightField.getNumber()
        currentHeight = self.heightField.getNumber()
        bounceNumber = self.numBounceField.getNumber()
        bounceIndex = self.bouncyField.getNumber()
        for i in range(bounceNumber):
            bounceHeight = currentHeight * bounceIndex
            totalDistance += 2 * bounceHeight
            currentHeight = bounceHeight
        totalDistance = totalDistance - bounceHeight
        self.totalDistance.setNumber(totalDistance)

def main():
    bouncy()

if __name__ == "__main__":
    main()

input("pythong")