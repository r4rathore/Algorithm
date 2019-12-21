def SelectionSort(arr:list)-> list:
    sizeof_arr = len(arr)
    if sizeof_arr < 1:
        return arr

    for i in range(0, sizeof_arr-1):
        for j in range(i+1, sizeof_arr):
            if arr[i] > arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

print(SelectionSort([4,3,4,5,6,1,3,5,8,9]))