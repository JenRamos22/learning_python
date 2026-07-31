
def find_smallest(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

result = find_smallest([3, 8, 2, 7, 5])
print(result)


