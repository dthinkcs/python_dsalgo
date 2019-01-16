## Read input as specified in the question.
## Print output as specified in the question
# GIVEN I AND J add x's to the array

def printBoardLinear(arr):
  for i in range(n):
    for j in range(n):
      print(arr[i][j], end=" ")

  print()


def printBoard(arr):
  for i in range(n):
    for j in range(n):
      print(arr[i][j], end="")
    print()


def possiblePlacement(arr, I, J):
  #x = 1;
  # go horizontal
  for idx in range(len(arr)):
    # fix I
    if (idx != J):
        if arr[I][idx] == 1:
          return False
        
        
  # go vertical 
  for idx in range(len(arr)):
    # fix I
    if (idx != I):
        if arr[idx][J]:
          return False
  
  # go diagonal1
  i = I
  j = J
  while True:
    if i - 1 == -1 or j - 1 == -1:
      break
    else:
      if arr[i - 1][j - 1] == 1: 
        return False
    i -= 1
    j -= 1

  i = I
  j = J
  while True:
    if i + 1 == len(arr) or j + 1 == len(arr):
      break
    else:
      if arr[i + 1][j + 1] == 1:
        return False
    i += 1
    j += 1
    
  # go diagonal2
  i = I
  j = J
  while True:
    if i - 1 == -1 or j + 1 == len(arr):
      break
    else:
      if arr[i - 1][j + 1] == 1:
        return False    
    i -= 1
    j += 1

  i = I
  j = J
  while True:
    if i + 1 == len(arr) or j - 1 == -1:
      break
    else:
      if arr[i + 1][j - 1] == 1:
        return False 
    i += 1
    j -= 1

  return True
  # end of funtion

def solutions(arr, I):
  # place it at I, j
  for j in range(len(arr)):
    if possiblePlacement(arr, I, j):
      arr[I][j] = 1
      if I == len(arr) - 1:
        printBoardLinear(arr) # print it; dont go forward; set current thing to be 0 so that you can test other solutions 
        arr[I][j] = 0
      else:
        # call solutions
        solutions(arr, I + 1)
        # once you come back set 
        arr[I][j] = 0




  

n = int(input())

arr = []

for i in range(n):
    arr.append([0] * n)

# printBoard(arr)
# print(possiblePlacement(arr, 1, 2))
# arr[1][2] = 1
# printBoard(arr)
# print(possiblePlacement(arr, 1, 2)) # EDGE CASE PLACING OVER EXISTING CHESS PIECE decison!!!
# print(possiblePlacement(arr, 1, 1))

solutions(arr, 0)
