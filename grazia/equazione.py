from cmath import *

def radici(a, b, c):
	if a == 0:
		return
	
	delta = pow(b, 2) - (4*a*c)

	if delta < 0:
		return
	
	elif delta == 0:
		return ( -b / (2 * a) )

	else:
		return (
			(-b + sqrt(delta).real)/ 2*a,
			(-b - sqrt(delta).real)/ 2*a
		)


print("Le radici del polinomio sono: " + str(radici(1, 4, 1)))
