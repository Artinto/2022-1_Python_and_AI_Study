import numpy
n,m,p=map(int,input().split())n,m,p을 map 함수를 이용해 input값을 정렬해주고 그를 정수형 리스트로 바꿔준다.
array1=numpy.array([input().split() for i in range(n)],int)
array2=numpy.array([input().split() for i in range(m)],int)#주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n,m번 반복한후 정수로 변형해준것을 행렬 array1,2라 선언한다.
print(numpy.concatenate((array1,array2),axis=0)) 이 것을 하나로 합치는데 이때 수직방향으로 합치기 위해 axis를 0으로 설정
