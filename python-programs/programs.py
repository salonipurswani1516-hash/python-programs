def factorial(number):
    answer = 1
    for value in range(1, number + 1):
        answer *= value
    return answer


def fibonacci(count):
    numbers = []
    first, second = 0, 1
    for _ in range(count):
        numbers.append(first)
        first, second = second, first + second
    return numbers


def structure_to_dictionary(name, age, course):
    return {"name": name, "age": age, "course": course}


if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("First 7 Fibonacci numbers:", fibonacci(7))
    print("Student dictionary:", structure_to_dictionary("Student", 20, "Computer Science"))
