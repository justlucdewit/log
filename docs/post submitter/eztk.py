from tkinter import *

def hexFromRgb(r, g, b):
    return "#%02x%02x%02x" % (r,g,b)

class Window(Frame):
    def __init__(self):
        root = Tk()
        Frame.__init__(self, root)
        self.master = root
        self.bgcol="#FFFFFF"
        self.fgcol="#000000"
        self.pack(fill=BOTH, expand=1)

    def set_size(self, width, height):
        self.master.geometry(f"{width}x{height}")

    def set_title(self, title):
        self.master.title(title)

    def set_background(self, r, g, b):
        col = hexFromRgb(r, g, b)
        self.bgcol = col
        self.configure(bg=col)

    def set_foreground(self, r, g, b):
        col = hexFromRgb(r, g, b)
        self.fgcol = col

    def launch(self):
        self.master.mainloop()

    def createLabel(self, xpos, ypos, txt=""):
        lbl = Label(self, text=txt, bg=self.bgcol, fg=self.fgcol)
        lbl.place(x=xpos, y=ypos)
        self.update()
        return eztk_Label(lbl.winfo_width(), lbl.winfo_height(), xpos, ypos)

    def createButton(self, xpos, ypos, txt=""):
        btn = Button(self, text=txt, bg=self.bgcol, fg=self.fgcol)
        btn.place(x=xpos, y=ypos)
        self.update()
        return eztk_Button(btn.winfo_width(), btn.winfo_height(), xpos, ypos)

    def createInput(self, xpos, ypos, lineWidth, lines):
        txt = Text(self, height=lines, width=lineWidth, bg=self.bgcol, fg=self.fgcol)
        txt.place(x=xpos, y=ypos)
        self.update()
        return eztk_Input(txt.winfo_width(), txt.winfo_height(), xpos, ypos)

class eztk_Input:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def show(self):
        print(f"Input[x:{self.x}, y:{self.y}, width:{self.width}, height:{self.height}]")

class eztk_Label:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def show(self):
        print(f"Label[x:{self.x}, y:{self.y}, width:{self.width}, height:{self.height}]")

class eztk_Button:
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def show(self):
        print(f"button[x:{self.x}, y:{self.y}, width:{self.width}, height:{self.height}]")