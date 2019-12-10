#A-Source Tower
#B-AuxTower
#C-Destination Tower
def TOH(n: int, A:int, B:int,C:int):
    if n < 1:
        return None
    else:
        TOH(n-1, A, C, B)
        print("({} , {})".format(A,C))
        TOH(n-1, B, A, C)
TOH(3, 1, 2, 3)

