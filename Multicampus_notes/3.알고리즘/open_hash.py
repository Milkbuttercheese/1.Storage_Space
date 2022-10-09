from enum import Enum
import hashlib

#버킷의 속성:0,1,2 만을 갖는 클래스
class Status(Enum):
    OCCUPIED=0
    EMPTY=1
    DELETED=2
    
#Bucket은 key,value,stat을 갖는 클래스이다
#set 함수를 통해 key,value,stat을 클래스 정의 한후 재정의 가능하다
#set_status는 그중에서도 속성만 따로 재정의하는 함수
class Bucket:
    
    def __init__(self,key=None,value=None,stat= Status.EMPTY):
        self.key=key
        self.value=value
        self.stat=stat
        
    def set(self,key,value,stat):
        self.key=key
        self.value=value
        self.stat=stat
    
    def set_status(self,stat):
        self.stat=stat
        
#해시테이블은 Bucket 객체를 원소로 하는 리스트로 구현한다
class OpenHash:
    def __init__(self,capacity):
        self.capacity= capacity
        self.table=[Bucket()]*self.capacity

# key값이 정수인 경우엔 해시 테이블의 길이로 나누고
# 정수가 아닌경우엔 해시 라이브러리를 이용하여 데이터를 처리해라
    def hash_function(self,key):
        if isinstance(key,int):
            return key % self.capacity
        return(int(hashlib.md5(str(key).encode()).hexdigest(),16)%self.capacity)

#지정해주려는 key값에 대응되는 hash값에 이미 다른 원소가 있는 경우
#다시 한번 위치를 지정해주기 위해 정의해둔 함수
    def rehash_function(self,key):
        return (self.hash_function(key)+1) %self.capacity

#특정 key값에 대응되는 해시값을 찾고, 그 해시값 위치의 노드 상태에 따라
#다른 행동을 하라고 조건을 두었다
#버켓이 비어있을 경우(EMPTY) => 탐색 실패
#버켓이 차있고, 노드 키값이 현재 찾는 키값과 일치하는 경우=> 탐색 성공!
#앞의 두 경우가 아닌 경운(삭제되어 있거나, 차있음에도 일치하지 않는경우)
#다른 위치에 재해시 되어있을 가능성이 존재함을 의미한다
#그러므로 재해시하여 다른 버켓을 탐색한다
    def search_node(self,key):
        hash_val= self.hash_function(key)
        bucket= self.table[hash_val]
        
        for i in range(self.capacity):
            if bucket.stat==Status.EMPTY:
                break
            elif bucket.stat == Status.OCCUPIED and bucket.key==key:
                return bucket
            hash_val = self.rehash_function(hash_val)
            bucket=self.table[hash_val]
        return None

#해시테이블 안에 담겨있는 리턴값 노드는 Bucket 객체로,key/value/stat 특성을 가져 각각을 꺼내 호출해야한다
    def search_val(self,key):
        bucket=self.search_node(key)
        if bucket != None:
            return bucket.value
        else:
            return None

# 이미 특정 key값이 등록되어 있다면 실행 중지
# 비어있거나, 삭제되어 있는 버켓이 있으면 버켓 안을 체우고
# 아닐경우 재해시하라
    def add_bucket(self,key,value):
        if self.search_val(key) != None:
            return False
        
        hash_val= self.hash_function(key)
        bucket= self.table[hash_val]
        
        for i in range(self.capacity):
            if bucket.stat == Status.EMPTY or bucket.stat == Status.DELETED:
                self.table[hash_val] =Bucket(key,value,Status.OCCUPIED)
                return True
            hash_val=self.rehash_function(hash_val)
            bucket= self.table[hash_val]
        return False
    
            

    #키가 key인 원소 삭제하기
    def remove(self,key):
        bucket= self.search_node(key)
        if bucket == None:
            return False
        else:
            bucket.set_status(Status.DELETED)
            return True

    #출력하는 프로그램
    def dump(self):
        for i in range(self.capacity):
            print(f'{i:2} ',end='')
            if self.table[i].stat == Status.OCCUPIED:
                print(f'{self.table[i].key}({self.table[i].value})')
            elif self.table[i].stat== Status.EMPTY:
                print('--미등록--')
            else:
                print('삭제 완료')

        
        
 