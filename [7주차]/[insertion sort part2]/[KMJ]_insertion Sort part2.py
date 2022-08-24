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



def insertionSort2(n, arr):
    k=0
    # 비교할 대상의 왼쪽 위치(반복한 횟수)를 k로 지정 -> 비교할 대상은 k+1
    while k<n-1: 
    # 반복횟수가 남아있는 동안 반복하기
        key=arr[k+1]
        # 비교할 대상을 key로 지정
        for i in range(k+1):     
        # 비교할 대상이 있는 위치까지 비교 반복
            if arr[i]>arr[k+1]:
            # 만약 비교하는 대상이 비교할 대상보다 크면
                for j in range(k+1,i,-1):            
                    arr[j]=arr[j-1]
                    # 비교하는 대상 오른쪽으로 쉬프트 반복하기
                arr[i]=key
                # 비교하는 대상에 key값 저장
        print(*arr)
        # 정리한 배열 프린트하기
        k+=1
        # 비교할 대상 값 증가
    #반복횟수가 끝나면 비교, 반복 마무리

if __name__ == '__main__':
    n = int(input().strip())
    # 배열의 크기 n에 저장
    arr = list(map(int, input().rstrip().split()))
    # 나머지 입력값 arr 배열에 넣기
    insertionSort2(n, arr)
    # n과 arr에 대한 함수 insertionSort2 사용
