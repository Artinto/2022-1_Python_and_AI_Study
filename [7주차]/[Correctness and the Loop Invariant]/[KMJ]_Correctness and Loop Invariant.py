def insertion_sort(l):
    for i in range(1, len(l)):
	  # 1부터 배열의 길이만큼 반복
        j = i-1
        # j를 i-1이라 선언
        key = l[i]
        # 이동시킬 대상을 key로 지정
        while (j >= 0) and (l[j] > a):
	      # j가 0과 같거나 크면서 a가 l[j]보다 클 때
           l[j+1] = l[j]
	         # 오른쪽으로 쉬프트
           j -= 1
	         # j값 줄이기
        l[j+1] = key
        # 만약 while문 조건에 해당되지 않으면 key값(l[i])을 l[j+1]에 저장
        
m = int(input().strip())
# 입력값 받기
ar = [int(i) for i in input().strip().split()]
# ar을 배열의 형태로 입력값 받기
insertion_sort(ar)
# ar 배열 정렬
print(" ".join(map(str,ar)))
# 배열 안 요소들만 출력
