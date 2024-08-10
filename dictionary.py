# Create a dictionary
student_grades = {
    "Raghav sharma": 85,
    "ravi sharma": 90,
    "jashan singh": 78,
    "Ankit jangir": 92
}

# Print the dictionary
print("Student Grades:", student_grades)

# Accessing elements
print("Raghav sharma Grade:", student_grades["Raghav sharma"])

# Adding a new 
student_grades["Pankaj"] = 88
print("Updated Student Grades:", student_grades)

# Removing an element
del student_grades["ravi sharma"]
print("After Removing ravi sharma:", student_grades)

# Iterating over the dictionary
print("Iterating over the dictionary:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

# Checking if a key exists
if "Raghav sharma" in student_grades:
    print("Raghav sharma's grade is in the dictionary.")

# Getting the length of the dictionary
print("Number of students:", len(student_grades))

# Using the get method to access a value
print("Ankit jangir Grade (using get method):", student_grades.get("Ankit jangir"))

#checking number odd or even

# a=int(input("Enter 1st number :"))
# if a%2==0:
#     print("Number is Even")
# else:
#     print("Number is Odd")
