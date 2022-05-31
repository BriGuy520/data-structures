def a_list(arr):

  
  for i in range(1, len(arr)):
    value = arr[i]
  
    while i > 0 and arr[i - 1] > value: 
      
      arr[i] = arr[i - 1]
      i = i - 1
    
    arr[i] = value
      
  print(arr)
      
    
    
    
  
  
  

a_list([5, 1, 3, 2])