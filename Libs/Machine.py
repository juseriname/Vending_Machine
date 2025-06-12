class Drink:
    def __init__(self,names,price,count):
        self.items_list = names

        self.items_price = price

        self.items_count = count

class VendingMachine(Drink):
    def __init__(self,names,price,count):
        super().__init__(names,price,count)
        self._cash = 0 #총 잔돈
        self._SmallChange=[10,10,10,10] #잔돈 1000 500 100 50

    #돈 관련 메서드
    def add_cash(self,value): #현금 value원 추가
        if value==1000:
            self._SmallChange[0]+=1
        if value==500:
            self._SmallChange[1]+=1
        if value==100:
            self._SmallChange[2]+=1
        if value==50:
            self._SmallChange[3]+=1
        self._cash+=value
        print(f'현재 잔액 : {self._cash}원')

    def refund(self): #잔돈 반환
        temp = [0,0,0,0] #1000 500 100 50
        money=[1000,500,100,50]
        if sum(self._SmallChange)==0: #기계에 잔돈이 없어용
            return -1
        for i in range(0,4):
            if self._cash >= self._SmallChange[i] * money[i]:
                temp[i] = self._SmallChange[i]
                self._cash -= self._SmallChange[i] * money[i]
                self._SmallChange[i] = 0
            else:
                temp[i] = self._cash // money[i]
                self._cash %= money[i]
        return temp

    def get_cash(self): #현재 잔액 가져오기
        #print(f'{self._cash}원이 남았습니다.')
        return self._cash

    #제품 관련
    def item_out(self,index): #현금결제
        if self.items_count[index] != 0:
            if self._cash >= self.items_price[index]:
                print(f'{self._cash} -> {self._cash-self.items_price[index]}')
                self._cash-=self.items_price[index]
                self.items_count[index]-=1
                print(f'{self.items_list[index]}를 샀어요.')
                return 2 #succes
            else:
                print(index, '돈이 부족합니다.')
                return 1 #no money
        else:
            print('재고가 없습니다.')
            return -1 #no items

    def item_out_card(self,index): #카드결제
        if self.items_count[index] != 0:
            self.items_count[index] -= 1
            print(f'{self.items_list[index]}를 샀어요.')
            return 2
        else :
            return -1


    def get_item_info(self,index):
        temp = [self.items_list[index],self.items_price[index],self.items_count[index]]
        return temp

    #관리자 페이지
    ##로그인
    def login(self,password):
        __password = 'password'
        if password == __password:
            return True
        else:
            return False
    ##제품 이름 수정
    def change_name(self,index,sub):
        self.items_list[index] = sub
    ##제품 가격 수정
    def change_price(self,index,sub):
        self.items_price[index] = int(sub)
    ##제품 개수 수정
    def change_count(self,index,value):
        self.items_count[index]+=value
    ##잔돈 개수 받기
    def get_smallchange(self):
        return self._SmallChange
    ##잔돈 수정
    def change_smallchange(self,index,value):
        if self._SmallChange[index] == 0:
            pass
        else:
            self._SmallChange[index]+=value

