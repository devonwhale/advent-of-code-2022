def assess(height, others):
  score = 0
  for tree in others:
    score += 1
    if tree >= height:
      break
  return score

input = ['30373','25512','65332','33549','35390']

trees = []

for line in input:
  split_line = list(line)
  parsed_line = list(map(int, split_line))
  trees.append(parsed_line)

current_row = 0
current_column = 0
always_visible_rows = [0, len(trees) - 1]
always_visible_columns = [0, len(trees[0]) - 1]
visible_trees = 0
best_score = 0

for tree_row in trees:
  if current_row in always_visible_rows:
    visible_trees += len(tree_row)
  else:
    for tree in tree_row:
      if current_column in always_visible_columns:
        visible_trees += 1
      else:
        west_trees = tree_row[:current_column]
        east_trees = tree_row[current_column + 1:]
        north_trees = []
        south_trees = []
        
        other_rows_index = 0
        is_north = True
        
        for row in trees:
          if other_rows_index == current_row:
            is_north = False
          elif is_north:
            north_trees.append(row[current_column])
          else:
            south_trees.append(row[current_column])
          other_rows_index += 1

        trees_to_assess = [reversed(west_trees), east_trees, reversed(north_trees), south_trees]
        directional_scores = []

        for tree_set in trees_to_assess:
          directional_scores.append(assess(tree, tree_set))

        score = directional_scores[0] * directional_scores[1] * directional_scores[2] * directional_scores[3]

        if score > best_score:
          best_score = score
        
      current_column += 1
  current_row += 1
  current_column = 0

print(best_score)
