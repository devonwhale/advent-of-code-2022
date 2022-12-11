import math

class Monkey:
  def __init__(self, number, items, operation, test, true_target, false_target):
    self.number = number
    self.items = items
    self.operation = operation
    self.test = test
    self.true_target = true_target
    self.false_target = false_target
    self.number_of_inspections = 0

  def __str__(self):
    return f'Monkey {self.number} has {self.items}'

  def get_items(self):
    return self.items

  def get_operation(self):
    return self.operation

  def get_test(self):
    return self.test
  
  def determine_target(self, value): 
    remainder = value % self.test
    if remainder:
      return self.false_target
    else:
      return self.true_target

  def add_item(self, item):
    self.items.append(item)

  def remove_item(self, item):
    self.items.remove(item)

  def inspect(self):
    self.number_of_inspections += 1

  def get_inspections(self):
    return self.number_of_inspections

def parse_item(item):
  item_value = item.split(',')[0]
  return int(item_value)

input = ['Monkey 0:','Starting items: 79, 98','Operation: new = old * 19','Test: divisible by 23','If true: throw to monkey 2','If false: throw to monkey 3','','Monkey 1:','Starting items: 54, 65, 75, 74','Operation: new = old + 6','Test: divisible by 19','If true: throw to monkey 2','If false: throw to monkey 0','','Monkey 2:','Starting items: 79, 60, 97','Operation: new = old * old','Test: divisible by 13','If true: throw to monkey 1','If false: throw to monkey 3','','Monkey 3:','Starting items: 74','Operation: new = old + 3','Test: divisible by 17','If true: throw to monkey 0','If false: throw to monkey 1']

number_of_monkeys = (len(input) + 1) / 7

input.append('')
iter_input = iter(input)

parsed_monkeys = []

for monkey in range(0, int(number_of_monkeys)):
  number = next(iter_input).split(' ')[-1].split(':')[0]
  items = list(map(parse_item, next(iter_input).split(' ')[2:]))
  operation = next(iter_input).split('=')[-1]
  test = int(next(iter_input).split(' ')[-1])
  true_target = int(next(iter_input).split(' ')[-1])
  false_target = int(next(iter_input).split(' ')[-1])
  next(iter_input)

  parsed_monkeys.append(Monkey(number, items, operation, test, true_target, false_target))

m_value = 1

for monkey in parsed_monkeys:
  m_value *= monkey.get_test()

for round in range(0, 10000):
  for monkey in parsed_monkeys:
    items_monkey_has = monkey.get_items().copy()
    for item in items_monkey_has:
      old = item
      altered_value = math.floor(eval(monkey.get_operation()))
      target_monkey = monkey.determine_target(altered_value)
      altered_value %= m_value
      monkey.remove_item(item)
      monkey.inspect()
      parsed_monkeys[target_monkey].add_item(altered_value)

inspections = []
for monkey in parsed_monkeys:
  inspections.append(monkey.get_inspections())

inspections.sort(reverse = True)
print(inspections[0] * inspections[1])
