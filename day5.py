# Samuel Horovatin, December 2022
import re

# Takes a stack line and extracts 
def convert_header_line(line, num_of_stacks):
    regex = r'\[[A-Z]\]|    |   \n$' #Regex from Matthew B.
    edited_line = re.findall(regex, line)
    return [x.strip("[] \n") for x in edited_line]

def make_move(move_str, stacks):
    moves =  [int(i) for i in str(move_str).strip('\n').split(' ') if i.isdigit()]
    moves = [moves[0], moves[1] - 1, moves[2] - 1]
    moved_stack = stacks[moves[1]][0:moves[0]]
    moved_stack.reverse() # Needed for single crate pick up and put down

    stacks[moves[2]] = moved_stack + stacks[moves[2]]
    stacks[moves[1]] = stacks[moves[1]][moves[0]:]
    return stacks

num_of_stacks = 0
raw_levels, corrected_levels, stacks = [], [], []
for line in open("./input/day5.txt", 'r'):

    if 'move' in line:
        stacks = make_move(line, stacks)
    elif ('[' in line) or (']' in line):
        raw_levels.append(line)
    elif not line == "\n":
        # Must be final line of stack portion of file, indicating number of stacks
        num_of_stacks = int(line.strip('\n').split('   ')[-1])
        for level in raw_levels:
            corrected_levels.append(convert_header_line(level, num_of_stacks))

        # Transpose stacks order stack tops to be at front of list
        stacks = [list(i) for i in zip(*corrected_levels)]
        for i in range(0, len(stacks)):
            new_stack = []
            for crate in stacks[i]:
                if not crate == '':
                    new_stack.append(crate)
            stacks[i] = new_stack

# Extract top of stack solution string
top_of_each_stack = []
for i in range(0,num_of_stacks):
    top_of_each_stack.append(stacks[i][0])
print('Top of Stacks Strings:',''.join(top_of_each_stack))  