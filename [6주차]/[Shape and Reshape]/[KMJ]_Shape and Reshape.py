import numpy
change_array = numpy.array(input().strip().split(' '),int)
change_array.shape = (3, 3)
print (change_array)

import numpy
my_array=numpy.array(input().strip().split(' '),int)
print (numpy.reshape(my_array,(3,3)))

# 위 4줄은 shape 아래 3줄은 reshape.
# shape는 배열의 형태를 바꿔서 변수에 저정하고, reshape는 배열의 형태를 바꿔서 출력한다.
# 위 4줄에 reshape를 쓰거나 아래 3줄에 shape를 쓰면 오류가 난다.
