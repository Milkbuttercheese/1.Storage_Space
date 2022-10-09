#fixedstack dtype을 deque를 이용해서 구현해보자
from collections import deque

class Stack:
    # maxlen 길이 만큼의 크기를 가진 빈 deque를 만듬
    def __init__(self,maxlen=256):
        self.capacity=maxlen
        self.__stk=deque([],maxlen)
        
    def __len__(self):
        return len(self.__stk)
    
    def is_empty(self):
        if self.__stk <= 0:
            return True
        return False
    
    def is_full(self):
        if len(self.__stk) == self.__stk.maxlen:
            return True
        return False
    
    def push(self,value):
        self.__stk.append(value)
    
    def pop(self):
        return self.__stk.pop()
    
    def peek(self):
        print(f'peek 값은 {self.__stk[-1]} 입니다')
        return 
    
    def clear(self):
        return self.__stk.clear()
    
    def find(self,value):
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1
        
    def count(self,value):
        return self.__stk.count(value)
    
    def __contains__(self,value):
        return self.count(value)
    
    def dump(self):
        print(list(self.__stk))
    