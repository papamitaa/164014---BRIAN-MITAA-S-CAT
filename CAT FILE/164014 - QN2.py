class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    def add_grade(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def display_grades(self):
        for assignment, grade in self.assignments.items():
            print(f"{assignment}: {grade}")

class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def assign_grade(self, student, assignment_name, grade):
        student.add_grade(assignment_name, grade)

    def display_all_students_grades(self):
        # Display instructor's name
        print(f"Instructor: {self.name}")
        print(f"Grades for the course '{self.course_name}':")
        for student in self.students:
            print(f"\nGrades for {student.name}:")
            student.display_grades()

#Student 1
student1 = Student("Nyangwesa", "Student 1")
instructor = Instructor("Mzee Mzima", "Application Programming for the Internet")

#Student 1's credential
instructor.add_student(student1)
instructor.assign_grade(student1, "Assignment 1", 90)
instructor.display_all_students_grades()
