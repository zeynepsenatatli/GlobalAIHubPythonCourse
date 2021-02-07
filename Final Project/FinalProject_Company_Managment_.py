class employees:
  def __init__(self, name, lname, age, language):
    self.name = name
    self.lastname = lname
    self.age = age
    self.language = language
 
  def showInfo(self):
    print(self.name + " " + self.lastname + " is a manager at Company. " + self.name + " is " + self.age + " years old.")

  def showLanguages(self):
    print(self.name + " " + self.lastname + " can speak:")
    for i in self.language:
      print(i)

class managers():
  def __init__(self, name, lname, age, language):
    self.name = name
    self.lastname = lname
    self.age = age
    self.language = language
  
  def showInfo(self):
    print(self.name + " " + self.lastname + " is an employee at Company. " + self.name + " is " + self.age + " years old.")

  def showLanguages(self):
    print(self.name + " " + self.lastname + " can speak:")
    for i in self.language:
      print(i)

employee1 = employees("Mark", "Smith", "34", ["Spanish","English"])
employee2 = employees("Jasmine", "Diaz", "29", ["English", "Persian"])
employee3 = employees("Kardelen","Yılmaz", "26", ["English", "Turkish"])
manager1 = managers("Otto", "Bauer", "47", ["English", "German", "French"])

employee1.showLanguages()
employee2.showLanguages()
employee3.showLanguages()
manager1.showLanguages()
