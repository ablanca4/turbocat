from tkinter import *
import buttonEvents
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self)

        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Turbocat")
        self.pack(fill=BOTH, expand=1)
        importButton = Button(self, text="Import Template", command=buttonEvents.importTemplate)
        importButton.place(x=15, y=15)


root = Tk()
root.geometry("500x500")
app = Window(root)

root.mainloop()