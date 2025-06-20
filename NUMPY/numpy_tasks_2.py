#SECTION C 

#task-1 
import numpy as np 

one_arr=np.array([1,2,3,4,5,6]) 

reshaped_one_arr=np.reshape(one_arr,(2,3))  
append_one_arr=np.insert(reshaped_one_arr,2,[10,20,30],axis=0) 
ones=np.array([1,1,1])
# stack_arr=np.hstack((append_one_arr,one_arr)) i can't do this 

flatten_arr=np.ravel(append_one_arr)
print(flatten_arr) 

#task-2 

arr = np.array([2, 4, np.nan, 8, np.inf, -np.inf])

neww_arr=np.nan_to_num(arr,nan=0, posinf=999,neginf=-999) 

print(neww_arr[neww_arr>1]) 

# task-3 
arr_three = np.array([5, 10, 15, 20, 25, 30]) 

print(arr_three[[0,2,4]]) 
new_arr_three=np.reshape(arr_three,(2,3)) 
print(new_arr_three)

#task-4 
arr_four= np.array([10, 20, 30, 40, 50, 60]) 

new_arr_four=np.split(arr_four,3) 
print(new_arr_four)
