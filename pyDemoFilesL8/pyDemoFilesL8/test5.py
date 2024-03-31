x=1;y=1;z=1
def f():
    x=2;y=2
    def g():
        x=3
        print (x,y,z)
    g()
g()
