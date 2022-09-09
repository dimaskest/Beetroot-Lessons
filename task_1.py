string = input("Enter your string ")

if len(string) >= 2:
        x = string[:2]
        y = string[-2:]
        print(x + y)
else:
        print("Empty String")
