import numpy as np
import scipy

A=np.array([[1,2,3,-2,-1],[3,5,5,-3,-9],[2,3,2,0,-8],[2,6,7,-5,1],[1,2,6,-4,-10]])
B=np.array([[6],[2],[-5],[17],[12]])
x = np.linalg.solve(A,B)

print("rozwiazania:")
print("x =", round(x[0][0],3))
print("y =", round(x[1][0],3))
print("z =", round(x[2][0],3))
print("t =", round(x[3][0],3))
print("u =", round(x[4][0],3))