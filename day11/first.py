
import re

with open('input.txt', 'r') as f:
  lines = f.readlines()
  lines = [line.strip() for line in lines]
  print(lines)

  # check rows with no galaxies (index) and expand adding a new empty list in the next idx
  counter = 1
  expanded_lines = []
  for idx, l in enumerate(lines):
    expanded_lines.append(list(l))
    if '#' not in l:
      print(l, idx)
      expanded_lines.append(['.']*len(l))
  print(expanded_lines)

  # check columns with no galaxies (idx) and expand adding a new empty list in the next idx
  counter = 1
  list_idx_cols_without_galaxies = [str(i) for i in range(0, len(expanded_lines[0]))]
  print(list_idx_cols_without_galaxies)
  for l in expanded_lines:
    for idx, col in enumerate(l):
      if col == '#':
        print(idx)
        if str(idx) in list_idx_cols_without_galaxies:
          list_idx_cols_without_galaxies.remove(str(idx))
  
  print(list_idx_cols_without_galaxies)
  
  # make the expansion in the columns
  tmp_expanded_lines = expanded_lines.copy()
  for idy, l in enumerate(expanded_lines):
    # take into account that every append makes the list grow and the indexes change by 1
    index_offset = 0
    for idx in list_idx_cols_without_galaxies:
      tmp_expanded_lines[idy].insert(int(idx)+index_offset, '.')
      index_offset += 1


  # enumerate every galaxy in the new expanded list and get the coordinates
  counter = 1
  list_coordinates_all_galaxies = []
  for idy, l in enumerate(expanded_lines):
    for idx, col in enumerate(l):
      if col == '#':
        l[idx] = str(counter)
        counter += 1
        x, y = idx, idy
        list_coordinates_all_galaxies.append((x, y)) 


  # compute all distances between
  counter = 1
  sum_all_distances = 0
  for i in range(0, len(list_coordinates_all_galaxies)-1):
    for j in range(i+1, len(list_coordinates_all_galaxies)):
      x_dst = abs(list_coordinates_all_galaxies[i][0] - list_coordinates_all_galaxies[j][0])
      y_dst = abs(list_coordinates_all_galaxies[i][1] - list_coordinates_all_galaxies[j][1])
      dst = x_dst + y_dst
      counter += 1
      sum_all_distances += dst
  print(sum_all_distances)




