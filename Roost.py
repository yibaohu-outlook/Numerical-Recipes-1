from Bisect import *
from Newton import *
import numpy as np
import sys
from Functions import *
import matplotlib.pyplot as plt


"""Plots"""

polynomials = [polynomial(x) for x in np.arange(-3,4,0.001)]
exponentials = [exponential(x) for x in np.arange(-3,4,0.001)]
x_0 = [0 for x in np.arange(-3,4,0.001)]
x_axis = [x for x in np.arange(-3,4,0.001)]

plt.plot(x_axis, x_0)
plt.plot(x_axis, polynomials)
plt.plot(x_axis, exponentials)
plt.show()





tollerance = 0.00001


"""-----------Newton-Raphson-----------------"""


"""--Polynomial"""
# Nth order polynomial will have at most N roots so can assume that the number of roots is known

#initial guess
a_guess, b_guess, c_guess = -2.0, 0.0, 4.0
#starting number of steps
numsteps = 1

root_a, root_b, root_c = [a_guess], [b_guess], [c_guess]
i = 0

#finding roots until tollerance is met
while (np.fabs(root_a[i]-true_root_poly_a)>tollerance and np.fabs(root_b[i]-true_root_poly_b)>tollerance and np.fabs(root_c[i]-true_root_poly_c)>tollerance):
	root_a.append(newt(root_a[i],numsteps,polynomial, poly_prime)) 
	root_b.append(newt(root_b[i],numsteps,polynomial, poly_prime)) 
	root_c.append(newt(root_c[i],numsteps,polynomial, poly_prime))
	i = i+1
	numsteps = numsteps*10

newton_poly_roots = [root_a, root_b, root_c]
poly_numsteps = numsteps

#print (root_a, root_b, root_c)



"""--Exponential"""
#There is only one root

numsteps=1
root_guess = 5
root = [root_guess]
i=0
while np.fabs(root[i]-true_root_exp)>tollerance:
	root.append(newt(root[i],numsteps,exponential,exp_prime))
	i = i+1
	numsteps = numsteps*10

newton_exp_root = root
exp_numsteps= numsteps
print root


"""----------Bisection-------------------"""

"""--Polynomial"""

#ranges where function changes sign
a_init, b_init, c_init = [-5.0,0.0],[0.0,2.0],[2.0,5.0]

bis_a, bis_b, bis_c = bisection(a_init[0], a_init[1], tollerance, polynomial), bisection(b_init[0], b_init[1], tollerance, polynomial), bisection(c_init[0], c_init[1], tollerance, polynomial)

bisect_poly_roots = [bis_a[0], bis_b[0], bis_c[0]]

#number of itterations it took
bisect_poly_count = [bis_a[1],bis_b[1],bis_c[1]]

#print (bis_a, bis_b, bis_c)


"""--Exponential"""

init = [-1,5]
bis = bisection(init[0],init[1],tollerance,exponential)
root = bis[0]
count=bis[1]

bisect_exp_root = bis[0]
bisect_exp_count = bis[1]


"""Print Number of steps to terminal"""

print "--Compating Number of Steps:"
print "	Polynomial	|	Exponential"
print "N-R:	%s		%s" % (bisect_poly_count, bisect_exp_count)
print "B:	%s			%s" % (poly_numsteps, exp_numsteps)



