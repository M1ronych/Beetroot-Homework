class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}, and I am {self.age} years old"

    def celebrate_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age}"

class Student(Person):
    def __init__(self,name,age,grade,student_id):
        super().__init__(name,age)
        self.grade = grade
        self.student_id = student_id
        self.courses = []

    def enroll(self,course_name):
       if course_name not in self.courses:
          self.courses.append(course_name)
       return f"{self.name} enrolled in {course_name}"

    def list_courses(self):
        return self.courses

    def study(self,subject):
        return f"{self.name} is studing {subject}"

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject = subject
        self.salary = salary
        self.classes_taught = []

    def assign_class(self,class_name):
        if class_name not in self.classes_taught:
            self.classes_taught.append(class_name)
        return f"{self.name} is now teaching {class_name}"

    def list_classes(self):
        return self.classes_taught

    def grade_student(self,student,grade):
        return f"{self.name} graded {student.name}: {grade}"

    def get_salary(self):
        return self.salary

class SchoolCat:
    def __init__(self,name,color,age):
        self.name = name
        self.color = color
        self.age = age

    def meow(self):
        return f"{self.name} says meow!"

    def nap(self):
        return f"{self.name} is taking a nap"

    def age_up(self):
        self.age +=1
        return f"{self.name} is now {self.age} years old"


if __name__ == "__main__":
    student = Student("Denis",16,"9B",1234)
    teacher = Teacher("Mr.Bob",35, "Math", 50000)
    cat = SchoolCat("Ted","gray",5)

    print(student.introduce())
    print(student.enroll("Physics"))
    print(student.study("Physics"))

    print(teacher.introduce())
    print(teacher.assign_class("9B"))
    print(teacher.grade_student(student,"B"))

    print(cat.meow())
    print(cat.nap())
    print(cat.age_up())


