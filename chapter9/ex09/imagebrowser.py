from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog

class imageFiles(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, "File Dialog Demo", width = 300, height = 200)
        self.outputArea = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Open", row = 1, column = 0,
                       command = self.openFile)

    def openFile(self):
        fList = [("Image files", "*.gif")]
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = fList)
        self.image = PhotoImage(file = fileName)
        self.outputArea["image"] = self.image

def main():
    imageFiles().mainloop()

if __name__ == "__main__":
 main()