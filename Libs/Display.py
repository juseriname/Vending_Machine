import tkinter
from itertools import count
from tkinter import *
import tkinter.messagebox as msgbox
from Libs.Machine import VendingMachine

root = Tk()
root.title("Vending Machine")
root.geometry("1400x700")
root.resizable(False,False)

m = VendingMachine()
cash = [20,20,20,20] #사용자가 가지고 있는 현금
items=[]
def __init__():
    global items,m
    for i in range(0,30):
        temp = m.get_item_info(i)
        items.append({'name':temp[0],'price':temp[1],'count':temp[2]}) #name, price, count

def get_password():
    global editing

    def comfirm():
        global editing
        in_password = txt.get()
        login_window.destroy()
        if m.login(in_password): #비밀번호 맞음?
            editing=True #관리자 권한 있음
            admin_page() #관리자 페이지 들어가기
        #print(in_password,editing)
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

    #index.Name[변경],Price[변경],Count[변경]
    #Columns
    column_name = Label(admin_window,text="제품 이름",width=15,height=1)
    column_name.grid(row=1,column=2)

    column_price = Label(admin_window, text="제품 가격",width=15,height=1)
    column_price.grid(row=1, column=5)

    column_count = Label(admin_window, text="제품 수량",width=15,height=1)
    column_count.grid(row=1, column=6)
    #Index
    def adm_draw_index():
        ind1 = Label(admin_window, text="1.", width=2, height=1)
        ind1.grid(row=2, column=1)
        ind2 = Label(admin_window, text="2.", width=2, height=1)
        ind2.grid(row=3, column=1)
        ind3 = Label(admin_window, text="3.", width=2, height=1)
        ind3.grid(row=4, column=1)
        ind4 = Label(admin_window, text="4.", width=2, height=1)
        ind4.grid(row=5, column=1)
        ind5 = Label(admin_window, text="5.", width=2, height=1)
        ind5.grid(row=6, column=1)
        ind6 = Label(admin_window, text="6.", width=2, height=1)
        ind6.grid(row=7, column=1)
        ind7 = Label(admin_window, text="7.", width=2, height=1)
        ind7.grid(row=8, column=1)
        ind8 = Label(admin_window, text="8.", width=2, height=1)
        ind8.grid(row=9, column=1)
        ind9 = Label(admin_window, text="9.", width=2, height=1)
        ind9.grid(row=10, column=1)
        ind10 = Label(admin_window, text="10.", width=2, height=1)
        ind10.grid(row=11, column=1)
        ind11 = Label(admin_window, text="11.", width=2, height=1)
        ind11.grid(row=12, column=1)
        ind12 = Label(admin_window, text="12.", width=2, height=1)
        ind12.grid(row=13, column=1)
        ind13 = Label(admin_window, text="13.", width=2, height=1)
        ind13.grid(row=14, column=1)
        ind14 = Label(admin_window, text="14.", width=2, height=1)
        ind14.grid(row=15, column=1)
        ind15 = Label(admin_window, text="15.", width=2, height=1)
        ind15.grid(row=16, column=1)
        ind16 = Label(admin_window, text="16.", width=2, height=1)
        ind16.grid(row=17, column=1)
        ind17 = Label(admin_window, text="17.", width=2, height=1)
        ind17.grid(row=18, column=1)
        ind18 = Label(admin_window, text="18.", width=2, height=1)
        ind18.grid(row=19, column=1)
        ind19 = Label(admin_window, text="19.", width=2, height=1)
        ind19.grid(row=20, column=1)
        ind20 = Label(admin_window, text="20.", width=2, height=1)
        ind20.grid(row=21, column=1)
        ind21 = Label(admin_window, text="21.", width=2, height=1)
        ind21.grid(row=22, column=1)
        ind22 = Label(admin_window, text="22.", width=2, height=1)
        ind22.grid(row=23, column=1)
        ind23 = Label(admin_window, text="23.", width=2, height=1)
        ind23.grid(row=24, column=1)
        ind24 = Label(admin_window, text="24.", width=2, height=1)
        ind24.grid(row=25, column=1)
        ind25 = Label(admin_window, text="25.", width=2, height=1)
        ind25.grid(row=26, column=1)
        ind26 = Label(admin_window, text="26.", width=2, height=1)
        ind26.grid(row=27, column=1)
        ind27 = Label(admin_window, text="27.", width=2, height=1)
        ind27.grid(row=28, column=1)
        ind28 = Label(admin_window, text="28.", width=2, height=1)
        ind28.grid(row=29, column=1)
        ind29 = Label(admin_window, text="29.", width=2, height=1)
        ind29.grid(row=30, column=1)
        ind30 = Label(admin_window, text="30.", width=2, height=1)
        ind30.grid(row=31, column=1)
    adm_draw_index()
    #Names
    def adm_draw_name():
        #입력창 그리기 #Todo
        global items
        name1 = Entry(admin_window,width=15)
        name1.grid(row=2,column=2)
        name1.insert(END,items[0]['name'])
    adm_draw_name()
####################### 결제 방식 변경
pay_method=False # False -> 현금, True-> 카드
def change_pay_method():
    global pay_method
    if pay_method:
        pay_method = False
        msgbox.showinfo("알림","결제 방식을 현금으로 변경하셨습니다.")
    else:
        pay_method = True
        msgbox.showinfo("알림", "결제 방식을 카드로 변경하셨습니다.")

######################### 메뉴바
menu = Menu(root)
menu_admin = Menu(menu,tearoff=0)
menu_admin.add_command(label = 'Login',command=get_password)
menu.add_cascade(label = '관리자 전용', menu = menu_admin)

menu_pay = Menu(menu,tearoff=0)
menu_pay.add_checkbutton(label='카드로 결제',command=change_pay_method)
menu.add_cascade(label='결제 방식',menu= menu_pay)


###################### 기계 동작하는 부분
def buy(num): #제품번호가 0부터 시작
    terms = m.item_out(num)
    if terms==2:
        msgbox.showinfo("제품 구입",f"{items[num]['name']}을 구입하였습니다.\n재고가 {items[num]['count']-1}개 남았습니다.")
        items[num]['count']-=1
    elif terms==1:
        msgbox.showwarning("잔액 부족",f"잔액이 부족합니다.")
    else:
        msgbox.showerror("재고 부족",f"재고가 부족합니다.")
    draw_money()

def add_cash(num):
    if cash[num]:
        if num==0:
            m.add_cash(1000)
        elif num==1:
            m.add_cash(500)
        elif num==2:
            m.add_cash(100)
        elif num==3:
            m.add_cash(50)
        cash[num]-=1
        draw_money()

def refund():
    refund_money = m.refund()
    print('환급된 금액: ',refund_money)
    if refund_money == -1:
        msgbox.showerror("알람","기계에 잔돈이 부족합니다.\n시설 관리자에게 문의하십시오.")
        # 기계에 잔돈이 부족합니다. 관리자에게 문의하십시오.
    for i in range(4):
        cash[i] += refund_money[i]
    msgbox.showinfo("환급",f"1000원 {refund_money[0]}개\n500원 {refund_money[1]}개\n100원 {refund_money[2]}개\n50원 {refund_money[3]}개\n을 환급했습니다.")
    draw_money()

def draw_money():
    now_cash = Label(root, text=f'현재 잔액 : {m.get_cash()}원',anchor='w',width=15,height=1)
    now_cash.grid(row=1, column=11)

    user_cash1 = Label(root,text=f'1000원 : {cash[0]}개',anchor='w',width=15,height=1)
    user_cash1.grid(row=2,column=11)
    user_cash2 = Label(root,text=f'500원 : {cash[1]}개',anchor='w',width=15,height=1)
    user_cash2.grid(row=3,column=11)
    user_cash3 = Label(root,text=f'100원 : {cash[2]}개',anchor='w',width=15,height=1)
    user_cash3.grid(row=4,column=11)
    user_cash4 = Label(root,text=f'50원 : {cash[3]}개',anchor='w',width=15,height=1)
    user_cash4.grid(row=5,column=11)

def draw_btn():
    btn_row=[1,3,5]
    btn1 = Button(root, text=items[0]['name'],command=lambda :(buy(0)), width=15,height=1)
    btn1.grid(row=btn_row[0],column=1)
    btn2 = Button(root, text=items[1]['name'],command=lambda :(buy(1)), width=15,height=1)
    btn2.grid(row=btn_row[0],column=2)
    btn3 = Button(root, text=items[2]['name'],command=lambda :(buy(2)), width=15,height=1)
    btn3.grid(row=btn_row[0],column=3)
    btn4 = Button(root, text=items[3]['name'],command=lambda :(buy(3)), width=15,height=1)
    btn4.grid(row=btn_row[0],column=4)
    btn5 = Button(root, text=items[4]['name'],command=lambda :(buy(4)), width=15,height=1)
    btn5.grid(row=btn_row[0],column=5)
    btn6 = Button(root, text=items[5]['name'],command=lambda :(buy(5)), width=15,height=1)
    btn6.grid(row=btn_row[0],column=6)
    btn7 = Button(root, text=items[6]['name'],command=lambda :(buy(6)), width=15,height=1)
    btn7.grid(row=btn_row[0],column=7)
    btn8 = Button(root, text=items[7]['name'],command=lambda :(buy(7)), width=15,height=1)
    btn8.grid(row=btn_row[0],column=8)
    btn9 = Button(root, text=items[8]['name'],command=lambda :(buy(8)), width=15,height=1)
    btn9.grid(row=btn_row[0],column=9)
    btn10 = Button(root, text=items[9]['name'],command=lambda :(buy(9)), width=15,height=1)
    btn10.grid(row=btn_row[0],column=10)
    btn11 = Button(root, text=items[10]['name'],command=lambda :(buy(10)), width=15,height=1)
    btn11.grid(row=btn_row[1],column=1)
    btn12 = Button(root, text=items[11]['name'],command=lambda :(buy(11)), width=15,height=1)
    btn12.grid(row=btn_row[1],column=2)
    btn13 = Button(root, text=items[12]['name'],command=lambda :(buy(12)), width=15,height=1)
    btn13.grid(row=btn_row[1],column=3)
    btn14 = Button(root, text=items[13]['name'],command=lambda :(buy(13)), width=15,height=1)
    btn14.grid(row=btn_row[1],column=4)
    btn15 = Button(root, text=items[14]['name'],command=lambda :(buy(14)), width=15,height=1)
    btn15.grid(row=btn_row[1],column=5)
    btn16 = Button(root, text=items[15]['name'],command=lambda :(buy(15)), width=15,height=1)
    btn16.grid(row=btn_row[1],column=6)
    btn17 = Button(root, text=items[16]['name'],command=lambda :(buy(16)), width=15,height=1)
    btn17.grid(row=btn_row[1],column=7)
    btn18 = Button(root, text=items[17]['name'],command=lambda :(buy(17)), width=15,height=1)
    btn18.grid(row=btn_row[1],column=8)
    btn19 = Button(root, text=items[18]['name'],command=lambda :(buy(18)), width=15,height=1)
    btn19.grid(row=btn_row[1],column=9)
    btn20 = Button(root, text=items[19]['name'],command=lambda :(buy(19)), width=15,height=1)
    btn20.grid(row=btn_row[1],column=10)
    btn21 = Button(root, text=items[20]['name'],command=lambda :(buy(20)), width=15,height=1)
    btn21.grid(row=btn_row[2],column=1)
    btn22 = Button(root, text=items[21]['name'],command=lambda :(buy(21)), width=15,height=1)
    btn22.grid(row=btn_row[2],column=2)
    btn23 = Button(root, text=items[22]['name'],command=lambda :(buy(22)), width=15,height=1)
    btn23.grid(row=btn_row[2],column=3)
    btn24 = Button(root, text=items[23]['name'],command=lambda :(buy(23)), width=15,height=1)
    btn24.grid(row=btn_row[2],column=4)
    btn25 = Button(root, text=items[24]['name'],command=lambda :(buy(24)), width=15,height=1)
    btn25.grid(row=btn_row[2],column=5)
    btn26 = Button(root, text=items[25]['name'],command=lambda :(buy(25)), width=15,height=1)
    btn26.grid(row=btn_row[2],column=6)
    btn27 = Button(root, text=items[26]['name'],command=lambda :(buy(26)), width=15,height=1)
    btn27.grid(row=btn_row[2],column=7)
    btn28 = Button(root, text=items[27]['name'],command=lambda :(buy(27)), width=15,height=1)
    btn28.grid(row=btn_row[2],column=8)
    btn29 = Button(root, text=items[28]['name'],command=lambda :(buy(28)), width=15,height=1)
    btn29.grid(row=btn_row[2],column=9)
    btn30 = Button(root, text=items[29]['name'],command=lambda :(buy(29)), width=15,height=1)
    btn30.grid(row=btn_row[2],column=10)

def draw_price():
    price_row=[2,4,6]
    price1 = Label(root, text=str(items[0]['price'])+"원")
    price1.grid(row=price_row[0], column=1)
    price2 = Label(root, text=str(items[1]['price'])+"원")
    price2.grid(row=price_row[0], column=2)
    price3 = Label(root, text=str(items[2]['price'])+"원")
    price3.grid(row=price_row[0], column=3)
    price4 = Label(root, text=str(items[3]['price'])+"원")
    price4.grid(row=price_row[0], column=4)
    price5 = Label(root, text=str(items[4]['price'])+"원")
    price5.grid(row=price_row[0], column=5)
    price6 = Label(root, text=str(items[5]['price'])+"원")
    price6.grid(row=price_row[0], column=6)
    price7 = Label(root, text=str(items[6]['price'])+"원")
    price7.grid(row=price_row[0], column=7)
    price8 = Label(root, text=str(items[7]['price'])+"원")
    price8.grid(row=price_row[0], column=8)
    price9 = Label(root, text=str(items[8]['price'])+"원")
    price9.grid(row=price_row[0], column=9)
    price10 = Label(root, text=str(items[9]['price'])+"원")
    price10.grid(row=price_row[0], column=10)
    price11 = Label(root, text=str(items[10]['price'])+"원")
    price11.grid(row=price_row[1], column=1)
    price12 = Label(root, text=str(items[11]['price'])+"원")
    price12.grid(row=price_row[1], column=2)
    price13 = Label(root, text=str(items[12]['price'])+"원")
    price13.grid(row=price_row[1], column=3)
    price14 = Label(root, text=str(items[13]['price'])+"원")
    price14.grid(row=price_row[1], column=4)
    price15 = Label(root, text=str(items[14]['price'])+"원")
    price15.grid(row=price_row[1], column=5)
    price16 = Label(root, text=str(items[15]['price'])+"원")
    price16.grid(row=price_row[1], column=6)
    price17 = Label(root, text=str(items[16]['price'])+"원")
    price17.grid(row=price_row[1], column=7)
    price18 = Label(root, text=str(items[17]['price'])+"원")
    price18.grid(row=price_row[1], column=8)
    price19 = Label(root, text=str(items[18]['price'])+"원")
    price19.grid(row=price_row[1], column=9)
    price20 = Label(root, text=str(items[19]['price'])+"원")
    price20.grid(row=price_row[1], column=10)
    price21 = Label(root, text=str(items[20]['price'])+"원")
    price21.grid(row=price_row[2], column=1)
    price22 = Label(root, text=str(items[21]['price'])+"원")
    price22.grid(row=price_row[2], column=2)
    price23 = Label(root, text=str(items[22]['price'])+"원")
    price23.grid(row=price_row[2], column=3)
    price24 = Label(root, text=str(items[23]['price'])+"원")
    price24.grid(row=price_row[2], column=4)
    price25 = Label(root, text=str(items[24]['price'])+"원")
    price25.grid(row=price_row[2], column=5)
    price26 = Label(root, text=str(items[25]['price'])+"원")
    price26.grid(row=price_row[2], column=6)
    price27 = Label(root, text=str(items[26]['price'])+"원")
    price27.grid(row=price_row[2], column=7)
    price28 = Label(root, text=str(items[27]['price'])+"원")
    price28.grid(row=price_row[2], column=8)
    price29 = Label(root, text=str(items[28]['price'])+"원")
    price29.grid(row=price_row[2], column=9)
    price30 = Label(root, text=str(items[29]['price'])+"원")
    price30.grid(row=price_row[2], column=10)

def draw_func():
    ins_row=[8] #insert coin
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

    root.grid_rowconfigure(7,minsize=20) #제품 선택과 돈 투입 버튼 분리하기

__init__()
draw_btn()
draw_price()
draw_func()
draw_money()
root.config(menu = menu)
root.mainloop()

#https://blog.naver.com/dsz08082/221420576638