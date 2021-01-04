def getDistance(a,b):
  return abs(a[0] - b[0]) + abs(a[1] - b[1])	

def get_next_pos(maze, taxi_pos, man_pos, visited):
  min_distance = 1000
  min_cur = []
  next_list = [[1,0],[0,1],[-1,0],[0,-1]]

  for next in next_list:
    cur_pos = [taxi_pos[0] + next[0],taxi_pos[1] + next[1]]

    if cur_pos in visited :
      continue

    if maze[cur_pos[0]][cur_pos[1]] == 1 :
      continue

    cur_distance = getDistance(cur_pos, man_pos)

    if cur_distance < min_distance :
      min_distance = cur_distance
      min_cur = cur_pos

  visited.append(min_cur)
  return min_cur

def get_visited(maze, taxi_input, man_input):
  taxi_pos = taxi_input
  man_pos = man_input
  visited = []

  while taxi_pos != man_pos:
    taxi_pos = get_next_pos(maze, taxi_pos, man_pos, visited)

  print(visited)


if __name__ == "__main__":
  input_info = list(map(int, input().split()))
  maze_len = input_info[0] + 2
  maze = []

  for i in range(0, maze_len):
    maze_row = []
    if i == 0 or i == maze_len-1:
      for j in range(0, maze_len):
        maze_row.append(1)
      maze.append(maze_row)
      continue

    maze_data = list(map(int, input().split()))
    maze_row.append(1)
    maze.append(maze_row + maze_data + maze_row)

  for el in maze :
    print(el)

  taxi_input = [6,5]
  taxi_oil = 15
  man_input = [2,2]

  get_visited(maze,taxi_input,man_input)

