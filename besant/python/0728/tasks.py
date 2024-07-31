"""
Question:
You are working in a software company where you need to manage project data. Each project has a list of tasks, and each task has a set of sub-tasks. Your job is to create a system that can handle project data efficiently using Python. You need to demonstrate how changes to the project data can affect the original data using shallow and deep copies.

Requirements:

Create a dictionary representing a project with a list of tasks, where each task is a dictionary containing a list of sub-tasks.
Make a shallow copy and a deep copy of the project data.
Modify the shallow copy and the deep copy to demonstrate the difference between them.
Print the original project data, the shallow copy, and the deep copy after the modifications to show the effects.
"""
import copy

original = [{
    "coding": [
        "write main python file",
        "debug code"
    ],
    "dashboard": [
        "create line chart",
        "create pie chart"
    ]},
    {"blog": [
        "write introduction",
        "write conclusion"
    ],
    "report": [
        "write description",
        "make illustration"
    ]
}]

shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
print(original)
print(shallow_copy)
print(deep_copy)

original[0]["testing"] = ["test copy"]  # this gets added to the shallow also but not the deep copy
shallow_copy.append(0)  # this is added to shallow alone, not original or deep copy
shallow_copy[1]["report"] = []  # changing in shallow one step deep changes the original but not the deep copy
deep_copy.append({"film": ["casting"]})  # adds the dictionary to deep copy only, original and shallow copy not affected

print(original)
print(shallow_copy)
print(deep_copy)
