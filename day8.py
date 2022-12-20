# Samuel Horovatin, December 2022

from typing import List


visible_trees = 0
edge_trees = 0
middle_trees = 0
tree_grid = []
for line in open("./input/day8.txt", 'r'):
    line = line.rstrip('\n')
    tree_grid.append([int(x) for x in [*line]])

def column(matrix: List[List[int]], i: int) -> List[int]:
    return [row[i] for row in matrix]

for tree_row_i in range(0, len(tree_grid)):
    for tree_col_i in range(0, len(tree_grid[tree_row_i])):
        if tree_col_i == 0 or tree_row_i == 0 or tree_col_i == (len(tree_grid) - 1) or tree_row_i == (len(tree_grid[tree_col_i]) - 1):       
            edge_trees = edge_trees + 1
        else:
            selected_tree = tree_grid[tree_row_i][tree_col_i]
            top_trees = column(tree_grid, tree_col_i)[0:tree_row_i]
            bottom_trees = column(tree_grid, tree_col_i)[tree_row_i+1:len(tree_grid)]
            right_trees = tree_grid[tree_row_i][tree_col_i+1:len(tree_grid)]
            left_trees = tree_grid[tree_row_i][0:tree_col_i]
            if selected_tree > max(top_trees) or selected_tree > max(bottom_trees) or selected_tree > max(right_trees) or selected_tree > max(left_trees):
                middle_trees = middle_trees + 1
        
print("Edge Tree Count:", edge_trees)
print("Middle Tree Count:", middle_trees)
print(f"Visibile Trees: {edge_trees + middle_trees}")
input("Press Enter to continue...")


def tree_sight_count(position_height: int, sight_line_trees: List[int]) -> int:
    sight_count = 0
    for tree in sight_line_trees:
        if position_height > tree:
            sight_count = sight_count + 1
        else: 
            sight_count = sight_count + 1
            break

    return sight_count

best_scenic_score = 0
ideal_position = [0,0]
for tree_row_i in range(0, len(tree_grid)):
    for tree_col_i in range(0, len(tree_grid[tree_row_i])):
        selected_tree = tree_grid[tree_row_i][tree_col_i]
        top_trees = column(tree_grid, tree_col_i)[0:tree_row_i]
        top_trees.reverse()
        bottom_trees = column(tree_grid, tree_col_i)[tree_row_i+1:]
        right_trees = tree_grid[tree_row_i][tree_col_i+1:]
        left_trees = tree_grid[tree_row_i][0:tree_col_i]
        left_trees.reverse()

        selected_tree_scenic_score = tree_sight_count(selected_tree, top_trees) * tree_sight_count(selected_tree, bottom_trees) * tree_sight_count(selected_tree, right_trees) * tree_sight_count(selected_tree, left_trees)
        if selected_tree_scenic_score > best_scenic_score:
            best_scenic_score = selected_tree_scenic_score
            ideal_position = [tree_row_i+1, tree_col_i+1]
        # print(f"Position: {[tree_row_i+1, tree_col_i+1]}")
        # print(f"top_trees scene total {tree_sight_count(selected_tree, top_trees)}")
        # print(f"bottom_trees scene total {tree_sight_count(selected_tree, bottom_trees)}")
        # print(f"right_trees scene total {tree_sight_count(selected_tree, right_trees)}")
        # print(f"left_trees scene total {tree_sight_count(selected_tree, left_trees)}")
        # print()
        # print(f"selected_tree {selected_tree}")
        # print(f"top_trees {top_trees}")
        # print(f"bottom_trees {bottom_trees}")
        # print(f"right_trees {right_trees}")
        # print(f"left_trees {left_trees}")
        # print()
print(f"The Best Scenic Score Of ({best_scenic_score}) can be found at {ideal_position}")        
input("Press Enter to continue...")