# sol 1
def mutate_string (string, position, character):
    A = list(string) # 문자열을 리스트의 형태로 반환
    A[position] = character
    string = ''.join(A) # 리스트를 다시 문자열로
    return string 

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    # sol 2
def mutate_string(string, position, character):
    s = string[:position]+character+string[position+1:]
    return s

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
