strings = ["apple", "banana", "kiwi", "orange", "pear", "grape"]

sorted_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted strings:", sorted_strings)
