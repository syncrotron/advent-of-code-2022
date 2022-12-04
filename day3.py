#!/usr/bin/env python3

# Ascii for lower case is 97-123, upper case is 65-91
ascii_index_list = list(range(97,123)) + list(range(65,91))

misplaced_items_scores = 0
for line in open("./input/day3.txt", "r"):
    # Lines end in \n, thus len is off by one 
    misplaced_item = 0
    first_compartment = set(line[0:((len(line)-1)//2)])
    second_compartment = set(line[((len(line)-1)//2):(len(line)-1)])
    misplaced_item = first_compartment.intersection(second_compartment).pop()
    
    # Will be off by one as list index's start at 0, thus you need a plus 1
    misplaced_items_scores = misplaced_items_scores + ascii_index_list.index(ord(misplaced_item)) + 1

print(f"Priority Sum: {misplaced_items_scores}")
    


    

