# Samuel Horovatin, December 2022
from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    name: str
    size: int
    parent: 'Node'
    children: List['Node'] = field(default_factory=list) 

def find_child(child_name: str, curr_node: Node):
    for child in curr_node.children:
        if child.name == child_name:
            return child
    return curr_node

def cd(cd_dir: str, curr_node: Node, root_node: Node):
    next_node = curr_node 
    if cd_dir == '..' and not curr_node.name == '/':
        next_node = curr_node.parent
    elif cd_dir == '/':
        next_node = root_node
    elif not curr_node.children == None:
        next_node = find_child(cd_dir, curr_node)
    return next_node

def update_parents_size(curr_node: Node, old_size: int, new_size: int):
    if not curr_node.parent == None:
        next_old_size = curr_node.size
        curr_node.size = curr_node.size - old_size + new_size
        update_parents_size(curr_node.parent, next_old_size, curr_node.size)
    else:
        return curr_node

MAX_DIR_SIZE = 100000
CD_CMD_LEN = len('$ cd ')
root_node = Node('/', 0, None)
curr_node = root_node
file_nodes, dir_nodes = [], []
for line in open("./input/day7.txt", 'r'):
    line = line.rstrip('\n') # Removes pesky newline
    print(line)
    if '$ cd ' in line:
        cd_dir = line[CD_CMD_LEN:]
        curr_node = cd(cd_dir, curr_node, root_node) 
    elif not 'ls' in line:
        cmd_parts = line.split(' ')
        # Stops duplicate children
        if not cmd_parts[0] in curr_node.children:
            
            if cmd_parts[0] == 'dir': 
                curr_node.children.append(Node(cmd_parts[1], 0, curr_node))
                dir_nodes.add((cmd_parts[1], 0))
            else:
                new_file_node = Node(cmd_parts[1], int(cmd_parts[0]), curr_node, None)
                curr_node.children.append(new_file_node)
                file_nodes.append(new_file_node)
