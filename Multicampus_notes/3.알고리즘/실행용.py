#pointer를 이용한 연결리스트 클래스 Linkedclass 구현하기

#노드 클래스는 데이터와 뒤쪽 포인터를 갖는다
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    #맨 처음 노드가 하나도 없는 빈 연결 리스트를 생성한다
    def __init__(self):
        self.no=0 #노드의 갯수
        self.head= None  #머리 노드에 대한 참조
        self.current=None #주목 노드에 대한 참조

    #객체의 길이를 반환하는 함수 => 연결리스트의 노드 개수를 반환한다
    def __len__(self):
        return self.no

    #탐색 메소드

    #pointer: 스캔중인 노드의 위치를 표시하는 변수
    #count: 맨 앞에서 몇번째 원소를 스캔하는지 나타내는 변수
    #current:탐색이 성공할 시, 해당위치를 주목current노드 값으로 저장해두고, 탐색을 종료한다
    def search(self,data):
        count=0
        pointer=self.head
        while pointer is not None:
            if pointer.data == data:
                self.current=pointer
                return count
            count= count+1
            pointer= pointer.next
        return -1

    #데이터값이 포함되는지 판단하는 함수 => 포함되면 True를, 그렇지 않으면 False를 반환한다#
    def __contains__(self,data):
        return self.search(data)>=0

    #노드 삽입 메소드

    #머리에 노드를 삽입하는 함수
    def add_first(self,data):
        pointer= self.head   #삽입하기전의 머리노드
        self.head= self.current= Node(data,pointer) #다음 참조로 기존 머리노드를 선택함
        self.no= self.no+1

    #맨끝에 노드를 삽입하는 함수
    def add_last(self,data):
        if self.head is None:     #리스트가 비어있다면
            self.add_first(data)  #맨 앞에 노드를 삽입 => 이경우 pointer=self.head=None이 되겠구만
        else:
            pointer= self.head
            #포인터의 끝까지 가게함
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next= self.current= Node(data,None)
            self.no= self.no +1

    #노드 제거 메소드

    #머리 노드 삭제하기
    def remove_first(self):
        if self.head is not None:
            self.head=self.current=self.head.next
        self.no= self.no -1

    #꼬리 노드 삭제하기
    def remove_last(self):
        #노드가 1개인 경우
        if self.head is not None:
            if self.head.next is None:
                self.remove_first()
            else:
                pointer=self.head #스캔 중인 노드
                pre= self.head    #스캔 중인 노드의 앞쪽 노드

                #pointer가 노드의 맨 끝으로 가라
                while pointer.next is not None:
                    pre=pointer
                    pointer=pointer.next
                #pre 뒤 꼬리 노드를 삭제
                pre.next= None
                self.current= pre
                self.no = self.no -1

    def remove(self,p):
        if self.head is not None:
            #p(pointer)가 머리 노드이면
            if p is self.head:
                self.remove_first()
            else:
                pointer= self.head()

            #pointer가 p 바로 왼쪽 옆에 오기까지 전진
            while pointer.next is not p:
                pointer=pointer.next
                if pointer is None:
                    return #pointer는 리스트에 존재하지 않는다=> 노드 p는 연결 리스트 내 존재 X

            pointer.next= p.next
            self.current = pointer
            self.no= self.no -1

    def remove_current_node(self):
        self.remove(self.current)

    #머리 노드가 빌 때 까지 머리노드를 삭제하는 명령어
    def clear(self):
        while self.head is not None:
            self.remove_first()
            self.current= None
            self.no=0

    #노드 이동 메소드

    #주목 노드를 한칸 뒤로 이동시키기
    def next(self):
        #현재 주목 노드가 비어있거나, 현재 주목 노드의 다음이 비어있다면 실행 불가로 return False
        if self.current is None or self.current.next is None:
            return False
        self.current= self.current.next
        return True

    #노드 출력 메소드

    #주목 노드를 출력시키는 함수
    def print_current_node(self):
        if self.current is None:
            print('주목 노드가 존재하지 않습니다')
        else:
            print(self.current.data)

    #모든 노드의 데이터값을 출력시키기
    def print_all_node(self):
        pointer=self.head

        while pointer is not None:
            print(pointer.data)
            pointer= pointer.next

    def __iter__(self):
        return LinkedListIterator(self.head)

#클래스 LinkedList의 이터레이터용 클래스
#iterator: 값을 차례대로 꺼내어 쓸 수 있는 객체
#raise StopIteration
class LinkedListIterator:

    def __init__(self,head):
        self.current= head

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data= self.current.data
            self.current= self.current.next
            return data

#포인터로 연결 리스트 프로그램 만들기
from enum import Enum

Menu= Enum('Menu',['머리에노드삽입','꼬리에노드삽입','머리노드삭제','꼬리노드삭제','주목노드출력','주목노드이동','주목노드삭제','모든노드삭제' \
    ,'검색','멤버십판단','모든노드출력','스캔','종료'])

def select_Menu():
    s=[f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s,sep='',end='')
        n=int(input(': '))
        if 1<= n<= len(Menu):
            return Menu(n)

lst= LinkedList()

while True:
    menu =select_Menu()

    if menu== Menu.머리에노드삽입:
        lst.add_first(int(input('머리 노드에 넣을 값을 입력하세요.')))

    elif menu==Menu.꼬리에노드삽입:
        lst.add_last(int(input('꼬리 노드에 넣을 값을 입력하세요.')))

    elif menu==Menu.머리노드삭제:
        lst.remove_first()

    elif menu== Menu.꼬리노드삭제:
        lst.remove_last()

    elif menu== Menu.주목노드출력:
        lst.print_current_node()

    elif menu== Menu.주목노드이동:
        lst.next()

    elif menu== Menu.주목노드삭제:
        lst.remove_current_node()

    elif menu == Menu.모든노드삭제:
        lst.clear()

    elif menu== Menu.검색:
        pos=lst.search(int(input('검색할 값을 입력하세요')))
        if pos >=0:
            print(f'그 값의 데이터는 {pos+1}번째에 있습니다')
        else:
            print('해당하는 데이터값은 리스트 내에 없습니다')

    elif menu==Menu.멤버십판단:
        print('그 값의 데이터는 포함되어'+('있습니다' if int(input('판단할 값을 입력해주세요')) in lst else '있지 않습니다'))

    elif menu == Menu.모든노드출력:
        lst.print_all_node()

    elif menu== Menu.스캔:
        for e in lst:
            print(e)
    else:
        break

#%%
