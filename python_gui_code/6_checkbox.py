from tkinter import *

root = Tk()
root.title('Application')
root.geometry("480x640")

checkvar = IntVar()
#checkbox = Checkbutton(root, text = '오늘 하루 보지 않기', variable = checkvar)
checkbox = Checkbutton(root, text = '오늘 하루 보지 않기')
checkbox.select()
#checkbox.deselect()
checkbox.pack()

checkvar2 = IntVar()
checkbox2 = Checkbutton(root, text = '일주일동안 보지 않기', variable = checkvar2)
#checkbox2.select()
checkbox.deselect()
checkbox2.pack()


def btncmd():
    print(checkvar.get())
    print(checkvar2.get())
    
btn = Button(root, text = '클릭', command = btncmd) 
btn.pack()

root.mainloop()