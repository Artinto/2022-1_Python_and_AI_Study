def print_formatted(number):
    A=[format(a)      for a in range(1,number+1,1)]
    B=[format(a, 'o') for a in range(1,number+1,1)]
    C=[format(a, 'X') for a in range(1,number+1,1)]
    D=[format(a, 'b') for a in range(1,number+1,1)]
    for i in range(number):
     print("".join(A[i]).rjust(len(D[-1])),end=" ")
     print("".join(B[i]).rjust(len(D[-1])),end=" ")
     print("".join(C[i]).rjust(len(D[-1])),end=" ")
     print("".join(D[i]).rjust(len(D[-1])))
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
