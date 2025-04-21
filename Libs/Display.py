from tkinter import *
root = Tk()
root.title("Vending Machine")
root.geometry("1400x700")
root.resizable(0,0)

def temp():
    print('pressed')

btn1 = Button(root, text="ok",command=temp,width=3,height=1)
btn1.grid(row=1,column=1)
btn2 = Button(root, text="ok",command=temp,width=3,height=1)
btn2.grid(row=2,column=2)





root.mainloop()

#https://blog.naver.com/dsz08082/221420576638