import random

rand_list_1 = []
rand_list_2 = []

while True:
    rand_list_1.append(random.randint(1, 100))
    rand_list_2.append(random.randint(1, 100))
    if len(rand_list_1) == 10:
        break
    
# set_1 = set(rand_list_1)
# set_2 = set(rand_list_2)
set_common = set(rand_list_1).intersection(set(rand_list_2))
list_common = list(set_common)

if len(list_common) > 0:
    print("Common integers between the 2 random lists are:", list_common)
else:
    print("There were no common integers between 2 random lists :(")