L2wasRunBefore=False
def L1():
    x="L1's value"
    def L2():
        def L3():
            x="L1's value"
            L2()#This call to L2 is from a LOWER level
        global L2wasRunBefore
        if not L2wasRunBefore:
            print("Called from L1, and x =",x)
            L2wasRunBefore=True;
            L3()
        else:
            print("Called from L3, but x =",x)
    L2() #This is the first call to L2()
L1()
