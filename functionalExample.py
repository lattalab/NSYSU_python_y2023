import random, functools
grammar=dict(S=[['NP','VP']],NP=[['Art','N']], VP=[['V','NP']],Art=['the','a'],N=['boy','ball','girl','table'],V=['hit','heard','saw','liked'])
def gen(phrase):return isinstance(phrase,list) and mend(gen, phrase) or (phrase in grammar) and gen(random.choice(grammar[phrase])) or [phrase]
def mend(fn, args): return [item for res in map(fn, args) for item in res]
print(functools.reduce(lambda x,y: x+" "+y, gen('S')).capitalize()+".")

# isinstance: 如果是那個Type回傳True