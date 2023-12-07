



with open('test.txt', 'r') as f:
  lines = f.readlines()
  list_of_hands = []
  for idx, l in enumerate(lines):
    print(l, idx)
    tmp = l.rstrip('\n')

    # get the different chars in the hand
    diff_chars = set(tmp.split(' ')[0])
    print(diff_chars)
    list_counts = []
    for c in diff_chars:
      count = tmp.split(' ')[0].count(c)
      print(count, c)
      list_counts.append(count)
    print(list_counts)

    # label each hand by its type
    if len(diff_chars) == 1:
      hand_type = 'fiveofakind'
    elif len(diff_chars) == 2:
      if set(list_counts) == set([4, 1]):
        hand_type = 'fourofakind'
      elif set(list_counts) == set([3, 2]):
        hand_type = 'fullhouse'
    elif len(diff_chars) == 3:
      if set(list_counts) == set([3, 1, 1]):
        hand_type = 'threeofakind'
      elif set(list_counts) == set([2, 2, 1]):
        hand_type = 'twopairs'
    elif len(diff_chars) == 4:
      hand_type = 'onepair'
    elif (diff_chars) == 5:
      hand_type = 'highcard'
  
    hand_bid = (tmp.split(' ')[0], tmp.split(' ')[1], hand_type)
    list_of_hands.append(hand_bid)
  print(list_of_hands)



