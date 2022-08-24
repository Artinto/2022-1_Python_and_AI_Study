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

def introTutorial(V, arr):
    return arr.index(V)
    # arr 배열에서 V를 찾은 후 값 반환

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # os 라이브러리에서 환경변수 ['OUTPUT_PATH'] 불러오기
    V = int(input().strip())
    # V에 입력값 받기

    n = int(input().strip())
    # n에 입력값 받기
    arr = list(map(int, input().rstrip().split()))
    # 나머지 입력값 list 형식으로 배열 arr에 받기
    result = introTutorial(V, arr)
    # introTutorial 함수대로 result 지정
    fptr.write(str(result) + '\n')
    # result 값을 str형태로 출력하기
    fptr.close()
    # 함수 종료하기
