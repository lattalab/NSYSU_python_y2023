import random, functools
grammar=dict(S=[['NP','VP']],NP=[['Art','N']], VP=[['V','NP']],Art=['the','a'],N=['boy','ball','girl','table'],V=['hit','heard','saw','liked'])
gen=lambda phrase: isinstance(phrase,list) and mend(gen, phrase) or (phrase in grammar) and gen(random.choice(grammar[phrase])) or [phrase]
mend = lambda fn, args: [item for res in map(fn, args) for item in res]
print(functools.reduce(lambda x,y: x+" "+y, gen('S')).capitalize()+".")

