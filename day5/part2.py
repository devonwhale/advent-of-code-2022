input = ['    [D]    ','[N] [C]    ','[Z] [M] [P] ',' 1   2   3 ']

instructions = ['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1','move 1 from 1 to 2']

stack_values = range(0, int(input[-1][-2]))
stacks = []
for stack in stack_values:
  stacks.append([])

input.pop(-1)

for line in input:
  name_index = 1
  stack_index = 0
  for stack in stack_values:
    if line[name_index] != ' ':
      stacks[stack_index].append(line[name_index])
    name_index += 4
    stack_index += 1

for task in instructions:
  split_task = task.split(' ')
  number_to_move = range(0, int(split_task[1]))
  move_from = int(split_task[3]) - 1
  move_to = int(split_task[5]) - 1

  items_to_move = []
  for x in number_to_move:
    items_to_move.append(stacks[move_from].pop(0))

  for item in reversed(items_to_move):
    stacks[move_to].insert(0, item)

output = ''

for stack in stacks:
  output += stack[0]

print(output)
