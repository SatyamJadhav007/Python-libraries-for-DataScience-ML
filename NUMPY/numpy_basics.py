""" 
   topics/concepts - 16
   zeros(shape)-> fill with zeros of "that" shape 
   ones(shape)-> fill with ones of "that" shape 
   full(shape,fill_value) -> fill with "fill_vaLue" of "that" shape 
   arange(start,stop,step) -> like list comprehension(loop condition) but for numpy arrays 
   eye(N) ->  create a identity matrix of sizee N 
   array.shape -> gives the shape of the array 
   array.size -> gives the elements in the array 
   array.ndim -> gives the dimension of the array (1D/2D/3D/>>) 
   array.dtype -> gives the datatype of the array elements 
   array.astype(new_type) -> changes the datatype of the array to "new_type" 
   +-* "**" // "/ "% -> operations on arrays 
   np.sum()/mean()/std()/var()/min()/max() -> aggergations functions of numpy 

"""

import numpy as np 

#creating a numpy array 
arr=np.array([1,2,3,4])
print(arr) 
# .zeros(shape), where shape is the dimension of the array same for ones 
zeros_array=np.zeros(3) 
ones_array=np.ones((2,3))
print("The zeros array is:",zeros_array)
print("The ones array is:",ones_array) 
range_arr=np.arange(1,11,1) 
print("Generating a range for elements in a numpy array:[.arange(start,stop,step)]",range_arr) 
identity_matrix=np.eye(3)
print("The identity matrix is:[.eye]",identity_matrix)
# .shape gives the no. of rows and columns of the array 
print("The shape of the identity matrix is:[.shape]}",identity_matrix.shape)
print("the size of a martrix is:[.size]",identity_matrix.size) 
print("The dimension of a matrix is:[.ndim] it can be 1D/2D/3D?? in that way",identity_matrix.ndim)
print("The data type of the array is:[.dtype]",identity_matrix.dtype)
updated_identity_matrix=identity_matrix.astype(int)
print("changing the datatype of the array:[.astype(new_type)]",updated_identity_matrix.dtype)


#operations on numpy arrays 

new_arr=np.array([[1,2,3],[4,5,6]]) 
print("Addition by something in the numpy array...",new_arr+4) 
print("Subtraction by something in the numpy array...",new_arr-6) 
print("Exponential of the array...",new_arr**3) 

#Aggregation functions 
# sum(), min(), max(), mean(), std(), var()
print("The sum of the array is:",np.sum(new_arr)) 
print("The min of the array is:",np.min(new_arr)) 
print("The max of the array is:",np.max(new_arr)) 
print("The mean of the array is:",np.mean(new_arr))
print("the standard devination of the array is:",np.std(new_arr)) 
print("the variance of the array is:",np.var(new_arr))