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

def depthfirst(curr_node: Node, size_dict: dict()):
    
    if curr_node.children == None:
        return size_dict, curr_node.size
    else:
        for child in curr_node.children:
           size_dict, children_size = depthfirst(child, size_dict)
           curr_node.size = curr_node.size + children_size
        size_dict[curr_node.name] = curr_node.size
        return size_dict, curr_node.size

MAX_DIR_SIZE = 100000
CD_CMD_LEN = len('$ cd ')
root_node = Node('/', 0, None)
curr_node = root_node
file_nodes, dir_nodes = [], []
for line in open("./input/day7.txt", 'r'):
    line = line.rstrip('\n') # Removes pesky newline
    if '$ cd ' in line:
        cd_dir = line[CD_CMD_LEN:]
        curr_node = cd(cd_dir, curr_node, root_node) 
    elif not 'ls' in line:
        cmd_parts = line.split(' ')
        # Stops duplicate children
        if not cmd_parts[0] in curr_node.children:
            
            if cmd_parts[0] == 'dir': 
                curr_node.children.append(Node(cmd_parts[1], 0, curr_node))
                dir_nodes.append((cmd_parts[1], 0))
            else:
                new_file_node = Node(cmd_parts[1], int(cmd_parts[0]), curr_node, None)
                curr_node.children.append(new_file_node)
                file_nodes.append(new_file_node)

root_node = curr_node
folder_size_dict = dict()
size_dict, root_size = depthfirst(root_node, folder_size_dict)

dir_sum = 0
for dir in folder_size_dict:
    if folder_size_dict[dir] <= MAX_DIR_SIZE:
        dir_sum = dir_sum + folder_size_dict[dir]
