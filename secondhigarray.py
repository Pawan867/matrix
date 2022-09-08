list1 = [16, 26, 18, 2, 39, 5, 55, 89, 105]


list2 = list(set(list1))


list2.sort()


print("Second largest element is:", list2[-2])
