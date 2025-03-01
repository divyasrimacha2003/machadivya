def most_frequent_element(lst):
    max_count = 0
    max_element = None
    for element in lst:
        count = lst.count(element)
        if count > max_count:
            max_count = count
            max_element = element
    return max_element

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print("Most frequent element: ", most_frequent_element(numbers))
