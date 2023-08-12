import random
import numpy as np
from matplotlib.pyplot import *

n=10000

array=np.zeros(n)
for i in range(n):
    array[i]=int((random.triangular(1,10)))
y=np.zeros(10)
x=np.zeros(10)

#Add together instances of a given integer in the random array
for i in range(1,10):
    y[i]=np.sum(array==i)/n*100
    x[i]=i
    

fig=figure()

bar(x,y)
xlabel('Integer')
ylabel('Percent occurence (%)')

savefig('actual_triangular_distribution.png') # Save figure
show()