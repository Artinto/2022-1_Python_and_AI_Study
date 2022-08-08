import math

class Complex(object):
    def __init__(self, real, imaginary):
      self.Com=complex(real,imaginary)

    def __add__(self, no):
      a = x.Com+y.Com
      result= '{:.2f}'.format(a)
      new = result[:-1]+"i"
      return new
        
    def __sub__(self, no):
      b = x.Com - y.Com
      result= '{:.2f}'.format(b)
      new = result[:-1]+"i"
      return new
        
    def __mul__(self, no):
      c = x.Com * y.Com
      result= '{:.2f}'.format(c)
      new = result[:-1]+"i"
      return new

    def __truediv__(self, no):
      d = x.Com / y.Com
      if d.imag == 0:
       new_d="%.2f+0.00i" % (d.real)
       return new_d
      
      result= '{:.2f}'.format(d) 
      new = result[:-1]+"i"
      return new

    def mod(self):
       Mod= ((pow(self.Com.real,2) + pow(self.Com.imag,2))**(1/2))
       e = complex(Mod)
       result= '{:.2f}'.format(e)
       new = result[:-1]+"i"
       return new


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')
   
