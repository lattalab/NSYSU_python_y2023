def changeme(mytuple, x): 
    """Changes a parameter"""
    mytuple=(1,2,3); x = 7
    print ("Values in the callee:", mytuple, x) 
mytuple = (10,20,30); x = 2 
print ("Values in the caller:", mytuple, x) 
changeme( mytuple, x ) 
print ("Values in the caller:", mytuple, x) 
