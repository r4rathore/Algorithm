class Solution:
    P,F = 1,1
    S = 1
    def Exponential(x: int, n:int):
        if n == 0:
            return 1
        else:
            r = Solution.Exponential(x, n-1)
            Solution.P = Solution.P * x
            Solution.F = Solution.F * n
            return r  + Solution.P/Solution.F

    def exponential_honorsMethod_loop(x:int, n:int):
        result = 1
        i = n
        while i >0:
            result = (x/i) * result + 1
            i = i -1
        return  result

    def exponential_honorsMethod_recursion(x:int, n:int):
        if n == 0:
            return Solution.S
        else:
            Solution.S = (x/n)*Solution.S + 1
            Solution.exponential_honorsMethod_recursion(x, n-1)
        return Solution.S

#print(Solution.Exponential(2,4))

print(Solution.exponential_honorsMethod_recursion(2,4))

