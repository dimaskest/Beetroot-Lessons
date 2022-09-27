def main():
    try:
        a = int(input("Please enter first number: "))
        b = int(input("Please enter second number: "))        
        result = a**2 / b
    except ValueError:
        a = int(input("Please enter first integer: "))
        b = int(input("Please enter second integer: "))
        result = a**2 / b
    except ZeroDivisionError:
        b = int(input("Please enter >1 number: "))
        result = a**2 / b
    return result
                
print(main())