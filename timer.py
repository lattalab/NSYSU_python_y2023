from time import time
def timer(com="START",was=[0]):
    if com=="START": was[0]=time()
    else: print('   ',
        f'{int(1000000*(time()-was[0])):,d}','usec')
