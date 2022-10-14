class Animal:
    def __init__(self) -> None:
        pass
    def talk(self):
        pass

class Dog(Animal):
    def talk(self):
        return "woof woof"

class Cat(Animal):
    def talk(self):
        return "meow"


dog = Dog()
cat = Cat()

print(dog.talk())
print(cat.talk())