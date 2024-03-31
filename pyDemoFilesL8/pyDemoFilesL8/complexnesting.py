x=1
def f(): x=2; print("prints Za:",x)
def g(): print("prints Zb:",x)
def h():
    x=4
    def i():
        print("prints Zc:",x)
    def j():
        x=5
        print("prints Zd:",x)
    def k():
        print("prints Ze:",x)
    i();j();l();print("prints Zf:",x)
def l():
    def k():
        print("prints Zg:",x)
#   k() # This would crash
    x=6
    k()
    print("prints Zh:",x)
print("prints Zi:",x)
l()
print("prints Zj:",x)
x=3
f();g();h();l()
print("prints Zk:",x)

