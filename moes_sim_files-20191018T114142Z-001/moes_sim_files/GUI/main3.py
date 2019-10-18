import tkinter as Tk
import sys

global see


class CoreGUI(object):
    def __init__(self, parent):
        self.parent = parent
        self.InitUI()
        button = Tk.Button(self.parent, text="Start", command=self.main)
        button.grid(column=0, row=1, columnspan=2)

    def main(self):
        see = 'whatever'
        print see

    def InitUI(self):
        self.text_box = Tk.Text(self.parent, wrap='word', height=11, width=50)
        self.text_box.grid(column=0, row=0, columnspan=2, sticky='NSWE', padx=5, pady=5)
        self.text_box.insert(Tk.END, see)
        sys.stdout = StdoutRedirector(self.text_box)


root = Tk.Tk()
gui = CoreGUI(root)
root.mainloop()
