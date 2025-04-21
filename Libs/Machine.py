
class Vending_Machine:
    def __init__(self,cash=0):
        self._cash = cash
        self.items_list = ['아이시스 8.0', '아이시스 8.0', '2% 아쿠아 제로', '레몬워터', '레몬워터', '옥수수 수염차', '옥수수 수염차', '옥수수 수염차', '트레비'
            , '펩시 제로', '펩시', '칠성사이다 제로', '칠성사이다', '망고', '망고', 'Liptea 복숭아', '스퀴즈 사과에이드', '스퀴즈 사과에이드', '스퀴즈 포도에이드'
            , '가나초코', '레쓰비', '핫6 제로', '밀키스', '레쓰비 카페타임', '게토레이 레몬향', '게토레이 레몬향', '코코 포도', '잔치집 식혜']

        self.items_price = [800, 800, 2000, 1800, 1800, 1600, 1600, 2200, 1300, 1300
            , 1100, 1100, 1300, 1300, 1200, 1200, 1200, 1100, 1100, 1100
            , 900, 900, 1300, 1100, 1300, 1200, 1000, 1000, 1000, 1000]

        self.items_count = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10
            , 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
            , 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    def add_50(self):
        self._cash+=50
        self.now_cash()

    def add_100(self):
        self._cash+=100
        self.now_cash()

    def add_500(self):
        self._cash+=500
        self.now_cash()

    def add_1000(self):
        self._cash+=1000
        self.now_cash()

    def item_out(self,i):
        if(self._cash >= self.items_price[i-1]):
            print(f'{self._cash} -> {self._cash-self.items_price[i-1]}')
            self._cash-=self.items_price[i-1]
            print(f'{self.items_list[i-1]}를 샀어요.')
        else:
            print('돈이 부족합니다.')

    def now_cash(self):
        print(f'현재 투입 금액은 {self._cash}원 입니다.')

    def refund(self):
        pass