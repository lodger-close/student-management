class Enrollment:
    def __init__(self, student, course, semester):
        self.student = student
        self.course = course
        self.semester = semester

    def __str__(self):
        return f"Enrollment - {self.student}, {self.course}, Semester: {self.semester}"
