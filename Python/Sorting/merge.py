def merge(a_list):

  if len(a_list) > 1: 
    mid = len(a_list) // 2
    left_side = a_list[:mid]
    right_side = a_list[mid:]
    merge(left_side)
    merge(right_side)
    
    left_idx = 0
    right_idx = 0
    original_idx = 0
    
    while left_idx < len(left_side) and right_idx < len(right_side):
      if left_side[left_idx] < right_side[right_idx]:
        a_list[original_idx] = left_side[left_idx]
        original_idx += 1
        left_idx += 1
      else: 
        a_list[original_idx] = right_side[right_idx]
        original_idx += 1
        right_idx += 1

    
    while left_idx < len(left_side):
      a_list[original_idx] = left_side[left_idx]
      original_idx += 1
      left_idx += 1
      
    while right_idx < len(right_side):
      a_list[original_idx] = right_side[right_idx]
      right_idx += 1
      original_idx += 1
      
  
  return a_list      
  
  
print(merge([3, 4, 1, 4, 99, 32, 84, 45, 27, 11, 99]))