#Selection Sort
def swap(i, j, arr:list):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def sort(arr: list):
    size = len(arr)
    for i in range(0,size -1):
        min = arr[i]
        for j in range(i+1, size):
            if arr[j] < arr[i]:
                swap(i, j, arr)
    return arr

print(
    sort(['A','C','B','Z','X']))
