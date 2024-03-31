def repeat(v,k=[]):
    g = int(v) if k==[] else k[0]
    k.insert(0,g-1)
    return g
