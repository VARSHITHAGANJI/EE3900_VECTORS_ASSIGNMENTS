## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to find the shortest distance between 2 skew lines and plotting the lines in 3D space ##
#importing required libraries

import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import nnls
from mpl_toolkits.mplot3d import Axes3D

## Line 1 = (1,2,3) + lambda1(1,-3,2)
## Line 2 = (4,5,6) + lambda2(2,3,1)

#Generate line points
def line_gen(A,B):
  len =20
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(-2,2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B)
    x_AB[:,i]= temp1.T
  return x_AB

def point_gen(A,B,L):
  return A + L*B





#setting up plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_ylim([-4, 10])
ax.set_xlim([-1, 10])
ax.set_zlim([2, 10])


#Points for line 1
A1 = np.array([1,2,3]).reshape((3,1))
B1 = np.array([1,-3,2]).reshape((3,1))

#Generating line 1
x_AB = line_gen(A1,B1)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='g',label='Line 1')
 



#Plotting and labelling point A1

ax.scatter(1,2,3,'o',label='a1')
ax.text(1 * (1 + 0.1), 2 * (1 - 0.1) ,3*(1-0.1), "(1,2,3)")


#Points for line 1
A2 = np.array([4,5,6]).reshape((3,1))
B2 = np.array([2,3,1]).reshape((3,1))

#Generating line 1
x_AB = line_gen(A2,B2)
#plotting line
plt.plot(x_AB[0,:],x_AB[1,:],x_AB[2,:],color='r',label='Line 2')

#Plotting and labelling point A2

ax.scatter(4,5,6,'o',label='a2')
ax.text(4 * (1 + 0.1), 5* (1 - 0.1) ,6*(1-0.1), "(4,5,6)")