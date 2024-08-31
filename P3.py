import numpy
#n=numpy.array([[1,2],[3,4]])
arr=[]
size=int(input("Enter the size of the array:"))
for i in range(size):
	row= list(map(int,input().split()))
	arr.append(row)
print("Array:")
print(arr)
print("Sum of elements:")
print(numpy.sum(arr))
print("Sum of each col:")
print(numpy.sum(arr,axis=0))
print("Sum of each row:")
print(numpy.sum(arr,axis=1))

