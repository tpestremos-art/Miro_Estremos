class Student:
    def __init__(self, name):
        self.name = name
      
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_students(self):
        return self.students

    def display_course(self):
        print("Course Name : ", self.course_name)
        for student in self.students:
            print("Student Name : ", student.name)

course = Course("Computer Science 3")

student1 = Student("Angel Ramirez")
student2 = Student("Marvin Villenues")

course.add_student(student1)
course.add_student(student2)

course.display_course()
