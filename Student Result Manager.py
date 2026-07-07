# Dictionary to store student names and marks
students = {
    "Rahul": 85,
    "Amit": 72,
    "Priya": 91,
    "Pawan": 68,
    "Neha": 79
}
print("Student Marks:")        # Display student records
for name, marks in students.items():
    print(name, ":", marks)

average = sum(students.values()) / len(students)   #Compute average marks
print("\nAverage Marks =", average)

topper = max(students, key=students.get)    #Find topper
print("Topper =", topper)
print("Topper Marks =", students[topper])

def grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    else:
        return "F"

grades = [(name, marks, grade(marks)) for name, marks in students.items()]

print("\nStudent Grades:")
for name, marks, g in grades:
    print(f"{name}: {marks} -> Grade {g}")