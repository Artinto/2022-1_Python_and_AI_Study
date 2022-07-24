def solve(s):
    t_s=s.split(" ")
    Result=''
    for i in t_s:
        i=i.capitalize()
        if Result== '':
            Result=i
        else:
            Result=Result+' '+i
    return Result
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
