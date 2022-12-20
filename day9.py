# Samuel Horovatin, December 2022
from typing import Tuple

def print_mov(move: str) -> None:
    print(f"== {move} ==")

def mov_head(head_position: Tuple[int, int], move: str) -> Tuple[int, int]:
    new_head_position = head_position
    if move[0] == 'U':
        new_head_position = (head_position[0], head_position[0]+int(move[2:]))
    elif move[0] == 'D':
        new_head_position = (head_position[0], head_position[0]-int(move[2:]))
    elif move[0] == 'L':
        new_head_position = (head_position[0]-int(move[2:]), head_position[0])
    elif move[0] == 'R':
        new_head_position = (head_position[0]+int(move[2:]), head_position[0])
    return new_head_position

head_position, tail_position = (0,0), (0,0)
tail_visited_list = []
for move in open("./input/day9.txt", "r"):
    move = move.rstrip('\n')
    print_mov(move)