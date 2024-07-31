"""
Student Enrollment System
Description:
You need to manage the enrollment of students in different courses. Each course has a unique ID, name, and a set of enrolled student IDs. You need to add a new student to a course, remove a student from a course, and find the course with the maximum number of students enrolled.

Task:
Create a dictionary to store course data where the keys are course IDs and the values are dictionaries containing the course's name and a set of enrolled student IDs.
Add a new student to a course.
Remove a student from a course.
Find the course with the maximum number of students enrolled.
"""
course_data = {
    "cls_001": {
        "name": "python",
        "students": {"s001", "s002", "s003", "s004", "s005"}
    },
    "cls_002": {
        "name": "sql",
        "students": {"s002", "s003", "s005"}
    },
    "cls_003": {
        "name": "data science",
        "students": {"s005", "s006", "s007"}
    },
    "cls_004": {
        "name": "data analysis",
        "students": {"s001", "s004"}
    }
}
print(course_data)

# add student
course_data["cls_004"]["students"].add("s003")

# remove student
course_data["cls_003"]["students"].remove("s005")

print(course_data)

final_name = None
final_count = 0
for course, values in course_data.items():
    length = len(values["students"])
    if length > final_count:
        final_count = length
        final_name = course

print(f"course with maximum number of students: {final_name}")
