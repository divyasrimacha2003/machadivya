def intersection(l1, l2):
    result = []
    for item in l1:
        if item in l2 and item not in result:
            result.append(item)
    return result
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))



print(intersection(l1, l2))

