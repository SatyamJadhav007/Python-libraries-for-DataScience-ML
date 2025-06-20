"""   
5-topics 
indexing,slicing-> normal python gatach ahe   
fancy indexing -> indexes to get non-sequential access of array elements 
boolean masking -> conditions use kr ani data kaadd array madhun 
reshape -> data same, structure changed(with conditions)... 
flatten/ravel -> multi-dimensional array to 1-D array conversation 
"""
#numpy follows 0-based indexing and also negative indexing 
#array[index] <- for 1D array 
#array[row,column] <- for 2D array 
import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8]) 
print(arr[3]) 
#array slicing: array[start:stop:step] FOR 1D array 
print(arr[1:4:2]) 
print(arr[::-1]) 

#fancy indexing-(non-sequential access of array elements it is) 
#arr[sequence/list]
print(arr[[0,2,3]]) 

#boolean masking(accessing array elements on the basis of conditions)
print(arr[arr>3])  

#reshaping-> changing the dimension without modifing the data in it 
# array.reshape(new_shape) 
#Note: .reshape creates a view and not a copy,meaning that changes will be reflected on the memory location 
#Also,the number elements in the original array should be equal to the product of the new dimension to make it happen 

reshaped_arr=arr.reshape(2,4)
print(reshaped_arr) 
# flattening-> changing the dimension without modifing the data in it to 1-D
""" 
.ravel() => views 
.flatten()=> copy 
""" 
arr_2D=np.array([[1,2,3],[4,5,6]]) 
print(arr_2D.ravel()) 
print(arr_2D.flatten()) 
