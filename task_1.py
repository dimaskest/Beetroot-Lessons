import re


class Email:
    def __init__(self, email):
        self.email = self.validate(email)

    @staticmethod
    def validate(email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        
        if re.search(regex, email):
            return email
        else:
            raise ValueError("Wrong format of email")


new_email = Email("aboba@gmail.com")

print(new_email.email)