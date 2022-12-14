# Samuel Horovatin, December 2022
from dataclasses import dataclass, field
from typing import List

@dataclass
class Node:
    name: str
    size: int
    parent: 'Node' = None
    children: List['Node'] = field(default_factory=list) 
    
    def print_node(self):
        print(f'Name: {self.name}, Size: {self.size}, Parent: {None if self.parent is None else self.parent.name}, # Children: {len(self.children) if self.children is not None else None}')

def find_child(child_name: str, curr_node: Node):
    for child in curr_node.children:
        if child.name == child_name:
            return child
    return curr_node

def find_root(node: Node):
    while not node.name == '/':
        node = node.parent
    return node

def cd(cd_dir: str, curr_node: Node):
    next_node = curr_node 
    if cd_dir == '..' and not curr_node.name == '/':
        next_node = curr_node.parent
    elif cd_dir == '/':
        next_node = find_root(next_node)
    elif not curr_node.children == None:
        next_node = find_child(cd_dir, curr_node)
    return next_node

def update_all_sizes(curr_node: Node):
    if curr_node.children is None:
        return curr_node, curr_node.size
    else:
        for child in curr_node.children:

            child, children_size = update_all_sizes(child)
            curr_node.size = curr_node.size + children_size
        return curr_node, curr_node.size

def find_size_total_below_thresh(curr_node: Node, total: int, thresh: int):
    if curr_node.children is None:
        return total
    else:
        total = total + (curr_node.size if curr_node.size <= thresh else 0)
        for child in curr_node.children:
            total = find_size_total_below_thresh(child, total, thresh)
        return total

MAX_DIR_SIZE = 100000
CD_CMD_LEN = len('$ cd ')
curr_node = Node('/', 0, None)
file_nodes, dir_nodes = [], []
for line in open("./input/day7.txt", 'r'):
    line = line.rstrip('\n') # Removes pesky newline
    if '$ cd ' in line:
        cd_dir = line[CD_CMD_LEN:]
        curr_node = cd(cd_dir, curr_node) 
    elif not '$ ls' in line:
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


root_node, root_size = update_all_sizes(find_root(curr_node))

print(f"Sum of dirs smaller than {MAX_DIR_SIZE}: {find_size_total_below_thresh(root_node, 0, MAX_DIR_SIZE)}")
input("Press Enter to continue...") 

def find_sizes_above_thresh(curr_node: Node, dir_size_list: List[int], thresh: int):
    if curr_node.children is None:
        return dir_size_list
    else:
        if curr_node.size >= thresh:
            dir_size_list.append(curr_node.size)
        for child in curr_node.children:
            dir_size_list = find_sizes_above_thresh(child, dir_size_list, thresh)
        return dir_size_list

SYS_SIZE = 70000000
SIZE_REQUIRED = 30000000
min_size = min(find_sizes_above_thresh(root_node, [], SIZE_REQUIRED - (SYS_SIZE - root_node.size)))
print(f"Smallest folder size to be deleted: {min_size}")
input("Press Enter to continue...") 

