def fib(num):
    a, b = 0, 1  # Set the initial values
    for i in range(0, num):
        yield i+1, a
        a, b = b, a+b

for item in fib(100):
    print(item)
