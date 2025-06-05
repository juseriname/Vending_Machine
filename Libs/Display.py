import tkinter
from tkinter import *
from Libs.Machine import VendingMachine

root = Tk()
root.title("Vending Machine")
root.geometry("1400x700")
root.resizable(False,False)

m = VendingMachine()
cashs = [20,20,20,20] #사용자가 가지고 있는 현금
items=[]
for i in range(1,31):
    items.append(m.get_item_info(i)) #name, price, count

def get_password():
    global editing

    def comfirm():
        global editing
        in_password = txt.get()
        if m.login(in_password): #비밀번호 맞음?
            editing=True #관리자 권한 있음
            admin_page() #관리자 페이지 들어가기
        print(in_password,editing)
        login_window.destroy()
        editing=False #관리자 권한 없음

    login_window = tkinter.Toplevel(root)
    login_window.title("관리자 로그인")
    login_window.geometry("300x80")

    login_info = tkinter.Label(login_window,text="비밀번호를 입력해 주세요.")
    login_info.pack()

    txt = Entry(login_window, width=30) #textbox로 입력받기.
    txt.pack()

    check_button = Button(login_window,text="확인",command=comfirm,width=8,height=1)
    check_button.pack()

####################### 관리자 페이지
editing = False
def admin_page():
    admin_window = tkinter.Toplevel(root)
    admin_window.title("관리자 페이지")
    admin_window.geometry("1400x700")

####################### 결제 방식 변경
pay_method=False # False -> 현금, True-> 카드
def change_pay_method():
    global pay_method
    if pay_method:
        pay_method = False
        print('현금 결제로 변경')
    else:
        pay_method = True
        print('카드 결제로 변경')

######################### 메뉴바
menu = Menu(root)
menu_admin = Menu(menu,tearoff=0)
menu_admin.add_command(label = 'Login',command=get_password)
menu.add_cascade(label = '관리자 전용', menu = menu_admin)

menu_pay = Menu(menu,tearoff=0)
menu_pay.add_checkbutton(label='카드로 결제',command=change_pay_method)
menu.add_cascade(label='결제 방식',menu= menu_pay)


###################### 기계 동작하는 부분
def buy(num):
    m.item_out(num)
    refresh()


def add_cash(num):
    if cashs[num]:
        if num==0:
            m.add_cash(1000)
        elif num==1:
            m.add_cash(500)
        elif num==2:
            m.add_cash(100)
        elif num==3:
            m.add_cash(50)
        cashs[num]-=1
        refresh()

def refund():
    refund_money = m.refund()
    print('환급된 금액: ',refund_money)
    if refund_money == -1:
        pass
        # 기계에 잔돈이 부족합니다. 관리자에게 문의하십시오.
    cashs[0] += refund_money[0]
    cashs[1] += refund_money[1]
    cashs[2] += refund_money[2]
    cashs[3] += refund_money[3]
    refresh()


def refresh():
    now_cash = Label(root, text=f'현재 잔액 : {m.get_cash()}원',anchor='w',width=15,height=1)
    now_cash.grid(row=1, column=11)

    user_cash1 = Label(root,text=f'1000원 : {cashs[0]}개',anchor='w',width=15,height=1)
    user_cash1.grid(row=2,column=11)
    user_cash2 = Label(root,text=f'500원 : {cashs[1]}개',anchor='w',width=15,height=1)
    user_cash2.grid(row=3,column=11)
    user_cash3 = Label(root,text=f'100원 : {cashs[2]}개',anchor='w',width=15,height=1)
    user_cash3.grid(row=4,column=11)
    user_cash4 = Label(root,text=f'50원 : {cashs[3]}개',anchor='w',width=15,height=1)
    user_cash4.grid(row=5,column=11)


btn_row=[1,3,5]
btn1 = Button(root, text=items[0][0],command=lambda :(buy(0)), width=15,height=1)
btn1.grid(row=btn_row[2],column=1)
btn2 = Button(root, text=items[1][0],command=lambda :(buy(1)), width=15,height=1)
btn2.grid(row=btn_row[2],column=2)
btn3 = Button(root, text=items[2][0],command=lambda :(buy(2)), width=15,height=1)
btn3.grid(row=btn_row[2],column=3)
btn4 = Button(root, text=items[3][0],command=lambda :(buy(3)), width=15,height=1)
btn4.grid(row=btn_row[2],column=4)
btn5 = Button(root, text=items[4][0],command=lambda :(buy(4)), width=15,height=1)
btn5.grid(row=btn_row[2],column=5)
btn6 = Button(root, text=items[5][0],command=lambda :(buy(5)), width=15,height=1)
btn6.grid(row=btn_row[2],column=6)
btn7 = Button(root, text=items[6][0],command=lambda :(buy(6)), width=15,height=1)
btn7.grid(row=btn_row[2],column=7)
btn8 = Button(root, text=items[7][0],command=lambda :(buy(7)), width=15,height=1)
btn8.grid(row=btn_row[2],column=8)
btn9 = Button(root, text=items[8][0],command=lambda :(buy(8)), width=15,height=1)
btn9.grid(row=btn_row[2],column=9)
btn10 = Button(root, text=items[9][0],command=lambda :(buy(9)), width=15,height=1)
btn10.grid(row=btn_row[2],column=10)
btn11 = Button(root, text=items[10][0],command=lambda :(buy(10)), width=15,height=1)
btn11.grid(row=btn_row[1],column=1)
btn12 = Button(root, text=items[11][0],command=lambda :(buy(11)), width=15,height=1)
btn12.grid(row=btn_row[1],column=2)
btn13 = Button(root, text=items[12][0],command=lambda :(buy(12)), width=15,height=1)
btn13.grid(row=btn_row[1],column=3)
btn14 = Button(root, text=items[13][0],command=lambda :(buy(13)), width=15,height=1)
btn14.grid(row=btn_row[1],column=4)
btn15 = Button(root, text=items[14][0],command=lambda :(buy(14)), width=15,height=1)
btn15.grid(row=btn_row[1],column=5)
btn16 = Button(root, text=items[15][0],command=lambda :(buy(15)), width=15,height=1)
btn16.grid(row=btn_row[1],column=6)
btn17 = Button(root, text=items[16][0],command=lambda :(buy(16)), width=15,height=1)
btn17.grid(row=btn_row[1],column=7)
btn18 = Button(root, text=items[17][0],command=lambda :(buy(17)), width=15,height=1)
btn18.grid(row=btn_row[1],column=8)
btn19 = Button(root, text=items[18][0],command=lambda :(buy(18)), width=15,height=1)
btn19.grid(row=btn_row[1],column=9)
btn20 = Button(root, text=items[19][0],command=lambda :(buy(19)), width=15,height=1)
btn20.grid(row=btn_row[1],column=10)
btn21 = Button(root, text=items[20][0],command=lambda :(buy(20)), width=15,height=1)
btn21.grid(row=btn_row[0],column=1)
btn22 = Button(root, text=items[21][0],command=lambda :(buy(21)), width=15,height=1)
btn22.grid(row=btn_row[0],column=2)
btn23 = Button(root, text=items[22][0],command=lambda :(buy(22)), width=15,height=1)
btn23.grid(row=btn_row[0],column=3)
btn24 = Button(root, text=items[23][0],command=lambda :(buy(23)), width=15,height=1)
btn24.grid(row=btn_row[0],column=4)
btn25 = Button(root, text=items[24][0],command=lambda :(buy(24)), width=15,height=1)
btn25.grid(row=btn_row[0],column=5)
btn26 = Button(root, text=items[25][0],command=lambda :(buy(25)), width=15,height=1)
btn26.grid(row=btn_row[0],column=6)
btn27 = Button(root, text=items[26][0],command=lambda :(buy(26)), width=15,height=1)
btn27.grid(row=btn_row[0],column=7)
btn28 = Button(root, text=items[27][0],command=lambda :(buy(27)), width=15,height=1)
btn28.grid(row=btn_row[0],column=8)
btn29 = Button(root, text=items[28][0],command=lambda :(buy(28)), width=15,height=1)
btn29.grid(row=btn_row[0],column=9)
btn30 = Button(root, text=items[29][0],command=lambda :(buy(29)), width=15,height=1)
btn30.grid(row=btn_row[0],column=10)

price_row=[2,4,6]
price1 = Label(root, text=str(items[0][1])+"원")
price1.grid(row=price_row[0], column=1)
price2 = Label(root, text=str(items[1][1])+"원")
price2.grid(row=price_row[0], column=2)
price3 = Label(root, text=str(items[2][1])+"원")
price3.grid(row=price_row[0], column=3)
price4 = Label(root, text=str(items[3][1])+"원")
price4.grid(row=price_row[0], column=4)
price5 = Label(root, text=str(items[4][1])+"원")
price5.grid(row=price_row[0], column=5)
price6 = Label(root, text=str(items[5][1])+"원")
price6.grid(row=price_row[0], column=6)
price7 = Label(root, text=str(items[6][1])+"원")
price7.grid(row=price_row[0], column=7)
price8 = Label(root, text=str(items[7][1])+"원")
price8.grid(row=price_row[0], column=8)
price9 = Label(root, text=str(items[8][1])+"원")
price9.grid(row=price_row[0], column=9)
price10 = Label(root, text=str(items[9][1])+"원")
price10.grid(row=price_row[0], column=10)
price11 = Label(root, text=str(items[10][1])+"원")
price11.grid(row=price_row[1], column=1)
price12 = Label(root, text=str(items[11][1])+"원")
price12.grid(row=price_row[1], column=2)
price13 = Label(root, text=str(items[12][1])+"원")
price13.grid(row=price_row[1], column=3)
price14 = Label(root, text=str(items[13][1])+"원")
price14.grid(row=price_row[1], column=4)
price15 = Label(root, text=str(items[14][1])+"원")
price15.grid(row=price_row[1], column=5)
price16 = Label(root, text=str(items[15][1])+"원")
price16.grid(row=price_row[1], column=6)
price17 = Label(root, text=str(items[16][1])+"원")
price17.grid(row=price_row[1], column=7)
price18 = Label(root, text=str(items[17][1])+"원")
price18.grid(row=price_row[1], column=8)
price19 = Label(root, text=str(items[18][1])+"원")
price19.grid(row=price_row[1], column=9)
price20 = Label(root, text=str(items[19][1])+"원")
price20.grid(row=price_row[1], column=10)
price21 = Label(root, text=str(items[20][1])+"원")
price21.grid(row=price_row[2], column=1)
price22 = Label(root, text=str(items[21][1])+"원")
price22.grid(row=price_row[2], column=2)
price23 = Label(root, text=str(items[22][1])+"원")
price23.grid(row=price_row[2], column=3)
price24 = Label(root, text=str(items[23][1])+"원")
price24.grid(row=price_row[2], column=4)
price25 = Label(root, text=str(items[24][1])+"원")
price25.grid(row=price_row[2], column=5)
price26 = Label(root, text=str(items[25][1])+"원")
price26.grid(row=price_row[2], column=6)
price27 = Label(root, text=str(items[26][1])+"원")
price27.grid(row=price_row[2], column=7)
price28 = Label(root, text=str(items[27][1])+"원")
price28.grid(row=price_row[2], column=8)
price29 = Label(root, text=str(items[28][1])+"원")
price29.grid(row=price_row[2], column=9)
price30 = Label(root, text=str(items[29][1])+"원")
price30.grid(row=price_row[2], column=10)

ins_row=[7] #insert coin
ins1 = Button(root, text='1000원 투입',command=lambda :(add_cash(0)),width=10,height=1)
ins1.grid(row=ins_row[0],column=1)
ins2 = Button(root, text='500원 투입',command=lambda :(add_cash(1)),width=10,height=1)
ins2.grid(row=ins_row[0],column=2)
ins3 = Button(root, text='100원 투입',command=lambda :(add_cash(2)),width=10,height=1)
ins3.grid(row=ins_row[0],column=3)
ins4 = Button(root, text='50원 투입',command=lambda :(add_cash(3)),width=10,height=1)
ins4.grid(row=ins_row[0],column=4)
ins5 = Button(root, text='환급 받기',command=refund,width=10,height=1)
ins5.grid(row=ins_row[0],column=5)


refresh()
root.config(menu = menu)
root.mainloop()

#https://blog.naver.com/dsz08082/221420576638