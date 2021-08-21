## Author: Ganji Varshitha (AI20BTECH11009) ##
## Code to verify the matrix as symmetric or skew symmetric ##
#importing numpy and matplotlib libraries
import numpy as np
import matplotlib.pyplot as plt

## (i)
## Given matrix 
A= np.array([[1,-1,5],[-1,2,1],[5,1,3]])
print(A)
# Finding transpose
A_trans = A.T
print(A_trans)
# Finding whether the matrix is symmetric
diff= A-A_trans
#diff is null matrix
if (diff.all()==0):
  print("A is a symmetric matrix")
  
##(ii)
## Given matrix 
A= np.array([[0,1,-1],[-1,0,1],[1,-1,0]])
print(A)
# Finding transpose
A_trans = A.T
print(A_trans)
# Finding whether the matrix is skew symmetric i.e A = - A.trans
diff= A+A_trans
#diff is null matrix
if (diff.all()==0):
  print("A is a skew symmetric matrix")
