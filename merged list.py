list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
merged_list = []
[merged_list.append(item) for item in list1 + list2 if item not in merged_list]

print(merged_list)
