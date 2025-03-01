def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

lst = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6, 7]
print("List without duplicates:", remove_duplicates(lst))
