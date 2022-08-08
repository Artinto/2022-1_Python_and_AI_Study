cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    _curr, _next = 0, 1
    for _ in range(n):
        yield _curr
        _curr, _next = _next, _curr + _next

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
