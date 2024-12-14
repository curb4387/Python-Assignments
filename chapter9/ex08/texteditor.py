from breezypythongui import EasyFrame
import os, os.path

class textEditor(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Text Editor", width = 300, height = 200)
        self.addLabel(text = "Filename", row = 0, column = 0)
        self.filename = self.addTextField(text = "", row = 0, column = 1, columnspan = 2)
        self.addButton(text = "Open", row = 1, column = 0, command = self.openFile)
        self.addButton(text = "Save", row = 1, column = 1, command = self.saveFile)
        self.addButton(text = "New", row = 1, column = 2, command = self.newFile)
        self.textBox = self.addTextArea(text = "", row = 2, column = 0, columnspan = 3, height = 5, wrap = "word")

    def openFile(self):
        filename = self.filename.getText()
        file = open(filename, 'r')
        contents = file.read()
        file.close()
        self.textBox.setText(contents)

    def saveFile(self):
        filename = self.filename.getText()
        file = open(filename, 'w')
        contents = self.textBox.getText()
        file.write(contents)
        file.close()
        self.textBox.setText(contents)

    def newFile(self):
        self.filename.setText("")
        self.textBox.setText("")


def main():
    textEditor()

if __name__ == "__main__":
    main()

input("pythongui")