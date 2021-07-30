#!/usr/bin/env python3


numbers = [2, 3, 1, 4, 6, 5, 8, 9, 7, 0]

for i in range(1, len(numbers)):
    check = 0
    count = 0

    while check != 1:
        if numbers[i - count] < numbers[i - 1 - count] and (i - count) != 0:
            numbers[i - count], numbers[i - 1 - count] = \
                numbers[i - 1 - count], numbers[i - count]
            count += 1
        else:
            check = 1

print(numbers)
