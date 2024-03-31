def f(*v):
    print("First argument is:",v[0])
def passPacked(*v):
    f(v)
def passUnpacked(*v):
    f(*v)
print("f(1,2,3):",end="")
f(1,2,3)
print("passPacked(1,2,3):",end="")
passPacked(1,2,3)
print("passUnpacked(1,2,3):",end="")
passUnpacked(1,2,3)

