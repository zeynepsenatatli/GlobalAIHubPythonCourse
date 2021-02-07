class Animals:

  def __init__(self, name, breed, age):
    self.name = name
    self.breed = breed
    self.age = age

  def showInfo(self):
    print("Name: " + self.name)
    print("Breed: " + self.breed)
    print("Age: " + self.age)
    
class Dogs(Animals):
  def __init__(self, which, name, breed,age):
    super().__init__(name, breed, age)
    self.which = which
  
  def features(self):
    print("> There is " + self.which + " in this animal shelter named " + self.name + "." " It's " + self.breed + " and " + self.age + " years old. <")
  
class Cats(Animals):
  def __init__(self, which, name, breed,age):
    super().__init__(name, breed, age)
    self.which = which
  
  def features(self):
    print("> There is " + self.which + " in this animal shelter named " + self.name + "." " It's " + self.breed + " and " + self.age + " years old. <")

dog1 = Dogs("a dog","Max", "a labrador", "4")
dog1.features()
dog1.showInfo()

cat1 = Cats("a cat", "Pamuk", "a British shorthair", "5")
cat1.features()
cat1.showInfo()
