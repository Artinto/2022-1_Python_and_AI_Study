N = int(input())
perform = []
for command in range (N):
    command=input().split()
    if command[0] == "insert":
        perform.insert(int(command[1]),int(command[2]))
    elif command[0] == "print":
        print(perform)
    elif command[0] == "remove":
        perform.remove(int(command[1]))
    elif command[0] == "append":
        perform.append(int(command[1]))
    elif command[0] == "sort":
        perform.sort()
    elif command[0] == "pop":
        perform.pop()
    elif command[0] == "reverse":
        perform.reverse()
      
      
      
# 첫 input은 반복횟수, 이후의 input은 명령어와 명령을 수행할 때 필요한 숫자들을 의미한다.
# input에 명령어와 숫자들이 함께 포함되어 있으므로, split()함수를 이용하여 띄어쓰기를 기준으로 구분하여 list에 저장.
# command[0]은 명령어, command[1],command[2]는 명령어를 수행할 때 필요한 숫자들
# insert함수는 perform 리스트에 원하는 순번에 원하는 숫자 추가.
# print함수는 perform 리스트 출력.
# remove함수는 perform 리스트에서 원하는 숫자 삭제.
# append함수는 perform 리스트 마지막에 원하는 숫자 추가.
# sort함수는 perform 리스트 안 숫자들을 크기 순으로 정렬.
# pop함수는 perform 리스트에서 가장 뒤에 있는 수 삭제.
# reverse함수는 perform 리스트의 순서 반대로 정렬.
