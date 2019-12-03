#TimeComplexity -O(n)
#SpaceComplexity -O(n)

def Exponent(m,n):
    if n == 0:
        return 1
    else:
        return Exponent(m,n-1)*m

print(Exponent(2,4))