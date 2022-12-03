input = ['vJrwpWtwJgWrhcsFMMfFFhFp','jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL','PmmdzqPrVvPwwTWBwg','wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn','ttgJtRGJQctTZtZT','CrZsJsPPZsGzwwsLwLmpwMDw']

score = 0

for backpack in input:
  pocket_a,pocket_b = backpack[:len(backpack)//2], backpack[len(backpack)//2:]
  common_item = set(pocket_a).intersection(pocket_b)
  unmodified_value = ord(list(common_item)[0])
  if 97 <= unmodified_value <= 122:
    score += unmodified_value - 96
  else:
    score += unmodified_value - 38

print(score)
