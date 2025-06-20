"""  
    topics-6
   .insert(arr,index,value,axis=None/0/1) -> inserts value in arr on the basis of the index and the axis(row-wise/col-wise) 
   .append(arr,value) -> add the "value" to the end of the array 
   .concatenate(arr1,arr2,axis=[None,0,1]) -> joins two arrays 
   .delete(array,index,axis=[None,0,1]) -> deletes the element on the basis of the index and the axis(row-wise/col-wise)
   .split(array,sections) -> splits the array into given "sections" 
   .stack()/hstack()/vstack() ->stacks the arrays together (like we do in a DS "stack",that way)
"""

import numpy as np 
#inserting in a numpy array 
""" syntax:
    np.insert(arr,index,value,axis=None) 
    arr - original array 
    index - index in the original array 
    axis: 0 in 2D array for row-wise insert 
    axis: 1 in 2D array for column-wise insert 
"""
arr=np.array([1,2,3,4,5]) 
print("original array(Not inserted)",arr)
new_arr=np.insert(arr,2,100,axis=0)
print("new array(inserted something..)",new_arr) 

twoD_arr=np.array([[1,2,3],
                   [4,5,6]])
new_twoD_arr=np.insert(twoD_arr,0,33,axis=0) # for axis=None array->flatten 

print(new_twoD_arr) 

#append in a array 

new_arr_hehe=np.append(arr,[69,70,71]) 
print(new_arr_hehe) 

#joining two numpy arrays 
""" np.concatenate(arr1,arr2,axis={None/0/1})
    if axis=None -> 1D array 
    if axis=0 -> vertical concatenation 
    if axis=1 -> horizontal concatenation 
""" 

arr1= np.array([1,2,3]) 
arr2=np.array([4,5,6])  
new_arr_haha=np.concatenate((arr1,arr2))
print(new_arr_haha) 

#removing elements in array 

""" 
    np.delete(arr,index,axis=None)
    flattened array -> delete 
""" 

n=np.array([10,20,30]) 
newA=np.delete(n,2,axis=None) 
print(newA)
n2=np.array([[2,3,4],[5,6,7]]) 
newTwo=np.delete(n2,0,axis=0) 
print(newTwo) 


#Stacking and spliting arrays 
"""  
      vstack() row wise (eka khali ek)
      hstack() column wise (ek shath)
""" 
print("Vertical stacking:",np.vstack((arr1,arr2))) 
print("Horizontal stacking:",np.hstack((arr1,arr2)))  


"""  
     np.split() 

     np.hsplit() 

     np.vsplit() 
""" 

print(np.split(n2,2))  


