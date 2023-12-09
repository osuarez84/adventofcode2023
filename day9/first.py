

with open('input.txt', 'r') as f:
  lines = f.readlines()
  list_all_next_values = []
  for l in lines:
    serie_list = l.rstrip('\n').split(' ')
    serie_list = [int(i) for i in serie_list]
    print(serie_list)
    list_of_diff_lists = []
    tmp_list = serie_list
    while set(tmp_list) != {0}:
      tmp = []
      for i in range(1, len(tmp_list)):
        tmp.append(tmp_list[i] - tmp_list[i-1])
      list_of_diff_lists.append(tmp)
      tmp_list = tmp
    print(list_of_diff_lists)
    
    # reverse list_of_diff_lists to calculate and append the next element
    print(len(list_of_diff_lists))
    for i in range(len(list_of_diff_lists)-1, 0, -1):
      print(list_of_diff_lists[i])
      print(f'Sum: {list_of_diff_lists[i][-1] + list_of_diff_lists[i-1][-1]}')
      tmp_diff = list_of_diff_lists[i][-1] + list_of_diff_lists[i-1][-1]
      list_of_diff_lists[i-1].append(tmp_diff)
      print(f'New list with appended {list_of_diff_lists[i-1]}')
    next_value = serie_list[-1] + tmp_diff
    list_all_next_values.append(next_value)
    print(list_all_next_values)
    print(f'Next value: {next_value}')
  
  sum = 0
  for el in list_all_next_values:
    sum += el
  print(f'Solution: {sum}')