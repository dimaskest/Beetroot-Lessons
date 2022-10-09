class Dog:
    age_factor = 7
    def __init__(self, age) -> None:
        self.age = age
    def human_age(self):
        return f"In human equivalent your dog is {self.age * self.age_factor} years old"

doge = Dog(7)

print(doge.human_age())