#!/usr/bin/env python3

max_calories = 0
calorie_count = 0
for line in open("./input/day1.txt", "r"):
    if line == "\n":
        max_calories = max(max_calories, calorie_count)
        calorie_count = 0
    else:
        calorie_count = calorie_count + int(line)
print(f"Max calories: {max_calories}")
input("Press Enter to continue...")