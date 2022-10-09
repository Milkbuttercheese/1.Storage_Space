'''
노드 클래스를 정의하기
next: 뒤에 노드를 연결시키기 위해 쓰는 argument
'''
import hashlib
class Node:
    def __init__(self,key,value,next):
        self.key=key
        self.value=value
        self.next=next

'''
해시 테이블을 정의하기
hash_function:원솟값을 해시값에 대응시키는 함수 만드는 함수이다
정수형 자료형인지 확인하고 맞으면 capacity에 나누어 나머지값을 구하고 아닌경우
해시 라이브러리 함수를 이용한다
'''
class ChainedHash:
    def __init__(self,capacity):             
        self.capacity=capacity               
        self.table=[None] * self.capacity 
        
    def hash_function(self,key):  
         if isinstance(key,int):  
            return key % self.capacity
         return (int(hashlib.sha256(str(key).encode()).hexdigest(),16)%self.capacity)    
        

# Chainedhash 인스턴스(해시테이블)과 key를 parameter로 받는 함수이다.
# 특정key값이 가야할 해시테이블의 원소 위치를 찾은 뒤(key값이 정해지면 해시값은 정해진다.
# 그러나 해시값이 같다고 해서 반드시 key값이 같은건 아니다)
# 그 위치의 버킷을 구성하는 노드를 살핀다
# 노드 원소값이 key값과 같은지 대조하고, 아니라면 다음 노드로 대조한다. 이렇게 계속 대조하다가
# key값과 원소값이 일치하는 노드를 찾거나, 빈 노드를 마주하면 검색을 중단한다.


    def search(self,key):
        hash_val = self.hash_function(key)   
        node =self.table[hash_val]           

        while node != None:                   
            if node.key == key:
                return node.value             
            node= node.next                       


# 키가 key이고 값이 value인 원소 추가하는 함수이다.
# 노드를 살필 때 추가하고자 하는 key값과 같은 노드 원솟값이 있다면 실행을 중지한다
# 그 외의 경운 뒤쪽 노드를 살핀다. 빈 노드를 발견하게 되면 while문을 빠져나오게 되고,
# 노드를 추가한다. (새로운 노드= Node(key,value,next=기존 맨앞 노드), 맨앞 노드=새로운 노드 로 정의한다)

    def add_node(self,key,value):
        hash_val= self.hash_function(key)
        node=self.table[hash_val]

        while node != None:
            if node.key== key:                
                return False
            node= node.next

        new_node =Node(key,value,self.table[hash_val])
        self.table[hash_val]= new_node             
        return True           

# 원소를 제거하는 함수이다
# case1.지우고자 하는 노드가 맨 앞에 있다면 
#맨 앞 노드= 기존 두번째 자리 노드를 지정해서, 기존 맨 앞 노드를 지운다
# case2.그 외의 경우엔 어떤 기준 노드 앞 다음 바로 기준 노드 뒤가 이어져서,지우고자 하는 노드를 생략시켜 지운다
# 뒤쪽으로 이동하라: 특정 노드 앞= 기존 특정 노드, 특정 노드= 기존 특정 노드 뒤
# 빈 노드를 마주쳤다면 탐색을 끝내라. 삭제 실패이다

    def remove(self,key):
        hash_val= self.hash_function(key)
        node=self.table[hash_val]
        node_front= None

        while node != None:
            if node.key == key:
                if node_front == None:             
                    self.table[hash_val]=node.next 
                else:
                    node_front.next =node.next     
                return True
            node_front=node                        
            node=node.next                         
        return False                               

    
# 원소를 출력하는 함수이다
# self.capicity는 해시테이블의 길이를 의미한다
# self.table[i]를 통해 맨 앞의 노드를 호출하고,
# 노드가 비어있지 않으면 노드의 key,value값을 호출한 후에
# 다음 노드를 탐색하는 형식으로 진행한다

    #원소를 출력하는 함수
    def dump(self):
        for i in range(self.capacity):
            node=self.table[i]
            print(i,end='')
            while node != None:
                print(f' ->{node.key}({node.value})',end='')
                node=node.next
            print()
                    