print("LOGIN")

accounts = {"Levi" : "Ackermann", "Mikasa" : "Ackermann", "Erwin" : "Smith"}

us1 = input("Please enter your user name:")

p1 = input("Please enter your password:")

if us1 in accounts.keys():
  if p1 == accounts[us1]:
    print("You are logging in")
  else:
    print("Invalid password!")

elif p1 in accounts.values():
    print("Invalid username!")

else:
  print("Invalid username and password!")
