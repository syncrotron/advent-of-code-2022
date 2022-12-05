# Samuel Horovatin, December 2022

subset_count = 0
for line in open("./input/day4.txt"):
    # Use [:-1] to drop newline
    first_elf_range, second_elf_range = map(lambda x: x.split("-"), line[:-1].split(","))
    
    # Range is endpoint exclusive, thus we need to + 1
    first_elf_set = set(range(int(first_elf_range[0]),int(first_elf_range[1]) + 1))
    second_elf_set = set(range(int(second_elf_range[0]),int(second_elf_range[1]) + 1))

    if first_elf_set.issubset(second_elf_set) or second_elf_set.issubset(first_elf_set):
        subset_count = subset_count + 1 

print(f"Total number of subsets: {subset_count}")
input("Press Enter to continue...")

overlap_count = 0
for line in open("./input/day4.txt"):
    first_elf_range, second_elf_range = map(lambda x: x.split("-"), line[:-1].split(","))

    # Range is endpoint exclusive, thus we need to + 1
    first_elf_set = set(range(int(first_elf_range[0]),int(first_elf_range[1]) + 1))
    second_elf_set = set(range(int(second_elf_range[0]),int(second_elf_range[1]) + 1))

    if len(first_elf_set.intersection(second_elf_set)) > 0:
        overlap_count = overlap_count+1

print(f"Total number of any overlaps: {overlap_count}")
input("Press Enter to continue...")