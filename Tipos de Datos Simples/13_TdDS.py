arr = [1, 3, 5, 6, 11, 23]
sum = 9
i = 0
j = 0

for i in arr:
    for j in arr:
        if( i + j == sum):
            print(i, j)
            