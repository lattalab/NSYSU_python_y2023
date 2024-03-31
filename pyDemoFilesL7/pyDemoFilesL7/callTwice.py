# *vartuple 是 *arg 的意思
def printinfo( arg1, *vartuple ): 
    print ("Output is:") 
    print (arg1)
    # print(vartuple)
    for var in vartuple: 
        print (var) 
printinfo( 10 )
printinfo( 70, 60, 50 )
