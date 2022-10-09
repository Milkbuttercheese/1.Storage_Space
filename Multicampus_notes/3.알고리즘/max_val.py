#배열의 최댓값을 구하는 모듈 만들기
def max_of(lst):
    max_val=lst[0]
    for i in range(1,len(lst)):
        if max_val < lst[i] :
            max_val=lst[i]
    return max_val