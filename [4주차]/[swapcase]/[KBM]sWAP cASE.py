# swapcase() 함수 이용

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
# for문 이용
def swap_case(s):
  result = ""                # result 라는 빈 문자열 만들어서 반환
  for A in s:                # 문자열 s의 요소를 각 객체 A로
      if A.isupper():        # A가 대문자면
        result += A.lower()  # 소문자로 바꾸고 result에 저장
      elif A.islower():      # A가 소문자면
        result += A.upper()  # 대문자로 바꾸고 result에 저장
      else: 
        result += A
  return result  

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
