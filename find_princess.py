#!/usr/bin/python

#displayPathtoPrincess(3, [["-","-","-",],["-","m","-",],["p","-","-",]])
def displayPathtoPrincess(n,grid):
  my_pos = []
  princess_pos =[]
  pos_diff = []

  for i in range(0, len(grid)):
    for j in range(0, len(grid[i])):

      #found myself
      if grid[i][j] == 'm':
        my_pos.append(i)
        my_pos.append(j)

      #found the princess
      if grid[i][j] == 'p':
        princess_pos.append(i)
        princess_pos.append(j)
  #print("------------------")

  pos_diff.append(my_pos[0] - princess_pos[0])
  pos_diff.append(my_pos[1] - princess_pos[1])

  #print(my_pos, " princess is: ", princess_pos, "pos_diff ", pos_diff)

  #print("------------------")
  #print("TO FIND THE PRINCESS YOU MUST MOVE:")
  
  if pos_diff[0] > 0:
    print("UP" * abs(pos_diff[0]))
  elif pos_diff[0] < 0:
    print("DOWN" * abs(pos_diff[0]))
  else:
    print("NOT A NUMBER")

  if pos_diff[1] > 0:
    print("LEFT" * abs(pos_diff[0]))
  elif pos_diff[1] < 0:
    print("RIGHT" * abs(pos_diff[0]))
  else:
    print("NOT A NUMBER")
    

  
displayPathtoPrincess(3, [["-","-","-",],["-","m","-",],["p","-","-",]])
