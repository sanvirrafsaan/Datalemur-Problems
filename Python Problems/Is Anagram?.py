#link to problem: https://datalemur.com/questions/python-is-anagram

def is_anagram(s, t):
  """
  Determine if two strings are anagrams 
  Args: 
    s (str): The source string
    t 9str): The string to compare to 's'
  Returns: 
    bool: Returns True if 't' is an anagram of 's'. False otherwise
  
  """
  
  if len(s) != len(t):
    return False 
  
  s_dict = {}
  t_dict = {}
  
  for i in range(len(s)):
    if s[i] in s_dict: 
      s_dict[s[i]] += 1
    else: 
      s_dict[s[i]] = 1
    
    if t[i] in t_dict: 
      t_dict[t[i]] += 1
    else: 
      t_dict[t[i]] = 1
    
  return s_dict == t_dict
