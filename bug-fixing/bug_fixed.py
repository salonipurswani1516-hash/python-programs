"""Corrected marks calculator.

The bug was using the number of subjects as the total marks.
The fixed version adds the marks before calculating the average.
"""


def calculate_average(marks):
    if len(marks) == 0:
        return 0
    return sum(marks) / len(marks)


marks = [80, 70, 90]
print("Average marks:", calculate_average(marks))
