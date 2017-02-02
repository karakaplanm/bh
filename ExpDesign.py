from pyDOE import *
import numpy as np
A=np.zeros([8,4])
A[:,0]=1
A[:,1:4]=ff2n(3)

B=np.zeros([8, 4])
B[:,0]=1
B[:,1]=20+A[:,1]*4
B[:,2]=0.3+A[:,2]*0.2
B[:,3]=3.5+A[:,3]*0.5

C=np.zeros([8, 8])
C[:,0:4]=B[:,0:4]
C[:,4]=B[:,1]*B[:,2]
C[:,5]=B[:,1]*B[:,3]
C[:,6]=B[:,2]*B[:,3]
C[:,7]=B[:,1]*B[:,2]*B[:,3]

print A; print B;print C
b=np.array([[62.4],[90.6],
   [63.5],[91.7],[61.8],
   [88.3],[64.9],[90.2]])
x1,res,rnk,s=np.linalg.lstsq(A,b)
print "x1=", x1
x2,res,rnk,s=np.linalg.lstsq(B,b)
print "x2=", x2
x3,res,rnk,s=np.linalg.lstsq(C,b)
print "x3=", x3
