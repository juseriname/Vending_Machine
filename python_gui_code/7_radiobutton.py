from tkinter import *

root = Tk()
root.title('Application')
root.geometry("480x640")

Label(root, text = '메뉴를 선택하세요:').pack()
radio_var = IntVar()
radio_btn1 = Radiobutton(root, text = '햄버거', value = 1, variable = radio_var)
radio_btn1.select()
radio_btn2 = Radiobutton(root, text = '치즈버거', value = 2, variable = radio_var)
radio_btn3 = Radiobutton(root, text = '치킨버거', value = 3, variable = radio_var)

radio_drn = StringVar()
radio_drn1 = Radiobutton(root, text = '콜라', value = '콜라', variable = radio_drn)
radio_drn1.select()
radio_drn2 = Radiobutton(root, text = '사이다', value = '사이다', variable = radio_drn)
radio_drn3 = Radiobutton(root, text = '환타', value = '환타', variable = radio_drn)

radio_btn1.pack()
radio_btn2.pack()
radio_btn3.pack()
radio_drn1.pack()
radio_drn2.pack()
radio_drn3.pack()

def btncmd():
    print(radio_var.get())
    print(radio_drn.get())
    
btn = Button(root, text = '주문', command = btncmd) 
btn.pack()

root.mainloop()