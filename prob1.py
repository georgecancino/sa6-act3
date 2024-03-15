sum_of_digits = lambda x: sum(int(digit) for digit in str(x))

number = 51
print("Sum of digits of", number, "is:", sum_of_digits(number))
