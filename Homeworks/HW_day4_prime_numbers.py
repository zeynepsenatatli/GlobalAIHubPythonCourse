
def primeNums():
  
  for num in range(0,100):
    if num == 0 or num == 1:
      continue

    elif num == 2:
      print(num)
    
    else:
      for k in range(2,num):
        if (num % k) == 0:
          break
      else: 
        print(num)

primeNums()
