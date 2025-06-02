class Drink:
    def __init__(self):
        self.items_list = ['아이시스 8.0', '아이시스 8.0', '2% 아쿠아 제로', '레몬워터', '레몬워터', '옥수수 수염차', '옥수수 수염차', '옥수수 수염차', '트레비'
            , '펩시 제로', '펩시', '칠성사이다 제로', '칠성사이다', '망고', '망고', 'Liptea 복숭아', '스퀴즈 사과에이드', '스퀴즈 사과에이드', '스퀴즈 포도에이드'
            , '가나초코', '레쓰비', '핫6 제로', '밀키스', '레쓰비 카페타임', '게토레이 레몬향', '게토레이 레몬향', '코코 포도', '잔치집 식혜']

        self.items_price = [800, 800, 2000, 1800, 1800, 1600, 1600, 2200, 1300, 1300
            , 1100, 1100, 1300, 1300, 1200, 1200, 1200, 1100, 1100, 1100
            , 900, 900, 1300, 1100, 1300, 1200, 1000, 1000, 1000, 1000]

        self.items_count = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10
            , 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
            , 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

class VendingMachine(Drink):
    def __init__(self):
        super().__init__()
        self._cash = 0 #총 잔돈
        self._SmallChange=[10,10,10,10] #잔돈 1000 500 100 50

    #돈 관련 메서드
    def add_cash(self,value): #현금 value원 추가
        if value==1000:
            self._SmallChange[0]+=1
        if value==500:
            self._SmallChange[2]+=1
        if value==100:
            self._SmallChange[1]+=1
        if value==50:
            self._SmallChange[3]+=1
        self._cash+=value
        print(f'현재 잔액 : {self._cash}원')

    def refund(self): #잔돈 반환
        temp = [0,0,0,0] #1000 500 100 50

        if self._cash > self._SmallChange[0]*1000:
            temp[0]=self._SmallChange[0]
            self._cash-=self._SmallChange[0]*1000
        else:
            temp[0] = self._cash//1000
            self._cash %= 1000

        if self._cash > self._SmallChange[1] * 500:
            temp[1] = self._SmallChange[1]
            self._cash -= self._SmallChange[1] * 500
        else:
            temp[1] = self._cash // 500
            self._cash %= 500

        if self._cash > self._SmallChange[2] * 100:
            temp[2] = self._SmallChange[2]
            self._cash -= self._SmallChange[2] * 100
        else:
            temp[2] = self._cash // 100
            self._cash %= 100

        if self._cash > self._SmallChange[3] * 50:
            temp[3] = self._SmallChange[3]
            self._cash -= self._SmallChange[3] * 50
        else:
            temp[3] = self._cash // 50
            self._cash %= 50
        return temp

    def get_cash(self): #현재 잔액 가져오기
        #print(f'{self._cash}원이 남았습니다.')
        return self._cash

    #제품 관련
    def item_out(self,index): #현금결제
        if self.items_count[index-1] > 0:
            if self._cash >= self.items_price[index-1]:
                print(f'{self._cash} -> {self._cash-self.items_price[index-1]}')
                self._cash-=self.items_price[index-1]
                self.items_count[index-1]-=1
                print(f'{self.items_list[index-1]}를 샀어요.')
                #return 2 #succes
            else:
                #return 1 #no money
                print('돈이 부족합니다.')
        else:
            #return -1 #no items #아예 안눌리게 해야함
            print('재고가 없습니다.')

    def item_out_card(self,index): #카드결제
        self.items_count[index - 1] -= 1
        print(f'{self.items_list[index - 1]}를 샀어요.')

    def get_item_info(self,index):
        temp = [self.items_list[index-1],self.items_price[index-1],self.items_count[index-1]]
        return temp

    #관리자 페이지
    ##로그인
    def login(self,password):
        __password = 'password'
        if password == __password:
            return 1
        else:
            return 0
    ##제품 이름 수정
    def change_name(self,index,sub):
        self.items_list[index-1] = sub
    ##제품 가격 수정
    def change_price(self,index,sub):
        self.items_price[index-1] = sub
    ##제품 개수 수정
    def change_count(self,index,value):
        self.items_count[index-1]+=value
    ##잔돈 수정
    def change_smallchange(self,value):
        pass

