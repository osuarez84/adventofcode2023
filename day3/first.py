

# wiht a regular expression we can get all the coordenates of each digit of the number:
# ([(3,0),(4,0),(5,0)], '257')
# ([(12,2),(13,2)], '67'])

# (x,y) pairs to compute the adjacent values
# [(1,0), (-1,0), (0,-1), (0, 1), (1,1), (1,-1), (-1,1), (-1,-1)]


import re
import sys

list_adj_coords = [(1,0), (-1,0), (0,-1), (0, 1), (1,1), (1,-1), (-1,1), (-1,-1)] # right, leaft, down, up, diag right down, diag right up, diag left down, diag left up

# Coordinates in the matrix goes like this:
# x = 0, y = 0 is the top left corner
# x = 0, y = 1 is the next line
# x = 1, y = 0 is the next column
# so increasing y means going down

with open('input.txt', 'r') as f:
  lines = f.readlines()
  list_puzzle_parts = []
  y = 0
  for line in lines:
    print(line)
    indices_object = re.finditer(r'(\d+)', line)

    indices = [(m.start(0), m.end(0)) for m in indices_object]

    for num_idx in indices:
      for x in range(num_idx[0], num_idx[1]):
        num_coords = (x,y)
        print(line[x])
        print(x, y)
        
        for adj in list_adj_coords:
          char = ''
          next_coord = (num_coords[0] + adj[0], num_coords[1] + adj[1])
          if (0 <= next_coord[0] < len(line[0])) & (0 <= next_coord[1] < len(lines)): # check if the next coordinate is inside the matrix
            char = lines[next_coord[0]][next_coord[1]]
            print(char)

          if (char != '.') | (not char.isdigit()) | (char == ''):
            complete_num = line[num_idx[0]:num_idx[1]]
            list_puzzle_parts.append(complete_num)
            break
        
    print(list_puzzle_parts)
    y += 1
    sys.exit(1)

