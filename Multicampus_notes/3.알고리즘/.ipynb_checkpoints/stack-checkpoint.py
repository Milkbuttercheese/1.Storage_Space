class Stack:
    #스택 본체(리스트로 구현),스택의 크기, 스택에 체워진 원소수를 지정한다 
    def __init__(self,capacity,int=256):
        self.stk=[None]*capacity
        self.capacity=capacity
        self.ptr=0
     
    #스택에 쌓여있는 데이터수를 반환해주는 함수   
    #__len__으로 표기하면
    #obj.__len__()뿐만 아니라 len(obj)으로, 인스턴스를 입력하는 방식으로도 호출할 수 있다
    def __len__(self):
        return self.ptr
    
    #스택이 비어있는지 판단하는 함수
    def is_empty(self):
        if self.ptr > 0 : 
            return False 
        return True
     
    #스택이 가득 차있는지 판단하는 함수
    def is_full(self):
        if self.ptr == self.capacity:
            return True
        return False
    
    #푸시push: 스택 꼭대기에 값이 value인 데이터를 삽입하는 함수
    def push(self,value):
        if self.is_full():
            print('스택이 가득 차있습니다')
            return 
        self.stk[self.ptr]=value
        self.ptr= self.ptr+1
    
    #팝pop: 스택 꼭대기의 데이터를 꺼내는(스택에서 꼭대기 데이터를 삭제하고,출력하는) 함수
    def pop(self):
        if self.is_empty():
            print('스택이 비어 있습니다')
            return 
        self.ptr= self.ptr-1
        print(f'팝한 데이터는{self.stk[self.ptr]}입니다')
        return self.stk[self.ptr] 
    
    #피크peek: 스택 꼭대기의 데이터를 들여다보는 함수
    def peek(self):
        if self.is_empty():
            print('스택이 비어있습니다')
            return 
        print(f'피크한 데이터는{self.stk[self.ptr-1]}입니다')
        return 
    
    #클리어clear: 스택의 모든 데이터를 비우는 함수
    def clear(self):
        self.ptr=0
        
    #파인드find:데이터를 검색하는 함수/ 꼭대기부터 바닥쪽으로 선형검색을 한다
    #for range에서 두번째parameter가 첫번째 parameter보다 작은경우 첫번째 parameter가 우경계가 되며
    #두번째 parameter는 좌경계값이 되고, 경계값을 포함하지 않는다
    #검색이 성공하면 그 위치의 인덱스를, 실패하면 -1을 반환한다
    def find(self,value):                  
        for i in range(self.ptr-1,-1,-1):
            if self.stk[i] == value:
                return i
        return -1
    
    #카운트count:스택에 특정값value를 갖는 원소의 갯수를 카운트한다
    def count(self,value):
        c=0
        for i in range(self.ptr):
            if self.stk[i] == value:
                c=c+1
        return c
    
    #__contains__:스택안에 특정값value를 갖는 데이터가 포함되어 있는지 확인한다
    #__contains__로 표기하면 obj.__contains__(x) 표기 뿐만 아니라 ,
    # x in obj로, 인스턴스의 멤버십 판단을 할 수 있다
    def __contains__(self,value):
        if self.count(value)>0:
            return True
        return False
    
    #덤프dump:스택안의 데이터를 바닥부터 꼭대기순으로 출력하기(보여주기)
    def dump(self):
        if self.is_empty():
            print('스택이 비어있습니다')
        else:
            print(self.stk[:self.ptr])