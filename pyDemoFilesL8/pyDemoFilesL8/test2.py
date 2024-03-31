total = 0; 
def sum( arg1, arg2 ): 
  global total
  total  =  arg1 + arg2; 
  print("Inside total=",total)
sum( 10, 20 ); 
print ("Outside total=",total)
