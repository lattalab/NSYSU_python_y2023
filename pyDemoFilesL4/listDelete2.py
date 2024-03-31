L = [ 'abcd', 786, 2.23, 'john', 70.2, 1, 2, 3, 4, 5, 6]
print (L[2]); 
del L[2]; print (L[2]) #L[3] is now in the L[2] spot
print (L)     # See that L[3:] have now all shifted down
del L[2:7:2]; print (L)#This deletes 3rd,5th,and 7th 
del L                  #This deletes the entire list
print (L)              #What prints if there is no list?
