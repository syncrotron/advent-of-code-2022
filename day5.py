# Samuel Horovatin, December 2022

def convert_header_line(line, num_of_stacks):
    edited_line = str(line).replace("] [", ",").replace("    [", "-,").replace("]    ", ",-").replace("[", "").replace("]", "")
    edited_line = edited_line.replace(" ", ",").replace(",,,", ",-,").replace(",,", ",").strip("\n")
    return edited_line

def make_move(move_str, stacks):
    moves =  [int(i) for i in str(move_str).strip('\n').split(' ') if i.isdigit()]
    moves = [moves[0], moves[1] - 1, moves[2] - 1]
    print(len(stacks))
    moved_stack = stacks[moves[1]][0:moves[0]]
    moved_stack.reverse()

    stacks[moves[2]] = moved_stack + stacks[moves[2]]
    stacks[moves[1]] = stacks[moves[1]][moves[0]:]
    return stacks

num_of_stacks = 0
raw_levels, corrected_levels, stacks = [], [], []
for line in open("./input/day5.txt", 'r'):
    if 'move' in line:
        corrected_levels = make_move(line, corrected_levels)
    elif ('[' in line) or (']' in line):
        raw_levels.append(line)
    elif not line == "\n":
        num_of_stacks = int(line.strip('\n').split('   ')[-1])
        for level in raw_levels:
            corrected_levels.append(convert_header_line(level, num_of_stacks).split(",")[0:num_of_stacks])
        
        # Transpose lists
        stacks = [list(i) for i in zip(*corrected_levels)]
        for i in range(0, len(stacks)):
            new_stack = []
            for crate in stacks[i]:
                if not crate == '-':
                    new_stack.append(crate)
            stacks[i] = new_stack

top_of_each_stack = []
for i in range(0,num_of_stacks):
    top_of_each_stack.append(stacks[i][0])

print(top_of_each_stack)
       


