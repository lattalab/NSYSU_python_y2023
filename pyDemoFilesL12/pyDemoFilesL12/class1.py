class Puppy(object):
     color = 0
     def __init__(self, name, color):
         self.name = name
         Puppy.color = color
     def bark(self):
         print ("I am", Puppy.color, self.name)
puppy1 = Puppy("Max", "brown")
puppy1.bark()
puppy2 = Puppy("Ruby", "black")
puppy2.bark()
