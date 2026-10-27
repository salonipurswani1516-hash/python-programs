"""The improved version of a simple student marks program."""


def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def show_result(student_name, marks):
    average = calculate_average(marks)
    status = "Pass" if average >= 40 else "Needs improvement"
    print(f"{student_name}: average = {average:.1f}, {status}")


if __name__ == "__main__":
    show_result("Student", [75, 68, 82])
