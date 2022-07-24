def print_rangoli(n):
  alpha='abcdefghijklmnopqrstuvwxyz'
  import string
  design = string.ascii_lowercase   #알파벳 소문자 모아둠
  for i in range(n-1,-n, -1):
    string1 = '-'.join(design[n-1:abs(i):-1] + design[abs(i):n])
    print(string1.center(4 * n - 3, '-'))
print_rangoli(10)
