import random


string = input("Enter your word: ")
mixed_string_1 = "".join(random.sample(string, len (string)))
mixed_string_2 = "".join(random.sample(string, len (string)))
mixed_string_3 = "".join(random.sample(string, len (string)))
mixed_string_4 = "".join(random.sample(string, len (string)))
mixed_string_5 = "".join(random.sample(string, len (string)))

print(mixed_string_1, mixed_string_2, mixed_string_3, mixed_string_4, mixed_string_5)
