


import sys

with open('input.txt', 'r') as f:
  lines = f.readlines()
  time_list_tmp = lines[0].split(':')[1].rstrip('\n').split(' ')[1:]
  time_list = [int(el) for el in time_list_tmp if el != '']
  print(time_list)

  distance_list_tmp = lines[1].split(':')[1].rstrip('\n').split(' ')[1:]
  distance_list = [int(el) for el in distance_list_tmp if el != '']
  print(distance_list)

  list_counts = []
  for time, distance in zip(time_list, distance_list):
    count = 0
    for i in range(0, time+1):
      velocity = i * 1 # 1mm per milisecond
      time_travelling = time - i
      distance_travelling = velocity * time_travelling
      print(distance_travelling)
      if distance_travelling > distance:
        count += 1
    list_counts.append(count)

print(list_counts)
sol = 1
for el in list_counts:
  sol *= el

print(sol)
