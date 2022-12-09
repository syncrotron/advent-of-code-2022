# Samuel Horovatin, December 2022

BUFFER_SIZE = 4
first_marker = 0
for line in open("./input/day6.txt", 'r'):
    for i in range(0, len(line)):
        max_i = min(i+BUFFER_SIZE, len(line))
        if len(set(line[i:max_i])) == BUFFER_SIZE:
             first_marker = i + BUFFER_SIZE
             break

print(f'First Start-Of-Packet Marker After {first_marker} Chars (4 char buffer)')
input("Press Enter to continue...") 

BUFFER_SIZE = 14
first_marker = 0
for line in open("./input/day6.txt", 'r'):
    for i in range(0, len(line)):
        max_i = min(i+BUFFER_SIZE, len(line))
        if len(set(line[i:max_i])) == BUFFER_SIZE:
             first_marker = i + BUFFER_SIZE
             break

print(f'First Start-Of-Packet Marker After {first_marker} Chars (14 char buffer)')