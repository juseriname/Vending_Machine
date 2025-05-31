import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()

root.title('Application')
root.geometry("480x640")

def info():
    response = msgbox.showinfo('알림', '알림발생.')
    print('알림', response)  
    
def warn():
    response = msgbox.showwarning('경고', '경고발생.')
    print('경고', response)  

def error():
    response = msgbox.showerror('에러', '에러발생.')
    print('에러', response)  
    
def okcancel():
    response = msgbox.askokcancel('확인취소', '확인완료?')
    print('확인취소', response)  

def retrycancel():
    response = msgbox.askretrycancel('재확인', '재확인완료?')
    print('재확인', response)  

def yesno():
    response = msgbox.askyesno('yes/no', 'Yes or No?')
    print('yes/no', response)  
    
def yesnocancel():
    response = msgbox.askyesnocancel(title = None, message = 'yes/no/cancel')
    print('yes/no/cancel', response)  
        
Button(root, command = info, text = '알림').pack()
Button(root, command = warn, text = '경고').pack()
Button(root, command = error, text = '에러').pack()
Button(root, command = okcancel, text = '확인취소').pack()
Button(root, command = retrycancel, text = '재확인').pack()
Button(root, command = yesno, text = '예/아니오').pack()
Button(root, command = yesnocancel, text = '예/아니오/취소').pack()

root.mainloop()