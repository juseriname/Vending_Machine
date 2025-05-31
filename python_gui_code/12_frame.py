from tkinter import *

root = Tk()

root.title('Application')
root.geometry("480x640")

Label(root, text = '메뉴를 선택해주세요').pack(side = 'top')

Button(root, text = '주문하기').pack(side = 'bottom')

frame = Frame(root, relief = 'solid', bd =1)
frame.pack(side = 'left', fill = 'both', expand = True)

def btncmd():
    print('버튼클릭')

Button(frame, text = '햄버거', command = btncmd).pack()
Button(frame, text = '치즈버거').pack()
Button(frame, text = '치킨버거').pack()


frame_dr = LabelFrame(root, text = '음료')
frame_dr.pack()
frame_dr.pack(side = 'right', fill = 'both', expand = True)

Button(frame_dr, text = '햄버거', command = btncmd).pack()
Button(frame_dr, text = '치즈버거').pack()
Button(frame_dr, text = '치킨버거').pack()

root.mainloop()