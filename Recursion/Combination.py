#nCr

def combination(n:int, r:int)-> int:
    if ((n == r) or (r == 0)):
        return 1
    else:
        return combination(n-1, r-1) + combination(n-1, r)
print(combination(5,2))