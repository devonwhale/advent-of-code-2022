input = [1000,2000,3000,None,4000,None,5000,6000,None,7000,8000,9000,None,10000]

current_highest_calories = 0
best_index = 1
current_calories = 0
index = 1

for i in input:
  if i is None:
    if current_calories > current_highest_calories:
      current_highest_calories = current_calories
      best_index = index
    index = index + 1
    current_calories = 0
  else:
    current_calories = current_calories + i

if current_calories > current_highest_calories:
  current_highest_calories = current_calories
  best_index = index

print(current_highest_calories)
