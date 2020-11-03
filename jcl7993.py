import common

def astar_search(map):
	found = False
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# y between 0 and common.constants.MAP_HEIGHT-1
	# x between 0 and common.constants.MAP_WIDTH-1
	def f(fcurr):
		if fcurr == (6, 7) or fcurr == (5, 2):
			print("holup")
		h = abs(goal[0] - fcurr[0]) + abs(goal[1] - fcurr[1])
		g = 0
		while fcurr != start:
			fcurr = parent[fcurr[0]][fcurr[1]]
			g += 1
		return g + h

	start = None
	goal = None
	frontier = []
	parent = [[-1 for x in range(common.constants.MAP_WIDTH)] for y in range(common.constants.MAP_HEIGHT)]
	for x in range(common.constants.MAP_WIDTH):
		for y in range(common.constants.MAP_HEIGHT):
			if map[y][x] == 2:
				start = (y, x)
				map[y][x] = 4
			if map[y][x] == 3:
				goal = (y, x)
	frontier.append([start, f(start)])
	while len(frontier) != 0:
		node = frontier.pop(0)
		node = node[0]
		map[node[0]][node[1]] = 4
		if node != goal:
			children = [(node[0], node[1] - 1), (node[0] - 1, node[1]), (node[0] + 1, node[1]), (node[0], node[1] + 1)]
			for child in children:
				if 0 <= child[0] < common.constants.MAP_HEIGHT and 0 <= child[1] < common.constants.MAP_WIDTH and (
						map[child[0]][child[1]] == 0 or map[child[0]][child[1]] == 3):
					parent[child[0]][child[1]] = (node[0], node[1])
					frontier.append([child, f(child)])
			frontier.sort(key=lambda tup: (tup[1]))
		else:
			found = True
			break
	if found:
		curr = goal
		map[start[0]][start[1]] = 5
		while curr != start:
			map[curr[0]][curr[1]] = 5
			curr = parent[curr[0]][curr[1]]
	return found
