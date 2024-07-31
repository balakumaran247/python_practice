"""
Question 2: Student Grades Analysis
Description:
You need to manage student grades for a class. Each student has a unique ID, name, and a list of grades. You need to calculate the average grade for each student and identify the student with the highest average grade.

Task:
Create a dictionary to store student data where the keys are student IDs and the values are dictionaries containing the student's name and a list of grades.
Add a new grade to a student's record.
Calculate the average grade for each student.
Find the student with the highest average grade.
"""
total = int(input("number of student records to create: "))

register = {}
for _ in range(total):
    idx = input("enter the student id: ")
    name = input("enter the student name: ")
    mark_input = input("enter the grades separated by comma: ")
    marks = []
    for i in mark_input.split(","):
        marks.append(float(i))
    register[idx] = {name: marks}

average = {}
for rec in register.values():
    for n, l in rec.items():
        add = 0
        for j in l:
            add += j
        count = len(l)
        avg = add/count
        average[n] = avg

final_name = None
final_avg = 0

for fn, fa in average.items():
    if fa > final_avg:
        final_name = fn
        final_avg = fa

print(f"Student '{final_name}' is the highest with average score {final_avg}")
