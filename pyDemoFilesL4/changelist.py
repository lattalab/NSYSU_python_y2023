L=list(range(20))
for i in L:
    if 5<=i<=14: del L[i]
print("You can do it, but generally shouldn't.")
print("Do you think this program drops 5-14?")
print("Drops:",sorted(set(range(20))-set(L)))
