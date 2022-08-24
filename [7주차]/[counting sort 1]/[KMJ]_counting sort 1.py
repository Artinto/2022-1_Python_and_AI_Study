import math
# 수학 라이브러리 불러오기
import os
# 파일의 경로를 관리하는 라이브러리 불러오기
import random
# 랜덤함수 라이브러리 불러오기
import re
# 정규 표현식(Regular Expression) 라이브러리 불러오기
import sys
# 모듈의 경로를 확인하는 라이브러리 불러오기


def countingSort(arr):
    num=[0]*n
    # n크기만큼 num 배열 생성하기
    for i in range(len(arr)):
    # arr의 크기만큼 반복하여 검사하기
        num[arr[i]]+=1
        # num 배열에서 해당 숫자부분의 값을 1씩 증가시키기
    return num
    # num배열 반환하기
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # os 라이브러리에서 환경변수 ['OUTPUT_PATH'] 불러오기
    V = int(input().strip())
    # V에 입력값 받기

    n = int(input().strip())
    # n에 입력값 받기
    arr = list(map(int, input().rstrip().split()))
    # 나머지 입력값 list 형식으로 배열 arr에 받기
    result = countingSort(arr)
    # countingSort 함수대로 result 지정
    fptr.write(str(result) + '\n')
    # result 값을 str형태로 출력하기
    fptr.close()
    # 함수 종료하기
    
