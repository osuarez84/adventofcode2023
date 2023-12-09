



dict_maps = {}
with open('input.txt', 'r') as f:
  lines = f.readlines()
  list_of_instructions = lines[0].rstrip('\n')

  for i in range(2, len(lines)):
    key = lines[i].split('=')[0][:-1]
    print(key)
    left = lines[i].rstrip('\n').split('=')[1].split(',')[0][2:]
    right = lines[i].rstrip('\n').split('=')[1].split(',')[1][1:-1]
    print(left)
    print(right)
    dict_maps[key] = {
      'L': left,
      'R': right
    }
  print(dict_maps)

  next_node = 'AAA'
  idx = 0
  counter = 0
  while next_node != 'ZZZ':
    instruction = list_of_instructions[idx % len(list_of_instructions)]
    print(instruction)
    next_node = dict_maps[next_node][instruction]
    print(next_node)
    counter += 1
    idx += 1
  print(counter)

