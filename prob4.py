def intersection(list1, list2):
    intersection_list = list(filter(lambda x: x in list2, list1))
    return intersection_list

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Intersection of", list1, "and", list2, ":", intersection(list1, list2))
