#!/usr/bin/env python3


numbers = [2, 3, 1, 4, 6, 5, 8, 9, 7, 0]

for i in range(len(numbers)):
    for j in range(i, len(numbers), 1):
        if numbers[j] < numbers[i]:
            numbers[j], numbers[i] = numbers[i], numbers[j]

print(numbers)
