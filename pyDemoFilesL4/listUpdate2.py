lst = [ 'abcd', 786, 2.23, 'john', 70.2 ]
print (lst[2]); lst[2] = 2001; print (lst[2]) 
lst[1:3]=[9,9,9,9,9] #Replace a range, sizes needn’t match
print (lst)
lst[6:1:-2]=[111,222,333] # Backwards assignment
print (lst)
lst[1:7:2]=[1,2,3,4] #If using a step, sizes must match 
