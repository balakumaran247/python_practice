"""
Problem: A simple student grading system where the user can input student names and their scores. The system will calculate the average score and display the result.
"""
total = int(input("enter the total number of students: "))

students = {}
for _ in range(total):
    detail = input("enter the student and grade separated by comma: ")
    student, grade = detail.split(",")
    students[student.strip()] = float(grade.strip())

add = 0
for i in students.values():
    add += i
count = len(students)
avg = add/count

print(f"Average score of the students: {avg:.2f}")
