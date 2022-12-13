def debug_print(message):
  if True:
    print(message)

def compare_arrays(first, second):
  length_of_first = len(first)
  length_of_second = len(second)
  length = min(length_of_first, length_of_second)

  for position in range(0, length):
    first_item = first[position]
    second_item = second[position]

    debug_print(f'Compare {first_item} vs {second_item}')
  
    return compare_items(first_item, second_item)

def compare_items(first_item, second_item):
  if isinstance(first_item, list) and isinstance(second_item, list):
    return compare_arrays(first_item, second_item)
  elif isinstance(first_item, list):
    return compare_arrays(first_item, [second_item])
  elif isinstance(second_item, list):
    return compare_arrays([first_item], second_item) 
  elif first_item > second_item:
    debug_print('Right side is smaller, so inputs are not in the right order')
    return 0
  elif first_item < second_item:
    debug_print('Left side is smaller, so inputs are in the right order')
    return 1

  return -1

def compare_inputs(first_array, second_array):
  length_of_first = len(first_array)
  length_of_second = len(second_array)
  length = min(length_of_first, length_of_second)
  
  for position in range(0, length):
    first_item = first_array[position]
    second_item = second_array[position]

    debug_print(f'Compare {first_item} vs {second_item}')
  
    decision = compare_items(first_item, second_item)

    if decision == 1:
      return True
    elif decision == 0:
      return False
  
  if length_of_second <= length_of_first:
    debug_print('Right side ran out of items, so inputs are not in the right order')
    return False
  else:
    debug_print('Left side ran out of items, so inputs are in the right order')
    return True

input = ['[1,1,3,1,1]','[1,1,5,1,1]','','[[1],[2,3,4]]','[[1],4]','','[9]','[[8,7,6]]','','[[4,4],4,4]','[[4,4],4,4,4]','','[7,7,7,7]','[7,7,7]','','[]','[3]','','[[[]]]','[[]]','','[1,[2,[3,[4,[5,6,7]]]],8,9]','[1,[2,[3,[4,[5,6,0]]]],8,9]']
input.append('')
input.reverse()

score = 0

for round in range(1, int(len(input) / 3) + 1):
  first_array = eval(input.pop())
  second_array = eval(input.pop())
  input.pop()

  debug_print('----------------------------------')
  debug_print(f'Compare {first_array} vs {second_array}')
  
  if compare_inputs(first_array, second_array):
    score += round

print(score)
