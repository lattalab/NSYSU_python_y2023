"""This is a template for a game I call "Up, Down, Turn Around."
   It involves applying increment, decrement and invert operations to randomized subsets of a
   group of 10 bins. (Here, I am using the word "subset" in its mathematical sense. In reality,
   this homework implements the bins as a list, not a set (because order matters).)
   The accompanying "sampleruns" file shows how it should behave. Please read that file now...

   OK, so you have read the "sampleruns" file.

   The rest of this file is a template of the solution to the programming assignment. Your job is
   to: 1) Fill in all of the _____ below (you can also remove my comments, if you want to),
       2) Rename the file as "UpDnTA.py", and 3) submit "UpDnTA.py" to the cyberuniversity by
       Tuesday, April 18th at 11:59 pm."""

from random import shuffle, randrange
from copy import copy        # We never mentioned this one, but it does what the name suggests.
bins=list(map(copy,[[0]]*10))# We want "bins" to become:   [[0], [0], [0], ... [0]].

L1=copy(bins); L2=copy(bins); L3=copy(bins)  #Do you understand why we needed to make copies?
shuffle(L1);   shuffle(L2);   shuffle(L3)    #In each case, the 10 [0] are shuffled.

def up(singleton): singleton[0]+=1                     #The argument is a singleton list.
def down(singleton): singleton[0]-=1                   #The argument is a singleton list.
def turnaround(singleton): singleton[0]=-singleton[0]  #The argument is a singleton list.

def makeshallow(L):
    """This takes a list like this [[#0], [#1], [#2], ... [#9]]
       and returns a list like this [#0, #1, #2, ... #9]        """
    #Put any number of lines of code here
    List = [] #empty list
    for i in L: 
        List.append(i[0])
    return List 

funcs=[{  up  :(L1[:5])}, {  up  :(L1[5:])}, {  up  :(L2[:5])}, {  up  :(L1[5:])} ,
       {  down  :(L1[:5])}, {  down  :(L1[5:])}, {  down  :(L2[:5])}, {  down  :(L2[5:])} ,
       {  turnaround  :(L3[:5])}, {  turnaround  :(L3[5:])}
      ]
#  funcs=[{__1__:__2__}, {__3__:__4__}, ... {__19__:__20__}]
#  __1__, __3__, __5__, __7__:  These are: references to the up function.
#  __2__, __4__, __6__, __8__:  These are: The first 5 elements of L1, the last 5 elements of L1
#                                      The first 5 elements of L2, and the last 5 elements of L2.
#
#  __9__, __11__,__13__,__15__: These are: references to the down function.
#  __10__,__12__,__14__,__16__: These are the same as __2__, __4__, __6__, and __8__.
#
#  __17__, __19__:              These are: references to the turnaround function.
#  __18__, __20__:              These are: The first 5 elements of L3, the last 5 elements of L3.

shuffle(funcs)  # So now, funcs is a list of dictionaries. Each dictionary has a function for its
                # key, and each dictionary has a singleton list for its value.

steps=[]
for i in range(3): steps.append(randrange(0,10)) 
# This line creates a list of 3 random numbers in the range of 0 to 9.

# If we wanted to make the puzzle harder, we'd increase range's arument.
# But that is not part of this assignment

def showanddosteps():
    """This function is used to make the puzzle easier. It shows you which numbers are up, are
       down, and are turnaround. It also shows what steps were taken. (In a real game, this
       function would not be executed, and the puzzle would be much harder.)"""
    # The following line shows the 10 functions, in the order that they were shuffled. You can
    # see the format of this print in the sampleruns file:

    # enumerate :將已打亂的funcs 依順序配對1~10
    # *f得到funcs裡的某一個dictionary，透過這樣印出來
    # 得到相對的output
    
    for i,f in enumerate(funcs): print("\t",i,": ",str(*f.items()).split(" ")[1], sep='')
    print(end="\n        ")
    # *steps :把list裡面的元素印出來
    print(*steps,sep = ', ') # This prints steps, with commas in between. The format is shown in sampleruns

    # The following line is tough. Variable s is one step. __1__ is the key of one element of
    # the funcs list (that is: the element at index s). __2__ is the value for that key.
    for s in steps: list(map(list(funcs[s].keys())[0] , list(funcs[s].values())[0]))#(Here, we make it a list just to force it to run)
    print();print();print()

showanddosteps()

while(any(makeshallow(bins))): #The ____ is a builtin function to test if some elements aren't 0.
    print("%3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"%(tuple(range(1,11))))#prints 1  ...  9  10
    print("%3d %3d %3d %3d %3d %3d %3d %3d %3d %3d"%(tuple(makeshallow(bins))))#print current bins
    while (True):
        a=input("\nPress a key from 0 to 9 (or 'R' to Reset): ")
        if (a in "0123456789Rr"): break # Valid keys are 0, 1, ... 9, r, and R.
    if a == 'r' or a =='R': # this handles resets
        for i in bins: i[0]=0 #Notice how we use updating to keep it pointing at the same thing
        showanddosteps()
        continue
    list(map(list(funcs[int(a)].keys())[0] , list(funcs[int(a)].values())[0]))#This is like the line from showanddosteps, but it uses a, not s

print("\n\n%3d %3d %3d %3d %3d %3d %3d %3d %3d %3d!\n"%(tuple(makeshallow(bins))))