#link to problem: https://datalemur.com/questions/python-roman-to-integer
def romanToInt(s: str) -> int:
  """
  Takes roman numerals and converts it to numbers
  Args: 
    string: A roman numeral string (e.g XI)
  Returns:
    int: a number representing the converted roman numeral

  Notes:
    Handles subtractive notation:
    - IV = 4, IX = 9
    - XL = 40, XC = 90
  """
  
  values = {"I":1, "V": 5, "X":10, "L":50, "C":100, "D":500, "M":1000}
  
  #add the last letter value 
  output = values[s[-1]] 
  
  #start from second last letter to not get index error
  i = len(s) - 1 -1
  #move right to left, adding or subtracting numbers 
  while i >= 0:
    current = values[s[i]]
    if current >= values[s[i+1]]:
      output = output + current 
    else: 
      output = output - current
    i -= 1
        
  return output
