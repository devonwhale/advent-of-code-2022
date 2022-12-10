def get_cycle_strength(cycle, strength, X):
  if cycle in [20, 60, 100, 140, 180, 220]:
    strength += cycle * X
  return strength

def update_screen(X, cycle, screen):
  line_to_update = 0
  position_in_line = cycle
  if cycle <= 40:
    pass
  elif cycle <= 80:
    line_to_update = 1
    position_in_line = cycle - 40
  elif cycle <= 120:
    line_to_update = 2
    position_in_line = cycle - 80
  elif cycle <= 160:
    line_to_update = 3
    position_in_line = cycle - 120
  elif cycle <= 200:
    line_to_update = 4
    position_in_line = cycle - 160
  elif cycle <= 240:
    line_to_update = 5
    position_in_line = cycle - 200

  position_in_line -= 1

  character_to_render = '.'
  if X - 1 <= position_in_line <= X + 1:
    character_to_render = '#'
  
  screen[line_to_update].append(character_to_render)
  
  return screen

input = ['addx 15','addx -11','addx 6','addx -3','addx 5','addx -1','addx -8','addx 13','addx 4','noop','addx -1','addx 5','addx -1','addx 5','addx -1','addx 5','addx -1','addx 5','addx -1','addx -35','addx 1','addx 24','addx -19','addx 1','addx 16','addx -11','noop','noop','addx 21','addx -15','noop','noop','addx -3','addx 9','addx 1','addx -3','addx 8','addx 1','addx 5','noop','noop','noop','noop','noop','addx -36','noop','addx 1','addx 7','noop','noop','noop','addx 2','addx 6','noop','noop','noop','noop','noop','addx 1','noop','noop','addx 7','addx 1','noop','addx -13','addx 13','addx 7','noop','addx 1','addx -33','noop','noop','noop','addx 2','noop','noop','noop','addx 8','noop','addx -1','addx 2','addx 1','noop','addx 17','addx -9','addx 1','addx 1','addx -3','addx 11','noop','noop','addx 1','noop','addx 1','noop','noop','addx -13','addx -19','addx 1','addx 3','addx 26','addx -30','addx 12','addx -1','addx 3','addx 1','noop','noop','noop','addx -9','addx 18','addx 1','addx 2','noop','noop','addx 9','noop','noop','noop','addx -1','addx 2','addx -37','addx 1','addx 3','noop','addx 15','addx -21','addx 22','addx -6','addx 1','noop','addx 2','addx 1','noop','addx -10','noop','noop','addx 20','addx 1','addx 2','addx 2','addx -6','addx -11','noop','noop','noop']

X = 1
cycle = 0
strength = 0
output = [[],[],[],[],[],[]]

for instruction in input:
  parsed_instruction = instruction.split(' ')
  if parsed_instruction[0] == 'noop':
    cycle += 1
    strength = get_cycle_strength(cycle, strength, X)
    output = update_screen(X, cycle, output)
  elif parsed_instruction[0] == 'addx':
    for i in range(0, 2):
      cycle += 1
      strength = get_cycle_strength(cycle, strength, X)
      output = update_screen(X, cycle, output)
    X += int(parsed_instruction[1])

for line in output:
  concat_line = ''
  for char in line:
    concat_line += char
  print(concat_line)
