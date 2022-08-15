import numpy 
n , m= map(int, input().split())#n,m을 map 함수를 이용해 input값을 정렬해주고 그를 정수형리스트로 바꿔준다.
array = numpy.array([input().split() for i in range(n)], int)# 주어진 input 값을 먼저 정렬 한 후에,  이런 것을 n번 반복한후 정수로 변형해준것을 행렬 array라 선언한다.
print (array.transpose())#전치
print (array.flatten())#한 곳에 합쳐서 출력
