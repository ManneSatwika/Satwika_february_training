class User:
def **init**(self, name, user_id):
self.__name = name
self.__user_id = user_id

```
def get_name(self):
    return self.__name

def get_id(self):
    return self.__user_id

def display_details(self):
    print("User:", self.__name, "ID:", self.__user_id)
```

class Student(User):
def **init**(self, name, user_id):
super().**init**(name, user_id)
self.__courses = []

```
def enroll_course(self, course):
    self.__courses.append(course)
    print("Course enrolled successfully")

def display_details(self):
    print("Student:", self.get_name(), "ID:", self.get_id())
    print("Courses:", self.__courses)
```

class Mentor(User):
def **init**(self, name, user_id):
super().**init**(name, user_id)
self.__students = []

```
def assign_student(self, student):
    self.__students.append(student)

def display_details(self):
    print("Mentor:", self.get_name(), "ID:", self.get_id())
    print("Assigned Students:")
    for s in self.__students:
        print(s.get_name())
```

class Admin(User):
def display_all(self, students, mentors):
print("\nAll Students:")
for s in students:
s.display_details()
print("\nAll Mentors:")
for m in mentors:
m.display_details()

students = []
mentors = []
admin = Admin("Admin", "A1")

while True:
print("\n1. Add Student")
print("2. Add Mentor")
print("3. Enroll Course")
print("4. Assign Student to Mentor")
print("5. View All Details")
print("6. Exit")

```
choice = input("Enter choice: ")

if choice == "1":
    name = input("Enter student name: ")
    sid = input("Enter student ID: ")
    students.append(Student(name, sid))

elif choice == "2":
    name = input("Enter mentor name: ")
    mid = input("Enter mentor ID: ")
    mentors.append(Mentor(name, mid))

elif choice == "3":
    sid = input("Enter student ID: ")
    course = input("Enter course: ")
    for s in students:
        if s.get_id() == sid:
            s.enroll_course(course)

elif choice == "4":
    sid = input("Enter student ID: ")
    mid = input("Enter mentor ID: ")
    student_obj = None
    for s in students:
        if s.get_id() == sid:
            student_obj = s
    for m in mentors:
        if m.get_id() == mid and student_obj:
            m.assign_student(student_obj)

elif choice == "5":
    admin.display_all(students, mentors)

elif choice == "6":
    break
```
