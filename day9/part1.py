def move_tail(head_idx, tail_idx):
  if (rope[head_idx][0] == rope[tail_idx][0] and rope[head_idx][1] == rope[tail_idx][1]) or ((-2 < rope[head_idx][0] - rope[tail_idx][0] < 2) and (-2 < rope[head_idx][1] - rope[tail_idx][1] < 2)):
    pass
  elif rope[head_idx][0] == rope[tail_idx][0]:
    if rope[head_idx][1] > rope[tail_idx][1]:
      rope[tail_idx][1] += 1
    else:
      rope[tail_idx][1] -= 1
  elif rope[head_idx][1] == rope[tail_idx][1]:
    if rope[head_idx][0] > rope[tail_idx][0]:
      rope[tail_idx][0] += 1
    else:
      rope[tail_idx][0] -= 1
  elif -2 < rope[head_idx][0] - rope[tail_idx][0] < 2:
    if rope[head_idx][1] > rope[tail_idx][1]:
      rope[tail_idx][1] += 1
    else:
      rope[tail_idx][1] -= 1
    rope[tail_idx][0] = rope[head_idx][0]
  elif -2 < rope[head_idx][1] - rope[tail_idx][1] < 2:
    if rope[head_idx][0] > rope[tail_idx][0]:
      rope[tail_idx][0] += 1
    else:
      rope[tail_idx][0] -= 1
    rope[tail_idx][1] = rope[head_idx][1]
  tail_locations.append(rope[tail_idx].copy())

def positive_move(idx, number_of_steps):
  for step in range(0, number_of_steps):
    rope[0][idx] += 1
    move_tail(0, 1)

def negative_move(idx, number_of_steps):
  for step in range(0, number_of_steps):
    rope[0][idx] -= 1
    move_tail(0, 1)

input = ['R 4','U 4','L 3','D 1','R 4','D 1','L 5','R 2']

rope_length = 2
rope = []
for knot in range(0, 2):
  rope.append([0,0])

tail_locations = [rope[-1].copy()]

for instruction in input:
  parsed_instruction = instruction.split(' ')
  direction = parsed_instruction[0]
  number_of_steps = int(parsed_instruction[1])

  if direction == 'U':
    positive_move(1, number_of_steps)
  elif direction == 'R':
    positive_move(0, number_of_steps)
  elif direction == 'D':
    negative_move(1, number_of_steps)
  elif direction == 'L':
    negative_move(0, number_of_steps)

distinct_locations = set(tuple(c) for c in tail_locations)

print(len(distinct_locations))
