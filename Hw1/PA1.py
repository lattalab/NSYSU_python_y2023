"""       The First Programming Assignment for "Programming in Python"

   This program reads input from the file indicated by fn, a variable defined
   on the line below this. It then prints facts about that file's text.""" 


fn='AssignmentGuidelines.txt' # This file must be in your current directory
f=open(fn,'r');L=f.readlines()#You haven't learned this yet, so I just did it

#Once the above lines are executed, "L" will contain a list of strings.
#
#These strings correspond to the lines from "AssignmentGuidlines.txt".
#
#Know that the "\n" at the end of each of the lines IS part of its string.



#The following prints: The file "AssignmentGuidlines.txt" contains 100 lines.
#
#SPECIAL REQUIREMENT ON THIS LINE:You must use string concatenation (+), and
#you can't use commas (,) nor any of the ways shown on slide 169 of Lecture2.
#                                  
sentence =str(len(L))
print("The file \"" + fn + "\" contains " + sentence + " lines.")


#The following creates a single string from the list of strings store in L.
#
#Hint:In interactive mode, type help(str.join). Note that this method belongs
#     to the string used as the seperator, not to the strings being joined.
#
#Hint:Since the strings already each end in a "\n", there is no need to add
#     a new separator (meaning that the separator should be ""). 
#
#... = ...
single_str = "".join(L)  #contain all content in .txt


#The following prints this text: There are 61 sentences and 5320 characters.
#
#Hint:In interactive mode, type help(str.count). Note that in this assignment
#     every sentence ends in a period (".").
#
#SPECIAL REQUIREMENT ON THIS LINE: You must use "," and you can't use "+" nor
#any of the ways shown on slide 159 of Lecture 2.
#
#print(...)
print("There are", single_str.count('.'), "sentences and", len(single_str),"characters.")


#The following creates a list of strings, where each string is a sentence.
#The period will NOT be part of the string.
#
#Note that words in sentences are separated by spaces. But, also note that
#sentences cross line boundaries (eg, this current sentence spans 3 lines)--
#and, when crossing line boundaries, words are separated by "\n" not by " ". 
#
#Hint:Type help(str.replace) & consider how to fix crossing line boundaries.
#
#Hint:Type help(str.split) & consider how sentences are separated by periods.
#
#Hint:Know that strings are immutable, so str.replace() returns a new string.
#     But consider how that returned string can then have its own methods.
#     This is called chaining. Eg: chr(65).lower().upper().lower().islower()
#
#...=...
str1 = single_str.replace("\n"," ")
str2 = str1.split('.') #separate every sentence with '.' ,and store in list



print('\nThe file gives 7 guidance rules:')# I've given you this simple line.


#The following prints the 7 numbered sentences starting with "1)...", "2...",
#up through "7)...". Moreover, your output cannot print quotation marks.
#Hint: splat.
#
#SPECIAL REQUIREMENT ON THIS LINE: You may only use one "[". In other words,
#I require you to use index slicing.
#
print(".\n".join(list(str2[3:22:3])) + ".\n") #use str.join() and slicing


#The following creates a list of strings, where each string is a word.
#These words are all of the words from the input file (which means that there
#will be duplicates). These words are lower case. These words only contain
#letters (which means all punctuation and all numbers have been removed). 
#Hints on str.replace(arg1, arg2):
#   - Know that str.replace(arg1, arg2) will replace all instances of arg1.
#   - Know that, if arg2 = "", then str.replace can be used to do a delete.
#   - Know that chaining works (ie: str.replace(___).replace(___)...  ).
#   - Know that the only punctuation you need to remove are the punctuation
#     symbols found in AssignmentGuidlines.txt (ie: ",","(",")",":",";","-").
#   - Know that, once all of the punctuation and numbers are removed, you
#     may now have sequences with multiple spaces in a row. But if you then
#     reduce all pairs of spaces "  " into single spaces " ", then it reduces
#     the problem. And, if you chain this replacement action 3 times, then no
#     "  " will exist.  Note: 3 times will be enough for all our test inputs.
#     (By the way, if you were allowed to use techniques beyond the first
#     two lectures, there are easier ways to remove the punctuation -- but
#     we don't know those ways yet, so you cannot use them.)
#
#Hint on str.lower():
#   - Know that this is a method, not an attribute. So, even though it takes
#     no arguments, you invoke it with "str.lower()", not "str.lower".
#
#Hints on str.split():
#   - Know that invoking the split will create a list, so any chaining of str
#     methods must be done BEFORE invoking split.
#   - Know that words are separated by spaces. 
#
#...=...

#no punctuation symbols
str3 = str1.replace(",","").replace("(","").replace(")","").replace(":","").replace(";","").replace("-","").replace(".","")
#no number
str3 = str3.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
#reduce spaces
str3 = str3.replace("  "," ").replace("  "," ").replace("  "," ")
#to lower case and then split() 
list1 = str3.lower().split(" ")


#The following prints this text: There are 894 words.
#SPECIAL REQUIREMENT ON THIS LINE: You must use a formatted string literal
# containing a "{", and you cannot use any commas (,) or concatenation (+).
#Hint: See Lecture 2, Slide 169.
#
print(f"There are {len(list(list1))} words.")


#The following prints this text: But there are only 324 distinct words.
#SPECIAL REQUIREMENT ON THIS LINE: You must use "%".
#Hint: See Lecture 2, Slide 169.
#Hint: Sets have no duplicate elements.
#
set1 = set(list1)
print("But there are only %d distinct words."%(len(set1)))


print()   # I've given you this simple line.


#The following prints: The most common word is "the", which occurs 52 times.
#SPECIAL REQUIREMENT ON THIS LINE: You must use the string method called
#"format", as explained on Slide 168 of Lecture 2.
#
print("The most common word is \"the\", which occurs {:d} times.".format(list(list1).count("the")))


#The following prints: The next-most-common is "you", which occurs 45 times.
#There are NO SPECIAL REQUIREMENTS.
#
print("The next-most-common is \"you\", which occurs {:d} times.".format(list(list1).count("you")))


#The following prints:
#But if occurances of "your" are included then "you" occurs 64 times in total.
#There are NO SPECIAL REQUIREMENTS.
#
print("But if occurances of \"your\" are included then \"you\" occurs {:d} times in total.".format(list(list1).count("your") + list(list1).count("you")))
