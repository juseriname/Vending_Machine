import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('Application')
root.geometry("480x640")

values = [str(i) + '일' for i in range(1, 32)]
combobox = ttk.Combobox(root, height = 10, values = values, state = 'readonly')
combobox.current(10)
combobox.pack()
#combobox.set('카드결제일')


def btncmd():
    print(combobox.get())

btn = Button(root, text = '주문', command = btncmd) 
btn.pack()

root.mainloop()