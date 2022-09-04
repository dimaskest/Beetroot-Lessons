import random


string = input("Enter your word: ")
mixed_string = "".join(random.sample(string, len (string)))

print(f"'{mixed_string}', " * 5)
