def fun(s):
     try:
        username, url = s.split('@')  #이메일 판단 골뱅이~
        website, extension = url.split('.') ## ksy6591'@'naver'.'com 
     except ValueError:
        return False
     if username.replace('-', '').replace('_', '').isalnum() is False: #언더바 마이너스 없앨때 올 숫자이면 이메일아님
        return False
     elif website.isalnum() is False:  #웹사이트 올 숫자면 이메일아님
        return False
     elif len(extension) > 3: #뒤에 com  처럼 3자리 이하 여야함
        return False
     else:
        return True

        
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
