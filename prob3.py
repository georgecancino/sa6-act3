def find_maximum(numbers, compare):
    maximum = numbers[0]
    
    for num in numbers[1:]:
        if compare(num, maximum) > 0:
            maximum = num
    
    return maximum

numbers = [3, 7, 2, 9, 5]
greater = lambda x, y: x - y
print("Maximum number in the list:", find_maximum(numbers, greater))
