def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print("List 1: ", list1)
print("List 2: ", list2)

merged_list = merge_sorted_lists(list1, list2)
print("Merged List: ", merged_list)
