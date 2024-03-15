def exponential_mapping(numbers, n):
    result = list(map(lambda x: x ** n, numbers))
    return result

numbers = [1, 2, 3, 4, 5]
n = 3
print("Original numbers:", numbers)
print("Numbers raised to the power of", n, ":", exponential_mapping(numbers, n))
