from random import randint
import time


def qsort(arr, ascending = True):
    if len(arr) < 2:
        return arr
    
    pivot = arr[0]    
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i >= pivot]
    
    if len(less) < 5:
        return insertionSort(less) + [pivot] + insertionSort(greater)
    else:
        if ascending:
            return qsort(less) + [pivot] + qsort(greater)
        else:
            return qsort(greater, ascending= False) + [pivot] + qsort(less, ascending = False)


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue
    
    return alist


blist = [randint(0, 1000) for i in range(500)]

start = time.time()
print(qsort(blist))
end = time.time()
print("\n", end - start)

# Сумніваюсь щодо правильності поєднання пошуків та проведення тестів, але чим більше число 
# поставити в умові в рядку 13, тим довше виконується пошук. Цифра 5 ніби виявилась оптимальною, 
# з такою умовою пошук іноді відбувався справді швидше. Але різниця зовсім незначна + не завжди 
# вона позитивна. Не впевнений щодо потрібності поєднання пошуків, хоча знову ж, наврядчи я 
# зробив це правильно :)