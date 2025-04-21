--link to problem - https://datalemur.com/questions/python-intersection-of-two-lists
def intersection(a, b):
  final = []
  for num in a:
    if num in b:
      final.append(num)
      
  return final
