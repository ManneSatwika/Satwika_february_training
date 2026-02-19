# Question 1: Smart Student Eligibility Checker

# Taking inputs
student_name = input("Enter student name: ")
age = int(input("Enter age: "))
percentage = float(input("Enter percentage: "))
family_income = float(input("Enter family income: "))
rural_area = input("Is the student from a rural area? (True/False): ")


rural_area = rural_area == "True"


if (percentage > 85 and family_income < 300000) or (percentage > 90):
    print("Eligible for scholarship")
else:
    print("Not eligible")


print("\nStudent Details:")
print("Name:", student_name)
print("Age:", age)
print("Percentage:", percentage)
print("Family Income:", family_income)
print("Rural Area:", rural_area)
