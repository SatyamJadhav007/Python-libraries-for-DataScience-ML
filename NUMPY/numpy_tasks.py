import numpy as np 
#task-1
one_arr=np.arange(10,21,2)
print(one_arr)
print("The shape is:",one_arr.shape) 
print('the size is:',one_arr.size)
print("the dimenstion is:",one_arr.ndim) 
#task-2 
two_arr=np.ones((3,3)) 
updated_two_arr=two_arr.astype(np.int32) 
print("the updated datatype is:",updated_two_arr.dtype) 
#task-3 
three_arr=np.eye(4) 
print(three_arr.shape) 
print(three_arr.size) 
print(three_arr.ndim) 
print(np.dtype) 
#task-4 
four_arr=np.array([[5, 10, 15], 
 [20, 25, 30]]
) 
print(four_arr-5) 
print(four_arr**3) 
print(four_arr+2) 
#task-5 
five_arr=np.arange(50,81,10) 
print(five_arr) 

#task-6  
six_arr=np.zeros((2,4)) 
print(np.sum(six_arr))
print(np.mean(six_arr)) 
print(np.var(six_arr)) 

#task-7 
seven_arr=np.array([7,7,7,7,7])  
print(np.std(seven_arr)) 

#task-8 
eight_arr = np.array([2, 4, 6, 8]) 
updated_eight_arr= eight_arr.astype(np.float64) 
print(updated_eight_arr.dtype) 
#task-9 
nine_arr=np.ones((3,3)) 
print(nine_arr**2)

#task-10 
ten_arr=np.array([[10, 20, 30], 
 [40, 50, 60]]
) 
print(ten_arr+5) 
print(np.min(ten_arr)) 
print(np.max(ten_arr)) 
print(ten_arr.shape) 
print(ten_arr.size) 
print(np.mean(ten_arr))