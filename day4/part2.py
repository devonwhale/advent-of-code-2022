input = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8']

count = 0

for pair in input:
  split_pair = pair.split(',')
  split_first = split_pair[0].split('-')
  split_second = split_pair[1].split('-')
  first_lower = int(split_first[0])
  first_upper = int(split_first[1])
  second_lower = int(split_second[0])
  second_upper = int(split_second[1])
  if first_lower <= second_lower <= first_upper or first_lower <= second_upper <= first_upper:
    count += 1
  elif second_lower <= first_lower <= second_upper or second_lower <= first_upper <= second_upper:
    count += 1

print(count)
