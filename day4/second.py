import sys




with open('input.txt', 'r') as f:
  total_value = 0
  lines = f.readlines()
  # set dictionary to init scratchcards based on the number of cards in the input
  dict_init_scratchcards_by_id = {str(i): 1 for i in range(1, len(lines)+1)}

  for line in lines:
    l = line.rstrip('\n')
    tmp = l.split(':')[1]
    card_id = l.split(':')[0].split(' ')[-1]
    print(card_id)
    tmp_wining_numbers = tmp.split('|')[0]
    tmp_my_numbers = tmp.split('|')[1]

    wining_numbers = tmp_wining_numbers.split(' ')
    my_numbers = tmp_my_numbers.split(' ')

    clean_wining_numbers = [x for x in wining_numbers if x != '']
    clean_my_numbers = [x for x in my_numbers if x != '']
    matches = list(set(clean_wining_numbers) & set(clean_my_numbers))
    print(len(matches))

    final_range = int(card_id)+len(matches)+1

    # spcial case if sum of current card id and number of matches is greater than the number of remaining cards in the input
    if int(card_id)+len(matches) > len(lines):
      final_range = len(lines) - int(card_id) + 1

    # repite the process for a number of times the value in the current card
    for cards in range(dict_init_scratchcards_by_id[str(card_id)]):
      for i in range(int(card_id)+1, final_range):
        dict_init_scratchcards_by_id[str(i)] += 1
    print(dict_init_scratchcards_by_id)
    # sys.exit()

  # get the total number of scratchcards
  total_value = 0
  for key, val in dict_init_scratchcards_by_id.items():
    total_value += val
  print(total_value)

