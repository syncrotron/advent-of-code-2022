# Samuel Horovatin, December 2022

visible_trees = 0
edge_trees = 0
middle_trees = 0
tree_grid = []
for line in open("./input/day8.txt", 'r'):
    line = line.rstrip('\n')
    tree_grid.append([int(x) for x in [*line]])

def column(matrix, i):
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