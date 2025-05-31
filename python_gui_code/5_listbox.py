from tkinter import *

root = Tk()
root.title('Application')
root.geometry("480x640")

listbox = Listbox(root, selectmode = 'extended', height = 0)
listbox.insert(1, '사과')
listbox.insert(0, '딸기')
listbox.insert(2, '바나나')
listbox.insert(3, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    print('리스트에는 ', listbox.size(), '개가 있습니다. ')
#    listbox.delete(0)
    listbox.delete(END)
    print('리스트에는 ', listbox.size(), '개가 있습니다. ')
    print('리스트에는 [', listbox.get(0, 2), ']가 있습니다. ')
    print('선택된 항목 [', listbox.curselection(), ']가 있습니다. ')
    
btn = Button(root, text = '클릭', command = btncmd) 
btn.pack()

root.mainloop()