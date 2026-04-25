class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks   # list of marks

    def calculate_grade(self):
        avg = sum(self.marks) / len(self.marks)

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


s1 = Student("Rahul", [85, 90, 80])
print("Grade:", s1.calculate_grade())