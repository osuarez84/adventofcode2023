

import sys


list_of_possible_ids = []
dict_limits = {
  'red': 12,
  'green': 13,
  'blue': 14
}


# each line
# game_id
# list of  lists with set cubes with tuples (number_of_cubes, color)
#[1, [(1, 'red'), (1, 'blue'), (1, 'green'), (1, 'yellow')], [(1, 'red'), (1, 'blue'), (1, 'green'), (1, 'yellow')]]
with open('input.txt', 'r') as f:
  list_game_idx_impossible = []
  sum_ids_all_games = 0
  for line in f:
    l = line.rstrip('\n')
    # get the game id
    game_id = l.split(':')[0].split(' ')[1]
    sum_ids_all_games += int(game_id)
    
    # get list of color cubes for each game
    tmp = l.split(':')[1].split(';')
    print(tmp)
    list_of_color_cubes = [x.split(',') for x in tmp]
    print(list_of_color_cubes)
    list_sanitized_color_cubes = []
    for item in list_of_color_cubes:
      tmp_list_sanitized_color_cubes = [(x[1:].split(' ')[0], x[1:].split(' ')[1]) for x in item]
      for clean_item in tmp_list_sanitized_color_cubes:
        if int(clean_item[0]) > dict_limits[clean_item[1]]:
          if game_id not in list_game_idx_impossible:
            list_game_idx_impossible.append(game_id)

list_game_idx_impossible_int = [int(x) for x in list_game_idx_impossible]
sum_ids_impossible_games = sum(list_game_idx_impossible_int)

print(sum_ids_all_games)
print(sum_ids_impossible_games)

sol = sum_ids_all_games - sum_ids_impossible_games
print(sol)