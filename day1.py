#!/usr/bin/env python3
# Samuel Horovatin, December 2022

# Part 1
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

# Part 2
max_calories = [0,0,0]
calorie_count = 0
calorie_min = 0
for line in open("./input/day1.txt", "r"):
    if line == "\n":
        calorie_min = min(max_calories[0:2])
        if calorie_count > calorie_min:
            max_calories.remove(calorie_min)
            max_calories.append(calorie_count)
        calorie_count = 0
    else:
        calorie_count = calorie_count + int(line)
print(f"Max calories of top 3 elves: {sum(max_calories)}")
input("Press Enter to continue...")