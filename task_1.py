import asyncio
import time


async def fibonacci(num):
    a = 0
    b = 1

    if num ==1:
        return b
    else:
        for i in range(1, num):
            c = a + b
            a = b
            b = c
        return b


async def factorial(num):
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1
    return fact


async def square(num):
    return num**2


async def cube(num):
    return num**3


async def main():
    print(f"started at {time.strftime('%X')}")
    res_1 = await asyncio.gather(*[fibonacci(i) for i in range(1, 10 + 1)])
    res_2 = await asyncio.gather(*[factorial(i) for i in range(1, 10 + 1)])
    res_3 = await asyncio.gather(*[square(i) for i in range(1, 10 + 1)])
    res_4 = await asyncio.gather(*[cube(i) for i in range(1, 10 + 1)])
    print(f"\nFib: {res_1};\nFact: {res_2};\nSquare: {res_3};\nCube: {res_4};\n")
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())