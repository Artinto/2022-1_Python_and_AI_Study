
def is_leap(a):
 check = False

 if a%4==0:
   check = True;

 if a%100==0:
   check = False;

 if a%400==0:
   check = True;
 return check





year = int(input())
print(is_leap(year))
