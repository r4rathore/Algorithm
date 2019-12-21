def bubblesort(arr:list)->list:
    sizeof_arr = len(arr)
    if sizeof_arr < 1:
        return arr

    for i in range(0, sizeof_arr -2):
        for j in range(0, sizeof_arr - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

print(bubblesort([4,3,4,5,6,1,3,5,8,9]))