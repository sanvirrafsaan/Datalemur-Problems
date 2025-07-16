# Link to problem: https://datalemur.com/questions/python-triangular-sum-of-an-array
def triangular_sum(nums):
  
  n = len(nums)
  #base case 
  if n==1:
    return nums[0]
  
  #input: array length n. Output: array length n-1
  #make the recursive calls until base case reached
  else:
    newNums = []
    for i in range(n -1):
      value = (nums[i] + nums[i+1]) % 10
      newNums.append(value)
    
    return triangular_sum(newNums)
  
