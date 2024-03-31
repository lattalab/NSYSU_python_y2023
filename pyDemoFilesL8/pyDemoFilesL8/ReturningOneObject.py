def f(): return 1
a=f(); print("a=",a)   # of course 1 variable can get 1 value
def f(): return [1,2]
b=f(); print("b=",b)   # This also assigned just 1 value (a list)
def f(): return [1]
c=f(); print("c=",c)   # This list has just 1 element 
def f(): return (1)
d=f(); print("d=",d)   # Did we create a tuple of one element?
def f(): return (1,)
e=f(); print("e=",e)   # This time we made a 1 element tuple
