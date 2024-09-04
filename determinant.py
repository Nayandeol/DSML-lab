import numpy as np
n=int(input("Enter the size of an array:"));
arr=[]
for i in range (n):
      x = list(map(int,input().split()))
      arr.append(x)
print("Determinant")
print(int(round(np.linalg.det(arr))))
