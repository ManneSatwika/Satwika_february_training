class User:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def display_details(self):
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")

    def get_name(self):
        return self.__name


class Student(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__courses = []

    def enroll_course(self, course_name):
        self.__courses.append(course_name)
        print(f"{self.get_name()} enrolled in {course_name}")

    def display_details(self):
        super().display_details()
        print("Courses:", self.__courses)


class Mentor(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.__assigned_students = []

    def assign_student(self, student):
        self.__assigned_students.append(student)
        print(f"{student.get_name()} assigned to {self.get_name()}")

    def display_details(self):
        super().display_details()
        print("Assigned:", [s.get_name() for s in self.__assigned_students])


class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def display_all(self, students, mentors):
        print("\nAll Students:")
        for s in students:
            s.display_details()
        print("\nAll Mentors:")
        for m in mentors:
            m.display_details()


def main():
    students = []
    mentors = []
    admin = Admin("Admin", "admin@edtech.com")

    while True:
        print("\n1) Add Student\n2) Add Mentor\n3) Enroll Student\n4) Assign to Mentor\n5) Admin View All\n6) Exit")
        choice = input("Choose: ")

        if choice == "1":
            n = input("Student name: ")
            e = input("Student email: ")
            students.append(Student(n, e))

        elif choice == "2":
            n = input("Mentor name: ")
            e = input("Mentor email: ")
            mentors.append(Mentor(n, e))

        elif choice == "3":
            if not students:
                print("No students yet!")
            else:
                for i, s in enumerate(students):
                    print(i + 1, s.get_name())
                idx = int(input("Pick student: ")) - 1
                course = input("Course name: ")
                students[idx].enroll_course(course)

        elif choice == "4":
            if not mentors or not students:
                print("Add both first!")
            else:
                for i, m in enumerate(mentors):
                    print(i + 1, m.get_name())
                mid = int(input("Pick mentor: ")) - 1
                for i, s in enumerate(students):
                    print(i + 1, s.get_name())
                sid = int(input("Pick student: ")) - 1
                mentors[mid].assign_student(students[sid])

        elif choice == "5":
            admin.display_all(students, mentors)

        elif choice == "6":
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
