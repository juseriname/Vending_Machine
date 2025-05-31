import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title('Application')
root.geometry("480x640")

#progressbar = ttk.Progressbar(root, maximum = 100, mode = 'indeterminate')
progressbar = ttk.Progressbar(root, maximum = 100, mode = 'determinate')
progressbar.start(10)
progressbar.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum = 100, length = 150, variable = p_var2)
progressbar2.pack()

def btncmd():
    progressbar.stop()
    print()

def btncmd2():
    for i in range(101):
        time.sleep(0.01)
        p_var2.set(i)
        progressbar.update()
        print(p_var2.get())
        
btn = Button(root, text = '중지', command = btncmd) 
btn.pack()
btn2 = Button(root, text = '시작', command = btncmd2) 
btn2.pack()

root.mainloop()