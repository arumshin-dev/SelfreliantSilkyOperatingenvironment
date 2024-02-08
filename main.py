class Dog:
  def __init__(self, name, age, color):
    self.name = name
    self.age = age
    self.color = color

  def sleep(self):
    print("zzzz....")
    
class GuardDog(Dog):
  def __init__(self, name, color):
    super().__init__(name, 5, color)
    self.aggresive = True

  def rrrrr(self):
      print("stay away!")

class Puppy(Dog):
  def __init__(self, name, color):
    super().__init__(name, 0.1, color)
    self.spoiled = True
    
  def woof_woof(self):
    print(f"{self.name} woof woof!")

    
ruffus = Puppy(
  name="Ruffus", 
  color="brown",
)
bibi = GuardDog(
  name="Bibi", 
  color="white",
)

print(ruffus, bibi)
ruffus.sleep()
bibi.sleep()

