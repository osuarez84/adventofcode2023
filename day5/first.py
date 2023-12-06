import sys
import re

with open('input.txt', 'r') as f:
  lines = f.readlines()
  seed_to_soil_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'seed-to-soil' in l]
  seed_to_soil_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'soil-to-fertilizer' in l]
  soil_to_fertilizer_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'soil-to-fertilizer' in l]
  soil_to_fertilizer_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'fertilizer-to-water' in l]
  fertilizer_to_water_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'fertilizer-to-water' in l]
  fertilizer_to_water_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'water-to-light' in l]
  water_to_light_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'water-to-light' in l]
  water_to_light_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'light-to-temperature' in l]
  light_to_temperature_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'light-to-temperature' in l]
  light_to_temperature_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'temperature-to-humidity' in l]
  temperature_to_humidity_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'temperature-to-humidity' in l]
  temperature_to_humidity_end = [(l.rstrip('\n'),idx-1) for idx, l in enumerate(lines) if 'humidity-to-location' in l]
  humidity_to_location_start = [(l.rstrip('\n'),idx+1) for idx, l in enumerate(lines) if 'humidity-to-location' in l]
  humidity_to_location_end = len(lines)

  dict_of_maps = {
    'seed_to_soil': lines[seed_to_soil_start[0][1]:seed_to_soil_end[0][1]],
    'soil_to_fertilizer': lines[soil_to_fertilizer_start[0][1]:soil_to_fertilizer_end[0][1]],
    'fertilizer_to_water': lines[fertilizer_to_water_start[0][1]:fertilizer_to_water_end[0][1]],
    'water_to_light': lines[water_to_light_start[0][1]:water_to_light_end[0][1]],
    'light_to_temperature': lines[light_to_temperature_start[0][1]:light_to_temperature_end[0][1]],
    'temperature_to_humidity': lines[temperature_to_humidity_start[0][1]:temperature_to_humidity_end[0][1]],
    'humidity_to_location': lines[humidity_to_location_start[0][1]:humidity_to_location_end]
  }

  # seed_to_soil = lines[seed_to_soil_start[0][1]:seed_to_soil_end[0][1]]
  # soil_to_fertilizer = lines[soil_to_fertilizer_start[0][1]:soil_to_fertilizer_end[0][1]]
  # fertilizer_to_water = lines[fertilizer_to_water_start[0][1]:fertilizer_to_water_end[0][1]]
  # water_to_light = lines[water_to_light_start[0][1]:water_to_light_end[0][1]]
  # light_to_temperature = lines[light_to_temperature_start[0][1]:light_to_temperature_end[0][1]]
  # temperature_to_humidity = lines[temperature_to_humidity_start[0][1]:temperature_to_humidity_end[0][1]]
  # humidity_to_location = lines[humidity_to_location_start[0][1]:humidity_to_location_end]

  list_all_dicts = []
  for k, v in dict_of_maps.items():
    final_dict = {}
    for el in range(0, len(v)):
      tmp_list_src = list(range(int(v[el].rstrip('\n').split(' ')[1]), int(v[el].rstrip('\n').split(' ')[1])+int(v[el].rstrip('\n').split(' ')[2])))
      tmp_list_dst = list(range(int(v[el].rstrip('\n').split(' ')[0]), int(v[el].rstrip('\n').split(' ')[0])+int(v[el].rstrip('\n').split(' ')[2])))
      tmp_dict = {k: v for (k, v) in zip(tmp_list_src, tmp_list_dst)}
      final_dict.update(tmp_dict)
    list_all_dicts.append(final_dict)

  # get initial seeds values
  seed_values = lines[0].rstrip('\n').split(':')[1].split(' ')[1:]

  # iterate over every seed value and every dictionary until the last one that contains the location
  chains_list = []
  for seed in seed_values:
    tmp = int(seed)
    tmp_list = []
    for m in list_all_dicts:
      if tmp in m.keys():
        value = m[tmp]
      else:
        value = tmp
      print(value)
      tmp = value
      tmp_list.append(value)
    chains_list.append(tmp_list)

  # get the final location for each seed
  final_loc_list = []
  for chain in chains_list:
    final_loc_list.append(chain[-1])
  
  # Get the lowers value
  lowerst_loc = min(final_loc_list)
  print(lowerst_loc)


# I am getting the correct answer from the toy example
# but the performance in the input is terrible because I store all the dictionaries in memory
# this is not neccesarry and should be improved

    