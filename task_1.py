def oops():
    # a = [1, 2, 3]
    # b = 3
    # return a[b]
    a = {
        "name": "Dmytro"
    }
    return a["age"]

def fix():
    try:
        oops()
    except IndexError:
        print("there is an IndexError")

fix()

# Answer: If I change oops to raise a KeyError my program will raise a KeyError :/