input = ['A Y',
'B X',
'C Z']

rock = 1
paper = 2
scissors = 3
draw = 3
win = 6

outcomes = {
  'A X': scissors,
  'A Y': rock + draw,
  'A Z': paper + win,
  'B X': rock,
  'B Y': paper + draw,
  'B Z': scissors + win,
  'C X': paper,
  'C Y': scissors + draw,
  'C Z': rock + win
}

score = 0

for item in input:
  score = score + outcomes[item]

print(score)
