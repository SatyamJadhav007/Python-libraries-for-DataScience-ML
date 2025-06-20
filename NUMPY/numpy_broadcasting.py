"""  
    topics-1
    broadcasting -> operations on arrays with again some conditions(equal in shape->one dimension)
"""

import numpy as np 

arr=np.array([44,66,433]) 
discount=10 

discounted_arr=arr-(arr*discount/100) 
print(discounted_arr) 

#rule 1: matching dimensions(shape) 
#rule 2: expanding single elements 
#for ex, if => [1,2,3] + 10  <<<-- "10" is added to all the elements of the array 
#rule 3: incompatible dimensions(true) -> then throw new Error("Shapes must match!")
#note: atleast one dimension should be equal for operations on array 
matrix=np.array( [[1,2,3],[4,5,6]])  

vector=np.array([11,22,33]) 

result=matrix + vector 
print(result)