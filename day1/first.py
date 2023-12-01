# read every line of the file

import sys


with open('input.txt', 'r') as f:
  list_of_numbers = []
  for line in f:
    l = line.rstrip('\n')
    # iterate from left to right and get first number
    for el in range(0, len(l)):
      if not l[el].isalpha():
        num1 = l[el]
        break
    
    # iterate from right to left and get the first number
    for el in reversed(range(0, len(l))):
      if not l[el].isalpha():
        num2 = l[el]
        break

    complete_num = int(num1 + num2)
    list_of_numbers.append(complete_num)

  sol = sum(list_of_numbers)
  print(sol)