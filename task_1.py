from tokenize import String


string = input("Enter your string ")


def main(string):
    if len(string) >= 2:
        x = string[:2]
        y = string[-2:]
        print(x + y)
    else:
        print("Empty String")


main(string)