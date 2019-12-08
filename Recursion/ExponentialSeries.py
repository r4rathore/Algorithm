class Solution:
    P,F = 1,1
    def Exponential(x: int, n:int):
        if n == 0:
            return 1
        else:
            r = Solution.Exponential(x, n-1)
            Solution.P = Solution.P * x
            Solution.F = Solution.F * n
            return r  + Solution.P/Solution.F
print(Solution.Exponential(2,4))

