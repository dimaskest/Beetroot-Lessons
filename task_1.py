def binary_search(array, low, high, x):

    if high >= low:
        mid = (high + low) // 2
        if array[mid] == x:
            return mid
        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)
        else:
            return binary_search(array, mid + 1, high, x)
    else:
        return None


a = [i for i in range(0, 100 + 1)]
res = binary_search(a, 0, len(a) - 1, 63)

if res != None:
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")