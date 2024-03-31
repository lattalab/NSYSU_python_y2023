a,b,c=1,1,1
def outer():
    a=2
    def mid1():
        def mid2():        
            b=3
            def mid3():
                def innerBroken():
                    nonlocal a,b,c #Can't find global c
                    print(a,b,c)
                innerBroken()
            mid3()
        mid2()
    mid1()
outer()
