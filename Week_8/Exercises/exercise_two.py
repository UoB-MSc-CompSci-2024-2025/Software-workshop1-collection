class Student:
    def __init__(self, name, course_id, marks):
        self.name = name
        self.course_id = course_id
        self.marks = marks
        self.average = None

    def average_marks(self):
       sum_of_marks = 0
       for mark in self.marks:
           sum_of_marks = mark + sum_of_marks
       self.average =  sum_of_marks / len(self.marks)

    def display_info(self):
        print("Student details are:", self.name, self.course_id, self.average)


student = Student("Belinda", "SWW1", [85, 90, 69])
student.average_marks()
student.display_info()