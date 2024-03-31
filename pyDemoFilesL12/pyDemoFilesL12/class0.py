class Puppy(object):
     color = 0
     def __init__(self, name, color):
         self.name = name
         Puppy.color = color # 改到所有的class

puppy1 = Puppy("Max", "brown")
print(Puppy);print(Puppy.color)
print(puppy1);print(puppy1.color)
puppy2 = Puppy("Ruby", "black")
print(Puppy)
print(puppy1.color)
print(puppy1)
print(puppy1.name)
