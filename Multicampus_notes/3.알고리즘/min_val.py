#배열의 최솟값을 구하는 모듈 만들기
def min_of(lst):
    min_val=lst[0]
    for i in range(1,len(lst)):
        if min_val > lst[i] :
            min_val=lst[i]
    return min_val