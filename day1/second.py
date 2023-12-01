


import sys
import re

substring_list = {
  'one': '1',
  'two': '2',
  'three': '3',
  'four': '4',
  'five': '5',
  'six': '6',
  'seven': '7',
  'eight': '8',
  'nine': '9'
}

with open('input.txt', 'r') as f:
  list_of_numbers = []
  for line in f:
    l = line.rstrip('\n')
    list_idx_num = []
    for el in range(0, len(l)):
      if not l[el].isalpha():
        list_idx_num.append(el)

    list_idx_num_str = []
    # take into account that subtrings can appear more than once so we need to get all the indices
    for key in substring_list:
        indices_object = re.finditer(pattern=key, string=l)
        indices = [index.start() for index in indices_object]
        for idx in indices:
          list_idx_num_str.append((key, idx))
      
    print(list_idx_num)

    num1_idx = list_idx_num[0]
    num2_idx = list_idx_num[-1]
    num1 = l[num1_idx]
    num2 = l[num2_idx]

    if len(list_idx_num_str) != 0:
      list_ord_idx_num_str = sorted(list_idx_num_str, key=lambda x: x[1])
      print(list_ord_idx_num_str)
      if list_ord_idx_num_str[0][1] < num1_idx:
        num1 = substring_list[list_ord_idx_num_str[0][0]]
      if list_ord_idx_num_str[-1][1] > num2_idx:
        num2 = substring_list[list_ord_idx_num_str[-1][0]]

    complete_num = int(num1 + num2)
    print(complete_num)
    list_of_numbers.append(complete_num)
 
  print(list_of_numbers)
  sol = sum(list_of_numbers)
  print(sol)
  