import numpy as np
arr1=list(map(int,input().split()))
print("arr1=",arr1)
arr2=list(map(int,input().split()))
print("arr2=",arr2)
if np.array_equal(arr1,arr2):
	print("equal")
else:	
	print("not equal")
