n = int(input())
arr = map(int, input().split())
arr_set=set(arr)
arr_list=list(arr_set)
arr_list.sort(reverse=True)
print(arr_list[1])

# set()함수는 내장함수로 가지고 있는 숫자를 겹치지 않고 {}로 표현한다. ex) list1 = [1, 4, 3, 1, 2, 4] 일 때 set(list1) = {1,2,3,4}이다.
# list()함수는 {}로 묶인 함수를 리스트 형태로 바꾼다. -> 2등을 구해야 하므로 정렬을 내림차순으로 바꾸기 위해서
# sort()함수는 리스트의 순서를 정렬하는 함수이다. (reserve=True)면 내림차순, (reserve=False)면 오름차순이다.
# arr_list[1]은 리스트에 2번째에 위치한 값을 의미한다. (1등부터 순서대로 정렬했으므로 2등을 의미한다.)
