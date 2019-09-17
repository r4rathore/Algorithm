#Selection Sort
def swap(i, j, arr:list):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(arr: list):
    size = len(arr)
    for i in range(0,size -1):
        for j in range(0, size-1-i):
            if arr[j] > arr[j+1]:
                swap(j, j+1, arr)
    return arr

print(sort([56,2,87,54,98,1,3,0]))
#sort(['A','C','B','Z','X']))