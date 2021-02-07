n = int(input("Please enter an integer between 0 and 9 "))

if n <= 9 and n >= 0:
  for i in range(n+1):
    if i%2 == 0:
      print(i)
else:
  print("Invalid score!")
