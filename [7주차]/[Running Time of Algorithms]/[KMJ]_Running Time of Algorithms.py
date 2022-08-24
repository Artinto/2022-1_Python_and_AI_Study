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


def runningTime(arr):
    count = 0
    # 쉬프트 이동 횟수를 count로 정의하고 처음에는 0으로 초기화
    for i in range(1,len(arr)):
    # 1부터 배열의 길이만큼 반복하기
            while arr[i]<arr[i-1] and i > 0:
            # 왼쪽의 수보다 오른쪽의 수가 더 클때까지
                arr[i] , arr[i-1] = arr[i-1] , arr[i]
                # 왼쪽 수와 오른쪽 수 서로 위치 바꾸기
                count = count+1
                # 이동 횟수 증가시키기
                i = i-1
                # 왼쪽으로 이동 된 값이 그 왼쪽보다 더 작을 경우를 대비하여 i 값 줄이기
    return count
    # 이동 횟수 값 반환하기
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # os 라이브러리에서 환경변수 ['OUTPUT_PATH'] 불러오기
    V = int(input().strip())
    # V에 입력값 받기

    n = int(input().strip())
    # n에 입력값 받기
    arr = list(map(int, input().rstrip().split()))
    # 나머지 입력값 list 형식으로 배열 arr에 받기
    result = runningTime(arr)
    # runningTime 함수대로 result 지정
    fptr.write(str(result) + '\n')
    # result 값을 str형태로 출력하기
    fptr.close()
    # 함수 종료하기
