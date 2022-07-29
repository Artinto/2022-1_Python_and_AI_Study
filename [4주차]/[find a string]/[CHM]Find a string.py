def count_substring(string, sub_string):
    if sub_string[0]==sub_string[-1]:
     b=sub_string[:-1]
     a=string.count(b)
     return a
    else:
     a=string.count(sub_string)
     return a
  

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
