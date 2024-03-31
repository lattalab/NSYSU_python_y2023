#The following defines one object, oldprint:
oldprint=print

def print(*arg ,counter = [0] ,temp = [0,0,0,0] , 
    count = False, reset = False, stats = False , sep=None, end="\n"): 
    # temp's first element to calculate the number of print
    # second element to calculate counter
    # third element to calculate reset
    # fourth element to calculate stats
    """This version of print adds two features, for counting and statistics.
    
To use the counting feature, call print with a "count=True" argument.
The counter has several operating modes:
 - If no "counter" variable is passed-in, a default counter is used.
 - Otherwise, counter must be a list containing only an integer.
 - Also, to reset the counter back to 0, pass in "reset=True".
   Furthermore, if the only argument is "reset=True", nothing prints.

To use the statistics feature, call print with a "stats=True" argument.
In this case, no other arguments are allowed. It will display:
 - How many times print has been called (since importing this version).
 - How many times a counter was printed.
 - How many times a counter was reset.
 - How many times statistics were printed (including the current one)."""

    #The following line use a mutable function argument with a default value
    #(see lecture 7's discussion of this concept). But there is something
    #special about the name of this argument: it should get an unusual name,
    #because users aren't meant to ever use this argument when doing prints.
    #Now what is the purpose of this mutable argument? It keeps track of the
    #four statistics numbers that print if the user runs print(stats=True).
    #
    temp[0] = temp[0] + 1  #Adds 1 to the number that counts how often print was called:
    
    if (type(counter) != list) or (len(counter) != 1):
        raise ValueError("The counter must be a list containing one integer.")
 
    if stats:
        if len(arg) != 0 or count == True or reset == True:
            raise(SyntaxError(
             "When printing statistics, you can't include other arguments."))
        temp[3] = temp[3] + 1 # Adds 1 to statistic of how often statistics were printed
        # Prints the 4 statistice numbers
        oldprint("# ", "print:" , temp[0] ,end="    ")
        oldprint("# ", "with counter:" , temp[1] ,end="    ")
        oldprint("# ", "resets:" , temp[2] ,end="    ")
        oldprint("# ", "statistics:" , temp[3] ,end="\n")
        return

    if reset:
        temp[2] = temp[2] + 1  # Add 1 to the reset statistic.
        counter[0] = 0  # Reset the counter. It is a mutable default-valued argument.
        if len(arg) == 0 : return #Checks if nothing was passed-in to actually print.

    if count==False: return oldprint(*arg, sep=sep, end=end) # like original print() function
    
    temp[1] = temp[1] + 1 # Add 1 to the statistic of how many times a counter was printed.
    counter[0] = counter[0] + 1  # Add 1 to the counter.
    
    #The following makes the separator a ", "--unless the user passes-in sep:
    if sep == None: sep= ", "
    

    oldprint("(%d)"%(counter[0]), end = " ") #Prints the counter, along with its parentheses.
    #Prints the arguments the user passed in for printing.
    oldprint(*arg, sep=sep, end=end)