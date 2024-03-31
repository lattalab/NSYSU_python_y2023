from random import shuffle
cards=list(range(14*4))
del cards[14*3],cards[14*2],cards[14*1],cards[14*0]
shuffle(cards)
p=0
