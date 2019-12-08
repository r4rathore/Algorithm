import math as mt
def solution(a, b, c, N, M, X):
    mt.pow()
    money_needed:list = c
    for i in range(N):
        money_needed.append(b[i] - a[i])
    stock_money = X
    money_needed.sort()
    left_employee = 0
    for j in range(N+M):
        stock_money = stock_money - money_needed[j]
        if stock_money < 0:
            return left_employee
        left_employee +=1

    return left_employee

N,M,X = map(int, input().split(" "))
a=[]
b=[]
for i in range(N):
    x,y=map(int,input().split(" "))
    a.append(x)
    b.append(y)
c = list(map(int, input().split(" ")))

print(solution(a,b,c,N,M,X))