"""
tkinter
"""

import tkinter
from tkinter import messagebox

class App:

    def __init__(self, parent):
        frame = tkinter.Frame(parent, width=125, height=75)
        frame.pack()
        frame.pack_propagate(0) # prevent frame skink to content

        tkinter.Button(frame, text="Bt1", \
            command=lambda: self._inform("first")).\
            pack(side=tkinter.LEFT)
        tkinter.Button(frame, text="Bt2", \
            command=lambda: self._inform("second")).\
            pack(side=tkinter.LEFT)
        tkinter.Button(frame, text="QUIT", \
            fg="red", command=frame.quit).\
            pack(side=tkinter.RIGHT)

    def _inform(self, num):
        messagebox.showinfo("info", "You pressed the {} button".format(num))

if __name__ == "__main__":
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()
