n = int(input('nr do termo: '))


def Fibonacci(n):
    F0 = 0
    F1 = 1
    if n == 1:
        Fn = 0
    elif n == 2:
        Fn = 1
    else:
        for i in range(n-2):
            Fn = F0 + F1
            F0 = F1
            F1 = Fn
        return Fn

print(Fibonacci(n))