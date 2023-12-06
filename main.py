from student import Student
from course import Course
from enrollment import Enrollment

def main():
    # Instantiate objects and demonstrate the student management system functionality
    student1 = Student("John Doe", "john@example.com", "Computer Science")
    student2 = Student("Jane Smith", "jane@example.com", "Electrical Engineering")

    course1 = Course("CS101", "Introduction to Computer Science")
    course2 = Course("EE201", "Circuit Analysis")

    enrollment1 = Enrollment(student1, course1, "Spring 2023")
    enrollment2 = Enrollment(student2, course2, "Spring 2023")

    print(enrollment1)
    print(enrollment2)

if __name__ == "__main__":
    main()
