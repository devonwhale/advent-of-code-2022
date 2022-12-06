input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

iterator = range(0, len(input) - 3)

for i in iterator:
  block = input[i:i+4]
  unique_characters = list(set(block))
  if len(unique_characters) == 4:
    print(i+4)
    break
