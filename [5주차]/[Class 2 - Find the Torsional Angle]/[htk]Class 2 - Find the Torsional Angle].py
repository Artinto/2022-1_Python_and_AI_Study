class Points(object):
    def __init__(self, x, y, z):
        self.x=x   #첫번째 인자로 인스턴스를 전달하기 위해 self 함수를 사용해 x,y,z값 설정
        self.y=y
        self.z=z
    def __sub__(self, no):
        return Points((self.x-no.x),(self.y-no.y),(self.z-no.z))#point함수를 이용해 좌표를 받아 뺀 좌표 출력(포인트 함수는 좌표를 입력받을 수 있다)

    def dot(self, no):
        return ((self.x*no.x)+(self.y*no.y)+(self.z*no.z))#내적이므로 point함수 이용하지 않고 그대로 내적출력
    def cross(self, no):
        return Points((self.y*no.z-self.z*no.y),(self.z*no.x-self.x*no.z),(self.x*no.y-self.y*no.x))#외적이므로 포인트 함수 이용해 외적 이용)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))           
