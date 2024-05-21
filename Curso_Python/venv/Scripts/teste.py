m	=	dict()
def	fat(n):
if	n	==	0:
    return	1
elif m.get(n)	!=	None:
    return	m[n]
else:
    m[n]	=	n	*	fat(n-1)
    return	m[n]