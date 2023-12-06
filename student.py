class Student:
    def __init__(self, name, email, major):
        self.name = name
        self.email = email
        self.major = major

    def __str__(self):
        return f"Student: {self.name}, Email: {self.email}, Major: {self.major}"
