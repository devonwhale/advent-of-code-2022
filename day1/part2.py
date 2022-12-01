input = [1000,2000,3000,None,4000,None,5000,6000,None,7000,8000,9000,None,10000]

current_highest_calories = 0
current_calories = 0

calories_list = []

for i in input:
  if i is None:
    calories_list.append(current_calories)
    current_calories = 0
  else:
    current_calories = current_calories + i

calories_list.sort(reverse = True)
top_three = calories_list[0] + calories_list[1] + calories_list[2]

print(calories_list[0])

print(top_three)
