## Read input as specified in the question.
## Print output as specified in the question
# GIVEN I AND J add x's to the array
from copy import deepcopy

def add_x(arr, I, J):
  x = 9;
  # go horizontal
  for idx in range(len(arr)):
    # fix I
    if (idx != J):
        arr[I][idx] = x
        
        
  # go vertical 
  for idx in range(len(arr)):
    # fix I
    if (idx != I):
        arr[idx][J] = x
  
  # go diagonal1
  i = I
  j = J
  while True:
    if i - 1 == -1 or j - 1 == -1:
      break
    else:
      arr[i - 1][j - 1] = x     
    i -= 1
    j -= 1
  i = I
  j = J
  while True:
    if i + 1 == len(arr) or j + 1 == len(arr):
      break
    else:
      arr[i + 1][j + 1] = x     
    i += 1
    j += 1
    
  # go diagonal2
  i = I
  j = J
  while True:
    if i - 1 == -1 or j + 1 == len(arr):
      break
    else:
      arr[i - 1][j + 1] = x     
    i -= 1
    j += 1
  i = I
  j = J
  while True:
    if i + 1 == len(arr) or j - 1 == -1:
      break
    else:
      arr[i + 1][j - 1] = x     
    i += 1
    j -= 1

  

n = int(input())

arr = []

for i in range(n):
    arr.append([0] * n)


arr[1][2] = 1
add_x(deepcopy(arr), 1, 2)

for i in range(n):
  for j in range(n):
    print(arr[i][j], end="")
  print()
