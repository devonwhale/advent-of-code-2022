input = ['A Y',
'B X',
'C Z']

winning_hands = ['A Y', 'B Z', 'C X']
drawing_hands = ['A X', 'B Y', 'C Z']

score = 0

for item in input:
  player_move = item[-1]
  if (player_move == 'X'):
    score = score + 1
  elif (player_move == 'Y'):
    score = score + 2
  elif (player_move == 'Z'):
    score = score + 3

  if item in winning_hands:
    score = score + 6
  if item in drawing_hands:
    score = score + 3

print(score)
