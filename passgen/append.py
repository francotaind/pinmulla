import math

result = []
def square_root(numbers):
    for number in numbers:
        result.append(math.sqrt(number))
    return result
response = result
numbers = [1, 2, 3, 4, 5, 6]
square_root(numbers)

print(f"response")
