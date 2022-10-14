class Person:
    def __init__(self, first_name: str, last_name: str, siblings: int, sex: str):
        self.first_name = first_name
        self.last_name = last_name
        self.siblings = siblings
        self.sex = sex

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self) -> str:
        return f"{self.get_full_name()} has {self.siblings} sibling(s), sex - {self.sex}"
    

class Student(Person):
    def __init__(self, first_name: str, last_name: str, siblings: int, sex: str, study: str):
        super().__init__(first_name, last_name, siblings, sex)
        self.study = study
    
    def get_study_duration(self):
        studies = {
            "law": 5,
            "computer science": 4,
            "medical": 6,
            "school": 10
            }
        
        if self.study not in studies:
            return "Your study is not on the list yet :)"
        else:
            return f"Your study diration is {studies[self.study]} years. Good luck in finishing it!"


    
class Teacher(Person):
    def __init__(self, first_name: str, last_name: str, siblings: int, sex: str, working_experience: int):
        super().__init__(first_name, last_name, siblings, sex)
        self.working_experience = working_experience
    
    def get_salary(self):
        if self.working_experience in range(5, 9):
            return f"Your salary for your {self.working_experience} year experience is $1000"
        elif self.working_experience >= 10:
            return f"Your salary for your {self.working_experience} year experience is $2000"
        else:
            return "Your salary is $500"


p1 = Person("Bob", "Odenkirk", 1, "male")
s1 = Student("Jesse", "Pinkman", 1, "male", "school")
t1 = Teacher("Walter", "White", 0, "male", 20)

# Питання: чи можна якось передати атрибути дочірніх функцій 
# батьківській функції, щоб батьківська функція враховувала їх та виводила в методі __str__?
# Тобто чи можу я, наприклад, якимось чином, виводячи  print(s1) отримати не тільки ті атрибути,
# що знаходяться в класі Person, а і self.study?