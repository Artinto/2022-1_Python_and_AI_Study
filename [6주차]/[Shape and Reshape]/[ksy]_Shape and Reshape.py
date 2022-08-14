import numpy
arr = input().strip().split(' ')
b=numpy.array(arr,int)
print(numpy.reshape(b,(3,3)))
#shape 예시
change_array = numpy.array([1,2,3,4,5,6])
change_array.shape = (3, 2)
print (change_array)
