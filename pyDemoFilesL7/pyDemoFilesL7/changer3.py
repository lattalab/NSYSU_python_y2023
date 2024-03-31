def changeme( mylist ): 
    """Changes a parameter"""
    mylist= [1,2,3]
    print ("Values in the callee:", mylist) 
mylist = [10,20,30]
changeme( mylist ) 
print ("Values in the caller:", mylist) 
