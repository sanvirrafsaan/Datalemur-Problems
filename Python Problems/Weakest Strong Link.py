#link to problem: https://datalemur.com/questions/python-weakest-strong-link

def weakest_strong_link(strength):
  #[1, 2, 3
  # 4, 5, 6
  # 7, 8, 9]
  #smallest number in the row, largest number in column.
  #store smallest #, store largest and compare. 
  
  #i=1, j=1, 2, 3 i1-j1, 
  #initialize rows 
  min_rows = [0] * len(strength)
  max_col = [0] * len(strength[0])
  
  m = len(strength) #number of rows 
  n = len(strength[0]) #number of columns


  # Find the minimum in each row
  min_rows = [min(row) for row in strength]

  # Find the maximum in each column
  max_col = [max(strength[i][j] for i in range(m)) for j in range(n)]

  # Check for the element that is both min in its row and max in its column
  for i in range(m):
    for j in range(n):
      if strength[i][j] == min_rows[i] and strength[i][j] == max_col[j]:
        return strength[i][j]
  return -1
