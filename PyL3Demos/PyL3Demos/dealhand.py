from importlib import reload
print(end="\n    ")
import deck, dealcard
reload(dealcard);reload(dealcard)
reload(dealcard);reload(dealcard)

n=input("\n\nHow many cards to discard? ")
print(end="\n    ")

L=list(range(int(n)))#The list elements don't matter
for i in L:          #What matters is the # of them
    reload(dealcard) #So this line runs n times
print()
