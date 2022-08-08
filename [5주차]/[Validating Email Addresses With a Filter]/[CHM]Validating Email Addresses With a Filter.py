def fun(s):
    # return True if s is a valid email, else return False
    a=s.replace(".","@")
    b=a.split("@")
    c=b[0].replace("_","1").replace("_","1")
    if len(b) != 3:
      return False
    if c.isalnum() ==False:
      return False


    username = any(a.isalnum() for a in b[0])
    website = b[1].isalnum()
    extension = b[2].isalpha()

    if username == False:
      return False
    elif website == False:
      return False
    elif extension ==False:
      return False
    elif len(b[2])>3:
      return False
    else:
      return True


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
