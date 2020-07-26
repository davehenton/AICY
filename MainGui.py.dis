#Note:
#Commits starting with "#!" are containing code.
#It is there for easily readd removed or unused features

#Imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

#Function called by closing the application, gives us the possibility to finish current task
def onExit():
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        root.destroy()

def listChats(Chat[]):
    for i in Chat[]:
        

#Configuring the "root"
root = Tk()
root.title("AICY")
root.resizable(False, False)
root.protocol('WM_DELETE_WINDOW', onExit)
#!root.columnconfigure(0, weight=1)
#!root.rowconfigure(0, weight=1)

#Configuring the mainframe
mainframe = ttk.Frame(root, padding="768 512 32 32")
#!mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.grid(column=0, row=0)


feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)


root.mainloop()
