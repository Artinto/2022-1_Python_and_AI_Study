x = int(input())
y = int(input())
z = int(input())
n = int(input())
answer = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if not i+j+k == n]
print(answer)

# 리스트 내포(List Comprehensions)란 조건문을 이용하여 리스트의 내용을 추가하거나 수정하는 것을 의미한다.
# 리스트 내포를 사용하지 않으면 i,j,k에 값을 하나하나 할당해 준 뒤 행렬을 작성해야하지만, 리스트 내포를 사용하면 한 줄로 간단하게 정리가 가능하다.
# i는 0부터 x까지, j는 0부터 y까지, k는 0부터 z까지 하나씩 값을 증가시켜 행렬을 작성한다.
# 마지막 if not i+j+k == n으로 인해 x+y+z=n일 때 값을 제외하고 행렬을 만든다.

# answer을 변수로 만들지 않고 바로 print([[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if not i+j+k == n])로 작성하면 코드를 더 줄일 수 있다.
