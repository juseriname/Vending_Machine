from Libs.Machine import VendingMachine
from Libs import Display

import Libs.Machine
items_list = ['아이시스 8.0','아이시스 8.0','2% 아쿠아 제로','레몬워터','레몬워터','옥수수 수염차','옥수수 수염차','옥수수 수염차','트레비'
    ,'펩시 제로','펩시','칠성사이다 제로','칠성사이다','망고','망고','Liptea 복숭아','스퀴즈 사과에이드','스퀴즈 사과에이드','스퀴즈 포도에이드'
    ,'가나초코','레쓰비','hot6 zero','밀키스','레쓰비 카페타임','게토레이 레몬향','게토레이 레몬향','코코 포도','잔치집 식혜']
#10
#20
#30
m=VendingMachine()
m.add_cash(1000)
m.item_out(7)
m.add_cash(1000)
m.item_out(7)
m.now_cash()
#Display.temp()