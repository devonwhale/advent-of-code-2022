class Node:
  def __init__(self, name, parent, size):
    self.name = name
    self.parent = parent
    self.size = size
    self.children = []

  def calculate_size(self):
    if self.size != 0:
      return self.size
    size = 0
    for child in self.children:
      size += child.calculate_size()
    return size

  def add_child(self, child):    
    self.children.append(child)

  def get_parent(self):
    return self.parent

  def get_name(self):
    return self.name

  def get_child(self, child_name):
    for child in self.children:
      if child.get_name() == child_name:
        return child

  def is_dir(self):
    return True if self.size == 0 else False

  def calculate_dir_sizes(self):
    sizes = []
    for child in self.children:
      if child.is_dir():
        sizes += child.calculate_dir_sizes()
    if self.is_dir:
      sizes.append((self.name, self.calculate_size()))
    return sizes

input = ['$ cd /','$ ls','dir a','14848514 b.txt','8504156 c.dat','dir d','$ cd a','$ ls','dir e','29116 f','2557 g','62596 h.lst','$ cd e','$ ls','584 i','$ cd ..','$ cd ..','$ cd d','$ ls','4060174 j','8033020 d.log','5626152 d.ext','7214296 k']

starting_node = Node('/', None, 0)
current_node = starting_node

for line in input:
  split_line = line.split(' ')
  if line[0] == '$':
    if split_line[1] == 'cd':
      if split_line[2] == '/':
        current_node = starting_node
      elif split_line[2] == '..':
        current_node = current_node.get_parent()
      else:
        current_node = current_node.get_child(split_line[2])
  else:
    if split_line[0] == 'dir':
      new_dir = Node(split_line[1], current_node, 0)
      current_node.add_child(new_dir)
    else:
      new_file = Node(split_line[1], current_node, int(split_line[0]))
      current_node.add_child(new_file)

dir_sizes = starting_node.calculate_dir_sizes()
total_size = 0
for size in dir_sizes:
  if size[1] <= 100000:
    total_size += size[1]

print(total_size)
