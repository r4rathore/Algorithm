import array


def insertion_sort(item: array):
    size = len(item)

    if size is 0:
        return None

    for j in range(1,size):
        key = item[j]

        i = j-1
        while i >= 0 and item[i] > key:
            item[i+1] = item[i]
            i-=1
        item[i+1] = key

    return item


print(insertion_sort([5,2,4,6,1,3]))