a,b,c=1,1,1
def outer():
    a=b=2
    def mid1():
        def mid2():        
            b=3
            def mid3():
                def inner():
                    nonlocal a,b
                    global c
                    print(a,b,c)
                inner()
            mid3()
        mid2()
    mid1()
outer()
