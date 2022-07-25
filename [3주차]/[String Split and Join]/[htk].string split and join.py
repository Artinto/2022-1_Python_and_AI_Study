    a=line
    b=a.split(" ")
    c="-".join(b)
    print(c)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
