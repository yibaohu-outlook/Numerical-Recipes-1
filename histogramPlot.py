import matplotlib.pyplot as plt
from MyExponentialPDF import *

#parameters for new exponential pdf
a=0
b=15
tau=2.2
targetValue=1000

expo = ExponentialPDF(a,b,tau)
dist=[0 for x in range(0,targetValue)] 
for i in range(0,targetValue):
	dist[i]=expo.next()

plt.hist(dist, bins = 20)
plt.show()


# plot histograms of tau by reading in from files (because running it 5000 times takes for ever!)
with open('decayTimesMinim.txt') as f:
    lines = f.read().splitlines()

values1 = [float(lines[i]) for i in range(0,len(lines))]
plt.hist(values1, bins=15, alpha = 0.5, label = 'Minimiser')

with open('decayTimesML.txt') as f:
    lines = f.read().splitlines()

values2 = [float(lines[i]) for i in range(0,len(lines))]
plt.hist(values2, bins=15, alpha = 0.5, label = 'Maximum likelihood')
plt.legend(loc='upper right')
plt.show()
