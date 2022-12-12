class Node:
  def __init__(self, coordinates, parent):
    self.coordinates = coordinates
    self.parent = parent
    
    self.total_node_cost = 0
    self.start_distance = 0

  def __str__(self):
    return f'Node at location {self.coordinates} with f value {self.total_node_cost}, g value {self.start_distance} and h value {self.heuristic}'

  def __repr__(self):
    return str(self)

  def __eq__(self, other):
    return self.coordinates == other.coordinates

  def get_path(self):
    if self.parent is None:
      return [self.coordinates]
    else:
      path = self.parent.get_path()
      path.append(self.coordinates)
      return path
    
def get_coordinates(grid, char):
  target_x = 0
  target_y = 0
  count_x = 0
  count_y = 0
  for row in grid:
    count_x = 0
    for column in row:
      if column == char:
        target_x = count_x
        target_y = count_y
        break
      count_x += 1
    count_y += 1

  return target_x, target_y

def get_viable_children(grid, coords, value):
  directions_to_assess = []
  if coords[1] > 0:
    directions_to_assess.append((0, -1)) # Up
  if coords[1] < len(grid) - 1:
    directions_to_assess.append((0, 1)) # Down
  if coords[0] > 0:
    directions_to_assess.append((-1, 0)) # Left
  if coords[0] < len(grid[0]) - 1:
    directions_to_assess.append((1, 0)) # Right
  
  if value == 'S':
    value = 'a'

  locations_to_explore = []
  
  for direction in directions_to_assess:
    new_x = coords[0] + direction[0]
    new_y = coords[1] + direction[1]
    potential_location = grid[new_y][new_x]
    if potential_location == 'E':
      potential_location = 'z'
    if potential_location == 'S':
      potential_location = 'a'
    if ord(potential_location) <= ord(value) + 1:
      locations_to_explore.append((new_x, new_y))

  return locations_to_explore

def sort_node_list(list):
  return sorted(list, key=lambda n: n.total_node_cost)

def find_path(grid):
  start_x, start_y = get_coordinates(grid, 'S')
  end_x, end_y = get_coordinates(grid, 'E')
  
  open_list = []
  closed_list = []
  
  start_node = Node((start_x, start_y), None)
  end_node = Node((end_x, end_y), None)
  
  open_list.append(start_node)
  
  while len(open_list) > 0:
    open_list = sort_node_list(open_list)
    lowest_cost_node = open_list.pop(0)
    closed_list.append(lowest_cost_node)
    
    coordinates = lowest_cost_node.coordinates
    lowest_cost_node_value = grid[coordinates[1]][coordinates[0]]
    
    if lowest_cost_node_value == 'E':
      return lowest_cost_node.start_distance
    else:
      children = get_viable_children(grid, coordinates, lowest_cost_node_value)
      
      for child in children:
        child_node = Node(child, lowest_cost_node)
        
        for existing_closed_list_node in closed_list:
          if child_node == existing_closed_list_node:
            break
        else:
          child_node.start_distance = lowest_cost_node.start_distance + 1
          child_node.total_node_cost = child_node.start_distance
  
          existing_index = 0
          already_present = False
          for existing_open_list_node in open_list:
            if child_node == existing_open_list_node:
              if child_node.start_distance > existing_open_list_node.start_distance:
                already_present = True
                break
              else:
                open_list.remove(existing_open_list_node)
          if not already_present:
            open_list.append(child_node)

input = ['Sabqponm', 'abcryxxl', 'accszExk', 'acctuvwj', 'abdefghi']

grid = []
for line in input:
  grid.append(list(line))

print(find_path(grid))
