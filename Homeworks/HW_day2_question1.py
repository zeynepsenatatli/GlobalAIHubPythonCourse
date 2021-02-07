mylist = [1, 5, 7, 4, 6, 11, 9, 3]
mylist1 = list()
num = 0

c = int(len(mylist) / 2)

mylist1 = mylist[0:c]

mylist.extend(mylist1)

while num < c:
  mylist.remove(mylist[0])
  num += 1

print(mylist)
