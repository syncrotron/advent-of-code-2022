# Samuel Horovatin, December 2022


num_fully_contained = 0
for line in open("./input/day4.txt"):
    # Use [:-1] to drop newline
    first_elf_range, second_elf_range = map(lambda x: x.split("-"), line[:-1].split(","))
    first_elf_set = set(range(int(first_elf_range[0]),int(first_elf_range[1]) + 1))
    second_elf_set = set(range(int(second_elf_range[0]),int(second_elf_range[1]) + 1))

    if first_elf_set.issubset(second_elf_set) or second_elf_set.issubset(first_elf_set):
        num_fully_contained = num_fully_contained + 1 

print(f"Total number of subsets: {num_fully_contained}")