def bubblesort(array):
    swapped = True
    n = len(array)
    start = 0
    end = n - 1
    while swapped is True:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        if swapped is False:
            break

        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True

        start += 1


list_ = [19, 2, 31, 45, 6, 11, 121, 27]
bubblesort(list_)
print(list_)