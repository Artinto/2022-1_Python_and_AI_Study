import textwrap
def wrap(string, max_width):
    result = textwrap.fill(string, width=max_width)
    print(result)#fill 기능은 텍스트로 단일 문단을 묶고 단일 문자열로 반환시켜준다.
