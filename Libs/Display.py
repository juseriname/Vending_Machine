from tkinter import *
from Libs.Machine import VendingMachine

root = Tk()
root.title("Vending Machine")
root.geometry("1400x700")
root.resizable(False,False)

m = VendingMachine()
cashs = [10,10,10,10] #사용자가 가지고 있는 현금


def buy1():
    m.item_out(1)
    refresh()
def buy2():
    m.item_out(2)
    refresh()
def buy3():
    m.item_out(3)
    refresh()
def buy4():
    m.item_out(4)
    refresh()
def buy5():
    m.item_out(5)
    refresh()
def buy6():
    m.item_out(6)
    refresh()
def buy7():
    m.item_out(7)
    refresh()
def buy8():
    m.item_out(8)
    refresh()
def buy9():
    m.item_out(9)
    refresh()
def buy10():
    m.item_out(10)
    refresh()
def buy11():
    m.item_out(11)
    refresh()
def buy12():
    m.item_out(12)
    refresh()
def buy13():
    m.item_out(13)
    refresh()
def buy14():
    m.item_out(14)
    refresh()
def buy15():
    m.item_out(15)
    refresh()
def buy16():
    m.item_out(16)
    refresh()
def buy17():
    m.item_out(17)
    refresh()
def buy18():
    m.item_out(18)
    refresh()
def buy19():
    m.item_out(19)
    refresh()
def buy20():
    m.item_out(20)
    refresh()


def add_cash1():
    if cashs[0]:
        m.add_cash(1000)
        cashs[0]-=1
        refresh()
def add_cash2():
    if cashs[1]:
        m.add_cash(500)
        cashs[1]-=1
        refresh()
def add_cash3():
    if cashs[2]:
        m.add_cash(100)
        cashs[2]-=1
        refresh()
def add_cash4():
    if cashs[3]:
        m.add_cash(50)
        cashs[3]-=1
        refresh()
def refund():
    refund_money = m.refund()
    cashs[0] += refund_money[0]
    cashs[1] += refund_money[1]
    cashs[2] += refund_money[2]
    cashs[3] += refund_money[3]
    refresh()


def refresh():
    now_cash = Label(root, text=f'현재 잔액 : {m.get_cash()}원')
    now_cash.grid(row=1, column=11)

    user_cash1 = Label(root,text=f'1000원 : {cashs[0]}개')
    user_cash1.grid(row=2,column=11)
    user_cash2 = Label(root,text=f'500원 : {cashs[1]}개')
    user_cash2.grid(row=3,column=11)
    user_cash3 = Label(root,text=f'100원 : {cashs[2]}개')
    user_cash3.grid(row=4,column=11)
    user_cash4 = Label(root,text=f'50원 : {cashs[3]}개')
    user_cash4.grid(row=5,column=11)



btn1 = Button(root, text="아이시스 8.0",command=buy1,width=15,height=1)
btn1.grid(row=1,column=1)
btn2 = Button(root, text="아이시스 8.0",command=buy2,width=15,height=1)
btn2.grid(row=1,column=2)
btn3 = Button(root, text="2% 아쿠아 제로",command=buy3,width=15,height=1)
btn3.grid(row=1,column=3)
btn4 = Button(root, text="레몬워터",command=buy4,width=15,height=1)
btn4.grid(row=1,column=4)
btn5 = Button(root, text="레몬워터",command=buy5,width=15,height=1)
btn5.grid(row=1,column=5)
btn6 = Button(root, text="옥수수 수염차",command=buy6,width=15,height=1)
btn6.grid(row=1,column=6)
btn7 = Button(root, text="옥수수 수염차",command=buy7,width=15,height=1)
btn7.grid(row=1,column=7)
btn8 = Button(root, text="옥수수 수염차",command=buy8,width=15,height=1)
btn8.grid(row=1,column=8)
btn9 = Button(root, text="트레비",command=buy9,width=15,height=1)
btn9.grid(row=1,column=9)
btn10 = Button(root, text="펩시 제로",command=buy10,width=15,height=1)
btn10.grid(row=1,column=10)
btn11 = Button(root, text="펩시",command=buy11,width=15,height=1)
btn11.grid(row=3,column=1)
btn12 = Button(root, text="칠성사이다 제로",command=buy12,width=15,height=1)
btn12.grid(row=3,column=2)
btn13 = Button(root, text="칠성사이다",command=buy13,width=15,height=1)
btn13.grid(row=3,column=3)
btn14 = Button(root, text="망고",command=buy14,width=15,height=1)
btn14.grid(row=3,column=4)
btn15 = Button(root, text="망고",command=buy15,width=15,height=1)
btn15.grid(row=3,column=5)
btn16 = Button(root, text="Liptea 복숭아",command=buy16,width=15,height=1)
btn16.grid(row=3,column=6)
btn17 = Button(root, text="스퀴즈 사과에이드",command=buy17,width=15,height=1)
btn17.grid(row=3,column=7)
btn18 = Button(root, text="스퀴즈 사과에이드",command=buy18,width=15,height=1)
btn18.grid(row=3,column=8)
btn19 = Button(root, text="스퀴즈 포도에이드",command=buy19,width=15,height=1)
btn19.grid(row=3,column=9)
btn20 = Button(root, text="가나초코",command=buy20,width=15,height=1)
btn20.grid(row=3,column=10)

price1 = Label(root,text="800원")
price1.grid(row=2,column=1)
price2 = Label(root,text="800원")
price2.grid(row=2,column=2)
price3 = Label(root,text="2000원")
price3.grid(row=2,column=3)
price4 = Label(root,text="1800원")
price4.grid(row=2,column=4)
price5 = Label(root,text="1800원")
price5.grid(row=2,column=5)
price6 = Label(root,text="1600원")
price6.grid(row=2,column=6)
price7 = Label(root,text="1600원")
price7.grid(row=2,column=7)
price8 = Label(root,text="2200원")
price8.grid(row=2,column=8)
price9 = Label(root,text="1300원")
price9.grid(row=2,column=9)
price10 = Label(root,text="1300원")
price10.grid(row=2,column=10)
price11 = Label(root,text="1100원")
price11.grid(row=4,column=1)
price12 = Label(root,text="1100원")
price12.grid(row=4,column=2)
price13 = Label(root,text="1300원")
price13.grid(row=4,column=3)
price14 = Label(root,text="1300원")
price14.grid(row=4,column=4)
price15 = Label(root,text="1200원")
price15.grid(row=4,column=5)
price16 = Label(root,text="1200원")
price16.grid(row=4,column=6)
price17 = Label(root,text="1200원")
price17.grid(row=4,column=7)
price18 = Label(root,text="1100원")
price18.grid(row=4,column=8)
price19 = Label(root,text="1100원")
price19.grid(row=4,column=9)
price20 = Label(root,text="1100원")
price20.grid(row=4,column=10)

btn21 = Button(root, text='1000원 투입',command=add_cash1,width=10,height=1)
btn21.grid(row=5,column=1)
btn22 = Button(root, text='500원 투입',command=add_cash2,width=10,height=1)
btn22.grid(row=5,column=2)
btn23 = Button(root, text='100원 투입',command=add_cash3,width=10,height=1)
btn23.grid(row=5,column=3)
btn24 = Button(root, text='50원 투입',command=add_cash4,width=10,height=1)
btn24.grid(row=5,column=4)
btn25 = Button(root, text='환급 받기',command=refund,width=10,height=1)
btn25.grid(row=5,column=5)
refresh()

root.mainloop()

#https://blog.naver.com/dsz08082/221420576638