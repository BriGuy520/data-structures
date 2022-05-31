def selection(a_list):
  
  for i in range(0, len(a_list)):
    
    minIndex = i
    
    for j in range(i + 1, len(a_list)):
      
      if a_list[j] < a_list[minIndex]:
        minIndex = j
        
    if minIndex != i:
      temp = a_list[minIndex]
      a_list[minIndex] = a_list[i]
      a_list[i] = temp
  
  print(a_list)


selection([1, 4, 3, 2, 0, 19, 24, 4])