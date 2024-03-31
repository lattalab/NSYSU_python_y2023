def f(): return (1,2)
a=f(); print("a=",a) 			# A two-element tuple
def f(): return 1,2
x,y=f(); print("x=",x," y=",y)	# Is this legal?
def f(): return (1,2)
x,y=f(); print("x=",x," y=",y)	# Is this legal?
a=f(); print("a=",a)			# We’ve seen this before
def f(): return 1,2			
x,y=f(); print("x=",x," y=",y)	# We’ve seen this before
a=f(); print("a=",a)			# But is this legal?
