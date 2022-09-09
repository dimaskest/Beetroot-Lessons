import random


random_list = []

while True:
    random_list.append(random.randint(1, 100))
    if len(random_list) == 10:
        break

print("The largest number from a list is:", max(random_list))