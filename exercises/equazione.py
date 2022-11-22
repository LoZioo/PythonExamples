from cmath import *

#Funzione che, presi in input tre reali a, b, c, torna in output una
#tupla di due elementi reali distinti, o un reale solo, tali che questi
#siano le radici dell'equazione di secondo grado ax^2 + bx + c = 0.
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
