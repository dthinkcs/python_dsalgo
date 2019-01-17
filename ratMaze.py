
def printBoard(arr):
  for i in range(len(arr)):
    for j in range(len(arr)):
      print(arr[i][j], end=" ")
  print()


def possible_move(arr, path, x, y):
	return x != -1 and x != len(arr) and y != -1 and y != len(arr) and arr[x][y] == 1 and path[x][y] == 0

def goLeft(arr, path, curr_i, curr_j):
	if possible_move(arr, path, curr_i, curr_j - 1):
		solution(arr, path, curr_i, curr_j - 1) 


def goRight(arr, path, curr_i, curr_j):
	if possible_move(arr, path, curr_i, curr_j + 1):
		solution(arr, path, curr_i, curr_j + 1)


def goUp(arr, path, curr_i, curr_j):
	if possible_move(arr, path, curr_i - 1, curr_j ):
		solution(arr, path, curr_i - 1, curr_j)


def goDown(arr, path, curr_i, curr_j):
	if possible_move(arr, path, curr_i + 1, curr_j ):
		solution(arr, path, curr_i + 1, curr_j)


def solution(arr, path, curr_i, curr_j):
	path[curr_i][curr_j] = 1
	if curr_i == len(arr) - 1 and curr_j == len(arr) - 1:
		printBoard(path)
	else:
		# LRUD
		goLeft(arr, path, curr_i, curr_j);
		goRight(arr, path, curr_i, curr_j);
		goUp(arr, path, curr_i, curr_j);
		goDown(arr, path, curr_i, curr_j);

	path[curr_i][curr_j] = 0


n = int(input())

maze = []
for i in range(n):
	lt = list(map(int, input().split()))
	maze.append(lt)

path = []
for i in range(n):
	path.append([0] * n)


#printBoard(maze)
#printBoard(path)


solution(maze, path, 0, 0)
