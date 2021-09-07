list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 3, 5, 7, 9, 11]

list1_as_set = set(list1)
intersection = list1_as_set.intersection(list2)

intersection_as_list = list(intersection)

print(intersection_as_list)
