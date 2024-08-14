import numpy as np
arr=[]
size=int(input("enter the size of the array: "))
for i in range(size):
	row=list(map(int,input().split()))
	arr.append(row)
im=np.linalg.inv(arr)
print("inverse: ",im)	
