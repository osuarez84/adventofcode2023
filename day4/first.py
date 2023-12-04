# iterate over every card we have

# get the winning numbers in the card in a list

# get the numbers I have in another list

# check how many numbers I have in the winning numbers list
# multiply this total by 2

import sys


with open('input.txt', 'r') as f:
  total_value = 0
  lines = f.readlines()
  for line in lines:
    card_value = 0
    l = line.rstrip('\n')
    tmp = l.split(':')[1]
    tmp_wining_numbers = tmp.split('|')[0]
    tmp_my_numbers = tmp.split('|')[1]
    print(tmp_wining_numbers)
    print(tmp_my_numbers)

    wining_numbers = tmp_wining_numbers.split(' ')
    my_numbers = tmp_my_numbers.split(' ')
    print(wining_numbers)
    print(my_numbers)

    clean_wining_numbers = [x for x in wining_numbers if x != '']
    clean_my_numbers = [x for x in my_numbers if x != '']
    print(clean_wining_numbers)
    print(clean_my_numbers)
    matches = list(set(clean_wining_numbers) & set(clean_my_numbers))
    print(matches)
    if len(matches) == 1:
      card_value = 1
    elif len(matches) > 1:
      card_value = 2**(len(matches)-1)
    total_value += card_value
    print(card_value)
  
  print(total_value)