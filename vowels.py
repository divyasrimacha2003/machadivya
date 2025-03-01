def countingvowels(s):
    count = 0
    vowels = 'aeiouAEIOU'
    for char in s:
        if char in vowels:
            count += 1
    return count

s = input("Enter a string: ")
print("Number of vowels: ", countingvowels(s))
