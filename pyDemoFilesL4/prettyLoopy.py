S = "Where is the 'X'?"
print('Looking for "X" in "%s"'%(S))

#To only see if a value is contained:
for letter in S:
   if letter == "X":
      print("Found, but can't say where")

#To keep track of where, make an ugly loop:
for pos in range(len(S)):
   if S[pos] == "X":
      print("Found at:",pos)

#But, actually, we can use a pretty loop:
for letter in enumerate(S):
   if letter[1]=='X':
      print("Found at:",letter[0])

#But, actually, we can be even prettier:
for pos, letter in enumerate(S):
   if letter=='X':
      print("Found at:",pos)

#But, actually, top programmers reuse code:
if "X" in S:print("Found at:",S.find("X"))
