""" 
   topics-3
   .isnan(array) -> tells us if the value of nan is present in the array or not 
   .nan_to_num(array,nan=value,posinf=value,neginf=value)->This function replaces the nan values to the given "value"{also used for infinity values}
   .isinf(array) -> checks if the value of infinity is present in the array or not
"""

import numpy as np 
# isnan() , nan_to_num () , isinf() 
a=np.array([1,2,3,np.nan,5,np.inf,-np.inf]) 

# np.isnan(array) <-- used to get missing values in the array 
# note: we can't compare NaN values directly in numpy! 
print(np.isnan(a)) 

# np.nan_to_num(array,nan=value)  <-- here, nan=value is the value by which the nan values will get replaced 
print(np.nan_to_num(a,nan=69)) 

# np.isinf(array) <-- checks for infinity value

print(np.isinf(a)) 

#to convert infinity to some numbere use posinf and neginf to set them with nan_to_num() function 
non_infinity=np.nan_to_num(a,posinf=1000,neginf=-100)
print(non_infinity)