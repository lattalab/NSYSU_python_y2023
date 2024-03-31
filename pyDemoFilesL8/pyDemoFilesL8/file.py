fo = open("foo.txt", "w" ) 
fo.write("Python is great." ); 
fo.write("Yeah it's great!!\r\n" ); 
fo = open("foo.txt", "r" ) 
str = fo.read(17); 
print ("Read String is :", str) 
fo.close()
