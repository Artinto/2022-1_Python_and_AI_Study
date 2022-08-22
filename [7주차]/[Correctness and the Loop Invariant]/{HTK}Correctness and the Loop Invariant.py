def insertion_sort(l):
    for i in range(1, len(l)):#1부터 a의 원소수 반복
        j = i-1 #j를 i-1이라 선언
        a = l[i]
        while (j >= 0) and (l[j] > a):#반복문 이용 
           l[j+1] = l[j]
           j -= 1#j가 0이상이고 l(j)가 l(i)보다 크면  l[j+1] = l[j]이고, j을 1씩 빼주는 것을 반복한다
        l[j+1] = a#그 후 l[j+1]을  l[i]로 교체
        
m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
insertion_sort(ar)
print(" ".join(map(str,ar)))
