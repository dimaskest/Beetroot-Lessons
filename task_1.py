import multiprocessing
import os


def check_if_prime(num):
    print("Worker process id for {0}: {1}".format(num, os.getpid()))
    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    numbers = [
        2,  # prime
        1099726899285419,
        1570341764013157,  # prime
        1637027521802551,  # prime
        1880450821379411,  # prime
        1893530391196711,  # prime
        2447109360961063,  # prime
        3,  # prime
        2772290760589219,  # prime
        3033700317376073,  # prime
        4350190374376723,
        4350190491008389,  # prime
        4350190491008390,
        4350222956688319,
        2447120421950803,
        5,  # prime
    ]

    p = multiprocessing.Pool()
  
    # map list to target function
    result = p.map(check_if_prime, numbers)
  
    print(result)