input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

length_of_block = 14

iterator = range(0, len(input) - (length_of_block - 1))

for i in iterator:
  block = input[i:i+length_of_block]
  unique_characters = list(set(block))
  if len(unique_characters) == length_of_block:
    print(i+length_of_block)
    break
