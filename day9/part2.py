def does_not_require_move(head, tail):
  same_location = head[0] == tail[0] and head[1] == tail[1]
  
  up = head[0] == tail[0] and head[1] + 1 == tail[1]
  right = head[0] + 1 == tail[0] and head[1] == tail[1]
  down = head[0] == tail[0] and head[1] - 1 == tail[1]
  left = head[0] - 1 == tail[0] and head[1] == tail[1]
  
  up_left = head[0] - 1 == tail[0] and head[1] + 1 == tail[1]
  up_right = head[0] + 1 == tail[0] and head[1] + 1 == tail[1]
  down_right = head[0] + 1 == tail[0] and head[1] - 1 == tail[1]
  down_left = head[0] - 1 == tail[0] and head[1] - 1 == tail[1]
  
  return same_location or up or right or down or left or up_left or up_right or down_right or down_left

def tail_two_right_of_head(head, tail):
  return head[0] + 2 == tail[0] and head[1] == tail[1]
  
def tail_two_left_of_head(head, tail):
  return head[0] - 2 == tail[0] and head[1] == tail[1]
  
def tail_two_above_of_head(head, tail):
  return head[1] + 2 == tail[1] and head[0] == tail[0]
  
def tail_two_below_of_head(head, tail):
  return head[1] - 2 == tail[1] and head[0] == tail[0]

def move_on_same_axis(head, tail, axis):
  if head[axis] > tail[axis]:
    tail[axis] += 1
  else:
    tail[axis] -= 1

def above_and_left(head, tail):
  return head[0] > tail[0] and head[1] < tail[1]

def above_and_right(head, tail):
  return head[0] < tail[0] and head[1] < tail[1]

def below_and_right(head, tail):
  return head[0] < tail[0] and head[1] > tail[1]

def below_and_left(head, tail):
  return head[0] > tail[0] and head[1] > tail[1]

def move_tail(head_idx, tail_idx):
  head = rope[head_idx]
  tail = rope[tail_idx]
  if does_not_require_move(head, tail):
    pass
  elif tail_two_right_of_head(head, tail):
    tail[0] -= 1
  elif tail_two_left_of_head(head, tail):
    tail[0] += 1
  elif tail_two_above_of_head(head, tail):
    tail[1] -= 1
  elif tail_two_below_of_head(head, tail):
    tail[1] += 1
  elif above_and_left(head, tail):
    tail[0] += 1
    tail[1] -= 1
  elif above_and_right(head, tail):
    tail[0] -= 1
    tail[1] -= 1
  elif below_and_right(head, tail):
    tail[0] -= 1
    tail[1] += 1
  elif below_and_left(head, tail):
    tail[0] += 1
    tail[1] += 1
  else:
    print(f'This is impossible. {head}, {tail}')

  if tail_idx == rope_length - 1:
    tail_locations.append(tail.copy())
  else:
    move_tail(tail_idx, tail_idx + 1)

def positive_move(idx, number_of_steps):
  for step in range(0, number_of_steps):
    rope[0][idx] += 1
    move_tail(0, 1)

def negative_move(idx, number_of_steps):
  for step in range(0, number_of_steps):
    rope[0][idx] -= 1
    move_tail(0, 1)

input = ['R 5','U 8','L 8','D 3','R 17','D 10','L 25','U 20']

rope_length = 10
rope = []
for knot in range(0, rope_length):
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
