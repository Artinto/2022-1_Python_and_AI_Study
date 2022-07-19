n = int(raw_input())
integer_list = map(int, raw_input().split())
print(hash(tuple(integer_list)))
    
    
# 해당 문제는 python3가 없어서 python2로 진행. input()->raw_input()
# 둘째 줄 까지는 주어져서 마지막 줄만 작성하면 됨.
# tuple()은 리스트와 다르게 index 안의 값이 고정되어 변경되지 않는 목록이다.
# hash()는 입력값을 고정된 길이의 값으로 변경해주는 함수다.
