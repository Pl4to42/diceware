from tkinter import *
from tkinter import ttk, Tk
import ctypes
from diceware import get_passphrase

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()

root = Tk()
root.title('Diceware')

mainframe = ttk.Frame(root)
mainframe.grid(column=0, row=0)
mainframe.pack_propagate(0)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

passphrase = StringVar()
passphrase.set('passphrase')


def generate(*args):
    passphrase.set(get_passphrase())


output_label = ttk.Label(mainframe, textvariable=passphrase, justify='center').grid(column=0, columnspan=2, row=0)
generate_button = ttk.Button(mainframe, text='Generate', command=generate).grid(column=0, columnspan=2, row=1)

pad_x = 5
pad_y = 5
for child in mainframe.winfo_children():
    child.grid_configure(padx=pad_x, pady=pad_y)

root.geometry('400x100')
root.resizable(0,0)

root.bind("<Return>", generate)

root.mainloop()
