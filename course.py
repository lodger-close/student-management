class Course:
    def __init__(self, code, title):
        self.code = code
        self.title = title

    def __str__(self):
        return f"Course: {self.code}, Title: {self.title}"
