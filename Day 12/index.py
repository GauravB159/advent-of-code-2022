def print_terrain(terrain, visited):
    for i, row in enumerate(terrain):
        for j, cell in enumerate(row):
            if((i,j) in visited):
                print(f"\033[31m{cell}\033[39m", end='')
            else:
                print(cell, end='')
        print()
    print()

from IPython.display import clear_output
import time 

def bfs(terrain, location, target, input):
    queue = [(location, 0, terrain[location[0]][location[1]])]
    visited = []
    count = 0
    while(len(queue) > 0):
        clear_output(wait=True)
        print_terrain(input, visited)
        time.sleep(0.001)
        count += 1
        if(count > 1000000): break
        current = queue.pop(0)
        depth = current[1]
        character = current[2]
        current = current[0]
        if(current in visited): continue
        if(terrain[current[0]][current[1]] == target): return (current, depth, character)
        if(current[0] < len(terrain) - 1 and (terrain[current[0] + 1][current[1]] - terrain[current[0]][current[1]]) <= 1):
            queue.append(((current[0] + 1, current[1]), depth + 1, terrain[current[0] + 1][current[1]]))
        if(current[0] > 0 and (terrain[current[0] - 1][current[1]] - terrain[current[0]][current[1]]) <= 1):
            queue.append(((current[0] - 1, current[1]), depth + 1, terrain[current[0] - 1][current[1]]))
        if(current[1] < len(terrain[0]) - 1 and (terrain[current[0]][current[1] + 1] - terrain[current[0]][current[1]]) <= 1):
            queue.append(((current[0], current[1] + 1), depth + 1, terrain[current[0]][current[1] + 1]))
        if(current[1] > 0 and (terrain[current[0]][current[1] - 1] - terrain[current[0]][current[1]]) <= 1):
            queue.append(((current[0], current[1] - 1), depth + 1, terrain[current[0]][current[1] - 1]))
        visited.append(current)
    print(count)