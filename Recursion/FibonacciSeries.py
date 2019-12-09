def Fibonacci_Iterative(n:int):
    if n <= 1:
        return n
    t1, t2, s = 1, 1, -1
    for i in range(2, n):
        s = t1 + t2
        t1 = t2
        t2 = s
    return s
print(Fibonacci_Iterative(7))


def Fibonacci_Recursive(n : int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_Recursive(n-1) + Fibonacci_Recursive(n -2)

print(Fibonacci_Recursive(7))

def Fibonacci_Recursive_Memoization(n: int):
    Fibnacci_Dict:dict = {}
    if n <= 1:
        Fibnacci_Dict[n] = n
        return n
    else:
        if Fibnacci_Dict.get(n-1) is None:
            Fibnacci_Dict[n - 1] = Fibonacci_Recursive_Memoization(n - 1)
        if Fibnacci_Dict.get(n-2) is None:
            Fibnacci_Dict[n - 2]  = Fibonacci_Recursive_Memoization(n -2)
        return Fibnacci_Dict[n -1] + Fibnacci_Dict[n -2]

print(Fibonacci_Recursive_Memoization(7))
