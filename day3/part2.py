input = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

score = 0
member_number = 1

for backpack in input:
  if member_number == 1:
    member_1 = backpack
    member_number = 2
  elif member_number == 2:
    member_2 = backpack
    member_number = 3
  elif member_number == 3:
    common_item = set(member_1) & set(member_2) & set(backpack)
    unmodified_value = ord(list(common_item)[0])
    if 97 <= unmodified_value <= 122:
      score += unmodified_value - 96
    else:
      score += unmodified_value - 38
    member_number = 1

print(score)
