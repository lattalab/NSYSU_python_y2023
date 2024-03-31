def splat(*v):
    print("splat:",v)

def doublesplat(**v):
    print("doublesplat:",v)

d = {"A":65,"B":66,"C":67}
splat(d)

splat(*d)

#splat(**d)# TypeError: splat() 
#            takes 0 positional arguments but 3 were given

#doublesplat(d)# TypeError: doublesplat()
#            takes 0 positional arguments but 1 was given

#doublesplat(*d)# TypeError: doublesplat() 
#            takes 0 positional arguments but 3 were given

doublesplat(**d)

