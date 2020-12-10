import random
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("800x600")
root.minsize(800, 600)
root.config(bg="blue")

root.title("Stone Paper Sicciors")
# -after, -anchor, -before, -expand, -fill, -in, -ipadx, -ipady, -padx, -pady, or -side



def paper():

    youc.config(text=f'You : Paper')
    c1 = random.randint(1, 3)
    if c1 == 1:
        c="Rock"
    if c1 == 2:
        c="Paper"
    if c1 == 3:
        c="Sciccors"
    compc.config(text=f'Comp : {c}')
    global yousvar
    global compsvar
    iy = int(yousvar.get())
    ic = int(compsvar.get())
    if c == "Rock":
        iy += 1
        ic += 0
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Paper":
        iy += 0
        ic += 0
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Sciccors":
        iy += 0

        ic += 1
        yousvar.set(iy)
        compsvar.set(ic)
    if ic == 5:
        import jjjj
        root.quit
    if iy == 5:
        import jjjj
        root.quit


def sci():

    youc.config(text="You : Sciccors")
    c1 = random.randint(1, 3)
    if c1 == 1:
        c="Rock"
    if c1 == 2:
        c="Paper"
    if c1 == 3:
        c="Sciccors"
    compc.config(text=f'Comp : {c}')
    global yousvar
    global compsvar
    iy = int(yousvar.get())
    ic = int(compsvar.get())
    if c == "Rock":
        iy += 0
        ic += 1
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Paper":
        iy += 1
        ic += 0
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Sciccors":
        iy += 0

        ic += 0
        yousvar.set(iy)
        compsvar.set(ic)
    if ic == 5:
        import jjjj
        root.quit
    if iy == 5:
        import jjjj
        root.quit


def rock():
    global root
    root.quit

    youc.config(text="You : Rock")
    c1 = random.randint(1, 3)
    if c1 == 1:
        c="Rock"
    if c1 == 2:
        c="Paper"
    if c1 == 3:
        c="Sciccors"
    compc.config(text=f'Comp : {c}')
    global yousvar
    global compsvar
    iy = int(yousvar.get())
    ic = int(compsvar.get())
    if c == "Rock":
        iy+=0
        ic+=0
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Paper":
        iy+=0
        ic+=1
        yousvar.set(iy)
        compsvar.set(ic)
    if c == "Sciccors":
        iy+=1

        ic+=0
        yousvar.set(iy)
        compsvar.set(ic)
    if ic == 5:

        root.quit
        import jjjj
    if iy == 5:

        root.quit
        import jjjj



youc=Label(root, text=f'You : ', font="algerian 50 bold", bg="BLUE", fg="yellow")
youc.pack(anchor="nw")
compc=Label(root, text=f'Comp : ', font="algerian 50 bold", bg="BLUE")
compc.pack(anchor="nw")
yousvar=StringVar()
yousvar.set("0")

compsvar=StringVar()
compsvar.set("0")
cf=Button(root, text="Rock", command=rock).pack(anchor="e")
cs=Button(root, text="Paper", command=paper).pack(anchor="e")
ct=Button(root, text="Sciccors", command=sci)
ct.pack(anchor="e")

"""yousr=Label(root, text="You", font="algerian 50 bold", bg="BLUE", fg="GREEN")
yousr.pack(anchor="sw")
compsr=Label(root, text="Comp", font="algerian 50 bold", bg="BLUE", fg="GREEN")
compsr.pack(anchor="sw")"""
yous=Label(root,textvar=yousvar, font="algerian 50 bold", bg="BLUE", fg="GREEN")
yous.pack(anchor="s")
comps=Label(root, textvar=compsvar, font="algerian 50 bold", bg="BLUE", fg="GREEN")
comps.pack(anchor="s")
root.mainloop()
