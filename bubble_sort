#!/usr/bin/env python3


numbers = [8, 9, 7, 5, 3, 4, 2, 1, 6, 5]
count = 1

for i in range(len(numbers) - count):
    for j in range(len(numbers) - 1):
        if numbers[len(numbers) - 1 - j] < numbers[len(numbers) - 2 - j]:
            numbers[len(numbers) - 1 - j], numbers[len(numbers) - 2 - j] = \
                numbers[len(numbers) - 2 - j], numbers[len(numbers) - 1 - j]
    count += 1

print(numbers)
