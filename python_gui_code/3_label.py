from tkinter import *

root = Tk()
root.title('Application')
root.geometry("480x640")

label1 = Label(root, text ='안녕하세요')
label1.pack()

photo = PhotoImage(file = "gui_basic/img.png")
label2 = Label(root, image =photo)
label2.pack()

def change():
    label1.config(text = '또만나요')
    global photo2 # 전역변수 선언 필요 : 가비지 컬렉션으로 인식하여 삭제될 수 있음. 
    photo2 = PhotoImage(file = "gui_basic/img2.png")
    label2.config(image=photo2)
    
btn = Button(root, text = '클릭', command = change)
btn.pack()

root.mainloop()