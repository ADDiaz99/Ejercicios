"""
write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
"""


first = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
second = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

duplicates = []

for i in first:
    if i in second and i not in duplicates:
        duplicates.append(i)

print(duplicates)