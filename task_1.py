with open("myfile.txt", "w") as file:
    file.write("Hello file world!")

with open("myfile.txt") as file:
    text = file.read()
print(text)

# If I write the same code in Python 3.10 (like command line) it works the same and creates this txt file in my PC