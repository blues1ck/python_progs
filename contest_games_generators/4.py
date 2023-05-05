def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        print(a)
        a, b = b, a + b
        
n = int(input('how many Fibonacci numbers do you want? '))
for i in fib(n):
    pass