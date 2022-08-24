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
    return sorted(arr)
    # sorted 함수를 사용하여 배열 정렬하기
    # 큰 조건없이 모든 입력값을 정렬하기만 하면 되므로 코드 간략화 가능.
    
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
    
