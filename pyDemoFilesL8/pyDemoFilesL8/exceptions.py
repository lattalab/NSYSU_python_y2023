z = int(input("Enter a number:  ")) 
try: 
   if (z<1): 10 * (1/z)
   if (z<2): 4 + junk*3
   if (z<3): '2' + 2
except ZeroDivisionError: 
   print("You can't divide by zero.")
except NameError:
   print("You didn't define a variable.")
except TypeError:
   print("Your types don't match.")
except:
   print("Some other kind of error happened.")
else: 
   print("I guess there were no problems.")
print("Even with errors, this always prints.")
