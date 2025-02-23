from itertools import cycle  # You must use this for rotating the wheels.
from functools import reduce # You must use this to turn 5 bits into an int.
from random import choice    # You must use this to make the wheel patterns.
from copy import deepcopy    # You must use this for copying wheels for reset.

start = True                 # Use this to tell lorenz() to reset its wheels.

# 每個輪子的大小 & 前五個負責psi & 後五個負責 chi & mu1,mu2
szs=[43,47,51,53,59,37,61,41,31,29,26,23]#These are the 12 lorenz wheel /*sizes*/.
# To explain about these 12 wheels, the first five wheels create 5-bit number
# called "psi", and the last wheels create a 5-bit number called "chi". These
# Psi and chi values are xor'ed together to create the key.
# (The middle two wheels are called "mu1" and "mu2". They are used to define
# when the "chi" wheels are allowed to rotate. They will be described later.)


def lorenz():
   """This function generates an integer from 0 to 31 (ie, a 5-bit integer).
   This integer is generated by a lorenz machine, for use in XOR encription.

   There is also a global variable named start. When it is True, the wheels
   are all either initialized or else reset to their initial values. Also,
   when this happens the start variable get automatically set to False."""
   wheels=[] #儲存輪子內容，內容是好幾個bit
   while 1:
      global start # Something is needed here, to allow "start" to be written-to.
      if len(wheels) == 0: #This test for whether the wheels need to be /*initialized*/.
         for sz in szs:
            wheels.append(cycle([choice([0, 1]) for _ in range(sz)])) # 每個都是list cycle()
            #This uses comprehension, append, cycle and choice.
            #Use cycle to make the iterator cycle like a wheel.
            #Use choice to choose bits randomly as either 0 or 1.
            #Use list comprehension to put the bits around the wheel.
            #Use append to add this wheel into the list of 12 wheels.

         chi = reduce(lambda x,y : 2*x+y, [next(wheels[i]) for i in range(7,12)]) # bits轉換成整數
         #This uses next, comprehension, reduce, and lambda.
         #Use next to get a value and rotate wheel #i.
         #Use list comprehension to take i from 7 to 11 (ie, chi).
         #Use reduce to concatenate the list of 5 bits into 1 int.
         #Use lambda to get a function to double arg1 and add arg2. 

         wheelsCopy= deepcopy(wheels) #This makes a deep copy of wheels.
         chiCopy=chi
      elif start:  #This indicate a reset (ie, time to start decoding).
         wheels=deepcopy(wheelsCopy) #This makes a deep copy of wheelsCopy.
         chi=chiCopy
         yield None #In the case of resetting the wheel, a "None" key is yielded.
      start = False
      
      psi=reduce(lambda x,y : 2*x+y, [next((wheels[i])) for i in range(0,5)]) 
                #This is like the "chi=___" line above, but for wheels 0 to 4.
                #Note: This "psi=___" wil cause the psi wheel to always spin.

      #As just seen above, the psi wheel always spins.
      #But now, for the chi wheel, the decision of whether to spin is handled
      #By the wheels 5 & 6 (ie, the 6th and 7th), (ie, mu1 & mu2)).
      ## -As for mu1, it always spins.
      ## -As for mu2, it only spins if mu1's newly-spun value is a 1.
      ## -As for the 5 chi wheels, they only spins if mu2's new value is a 1.
      
      if (mu1:=(next(wheels[5]))):#This line uses next to spin the 6th wheel and simultaneously
                               #uses expression assignment to put that next value into mu1.
         if (mu2:=(next(wheels[6]))):#A similar use of next+expression assignment, but for mu2. 
            #This is identical to the "chi=___" line up above.
            chi=reduce(lambda x,y : 2*x+y, [next(cycle(wheels[i])) for i in range(7,12)]) 
            
      yield psi^chi # This yields the exclusive-oring of the integers psi and chi.


def enc(s):
   """The lorenz cipher can only encode 5 bits, or 32 values. So the encoding
   will be: A or a -> 0, B or b -> 1, Z or z -> 25, ' ' -> 26, '.' -> 27,
   ',' -> 28, '"' -> 29, '?' -> 30, '\n' -> 32, and anything-else -> -1.

   Note: this wasn't the encoding used by the actual lorenz cypher.
   Note: This enc() function is for encoding, not encryption. That is: it
         return the integer code for the passed-in 1-character string."""
   if s.isalpha(): #Checks if s is a letter (ie, 'a', or 'A', or 'b', or ...)
      return ord(s.lower()) - ord('a') #A or a -> 0, B or b -> 1, Z or z -> 25.
   else:
      return {' ':26, '.':27, ',':28, '"':29, '?':30, '\n':32}.get(s, -1)
                     #' ' -> 26, '.' -> 27, ',' -> 28, '"' -> 29,
                     #'?' -> 30, '\n' -> 32, and anything-else -> -1.
   
def dec(v):return chr(v + ord('A')) if v <=25 and v >=0 else (' ' if v == 26 else ('.' if v==27 else (',' if v==28 else ('"' if v==29 else ('?' if v==30 else ('\n' if v==32 else ""))))))
                         #This reverses enc(). But it uses a conditional
                         #expression to implement it all on one line.

key=lorenz() # This initialize the lorenz() generator.
f=open('PA5template.py','r')   # This opens the file PA5template.py.
text=f.read() # This reads the entire PA5template.py into a string.

print("Encrypted:\n")
print("".join(map(dec, nums:=[next(key)^enc(i) for i in text if enc(i)!=-1] )))
# 將dec() apply to encrypted num, encrypted = key * encoded_num (有把不能轉換的剃除)                 

                  #This uses map(), dec(), expression assignment, enc(),
                  #^, next(), and list comprehension with a for and an if
                  #inside the comprehension. (The if is used in order to
                  #remove any disallowed characters the input -- meaning
                  #any characters for which enc returned -1.)
                  #
                  #As for the expresion assignment, it's used to catch the
                  #encrypted numbers. That is we catch them while they are
                  #still numbers (ie, before they decode into characters).
                  #
                  #The result of all this is to display garbled text.
                    
start = True;next(key) #I did this for you. It reset the wheel for decrypt.

print("\n"," - "*25,"\n\nDecrypted:\n")
print("".join( map(lambda x:dec(x^next(key)), nums) ))
# 將encrypted還原回來 = 再乘一次key

                    #This uses map, lambda, dec, ^, next, and the list of
                    #encrypted numbers caught on the previous print line.
                    #
                    #The result of all this is to display the original text,
                    #but wih all illegal characters removed.

###
f.close() # I add this to close the file.