#text wrap
import textwrap

def wrap(string, max_width):
    b=textwrap.fill(string,max_width)
    return b

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)



#a=textwrap.wrap(str,wid)         리스트형태로 출력
