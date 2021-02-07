print("LOGIN")

username = "Levi"
password = "Ackermann"

us1 = input("Please enter your username:" )

p1 = input("Please enter your password:" )

if us1 != username and p1 != password:
  print("Invalid username and password!")
elif us1 != username and p1 == password:
  print("Invalid username!")
elif us1 == username and p1 != password:
  print("Invalid password!")
else:
  print("You are logging in")
