def count_substring(string, sub_string):
    a=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:#주어진 문자열을 찾은후에 다음에서 부터 다시 그 문자열을 찾을 수 있도록 if문과 i+len(substring)을 이용
            a+=1
    return a
   

    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
