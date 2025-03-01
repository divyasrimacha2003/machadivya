def find_missing_number(lst,n):
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(lst)
    return expected_sum - actual_sum

n = int(input("Enter the value of n: "))
lst = list(range(1, n + 1))
missing = int(input("Enter the missing number: "))
lst.remove(missing)

print("List with missing number:", lst)
print("Missing number is:", find_missing_number(lst,n))
