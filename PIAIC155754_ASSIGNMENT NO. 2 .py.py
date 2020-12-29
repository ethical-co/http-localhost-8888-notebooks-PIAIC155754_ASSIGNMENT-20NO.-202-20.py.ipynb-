#!/usr/bin/env python
# coding: utf-8

# # #import numpy as np
# 
# # Task no 1
# def function1():
#     # create 2d array from 1,12 range 
#     # dimension should be 6row 2 columns  
#     # and assign this array values in x values in x variable
#     # Hint: you can use arange and reshape numpy methods  
#     #x =  # Write your code here 
# 
#     print(x)
# 
#     return x
#     """
#     expected output:
#     [[ 1  2]
#     [ 3  4]
#     [ 5  6]
#     [ 7  8]
#     [ 9 10]
#     [11 12]]
#     """
# 

# In[18]:


import numpy as np


# In[46]:


x2 = np.arange(1,13).reshape((6,2))
x2.shape = (6,2)


# In[47]:


print (x2)


# # Task2
# def function2():
#     #create 3D array (3,3,3)
#     #must data type should have float64
#     #array value should be satart from 10 and end with 36 (both included)
#     # Hint: dtype, reshape 
#     
#     x = 
# 
# 
#     return x
#     """
#     Expected: out put
# array([[[10., 11., 12.],
#         [13., 14., 15.],
#         [16., 17., 18.]],
#        [[19., 20., 21.],
#         [22., 23., 24.],
#         [25., 26., 27.]],
#        [[28., 29., 30.],
#         [31., 32., 33.],
#         [34., 35., 36.]]])    
#     """
# 

# In[1]:


import numpy as np


# In[3]:


x2 = np.arange(1,13).reshape((6,2))


# In[4]:


print(x2)


# In[1]:


import numpy as np


# In[6]:


x_3d_array = np.array([[3,3,3]])


# In[8]:


print(x_3d_array)


# In[9]:


import numpy as np


# In[20]:


x.dtype


# In[22]:


import numpy as np


# In[24]:


x = np.arange(10,37).reshape((9,3))


# In[25]:


print(x)


# # task3
# def function3():
#     #extract those numbers from given array. those are must exist in 5,7 Table
#     #example [35,70,105,..]
#     a = np.arange(1, 100*10+1).reshape((100,10))
#     x = a[] #wrtie your code here
#     return x
#     """
#     Expected Output:
#      [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
#        490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
#        945, 980] 
#     """ 

# In[118]:


import numpy as np


# In[123]:


np.logical_and[(35,70,105)]


# In[ ]:





# In[ ]:





# # task4
# def function4():
#     #Swap columns 1 and 2 in the array arr.
#    
#     arr = np.arange(9).reshape(3,3)
#   
#     return #wrtie your code here
#     """
#     Expected Output:
#           array([[1, 0, 2],
#                 [4, 3, 5],
#                 [7, 6, 8]])
#     """ 

# In[75]:


import numpy as np


# In[77]:


arr = np.arange(9).reshape(3,3)


# In[116]:


arr = arr[[1,0,2]]


# In[117]:


print(arr)


# # task5
# def function5():
#     #Create a null vector of size 20 with 4 rows and 5 columns with numpy function
#    
#     z = #wrtie your code here
#   
#     return z
#     """
#     Expected Output:
#           array([[0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0]])

# In[49]:


import numpy as np


# In[103]:


my_array = np.zeros(20).reshape((4,5))


# In[105]:


print(my_array)


# In[109]:


my_array[:,[0, 2]] = my_array[:,[2, 0]]


# In[110]:


print("\nAfter swapping arrays:")


# In[111]:


print(my_array)


# In[ ]:





# # task6
# def function6():
#     # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
#    
#     arr = #wrtie your code here
#   
#     return arr

# In[2]:


import numpy as np


# In[15]:


arr = np.zeros(10)
arr[4] =10 
arr[8] =20


# In[16]:


print(arr)


# # task7
# def function7():
#     #  Create an array of zeros with the same shape and type as X. Dont use reshape method
#     x = np.arange(4, dtype=np.int64)
#   
#     return #write your code here
# 
#     """
#     Expected Output:
#           array([0, 0, 0, 0], dtype=int64)
#     """ 

# In[22]:


import numpy as np


# In[23]:


a = np.arange(4)


# In[30]:


a = a.reshape((1,4))


# In[31]:


a


# In[32]:


np.zeros_like(a)


# # task8
# def function8():
#     # Create a new array of 2x5 uints, filled with 6.
#     
#     x = #write your code here
#   
#     return x
# 
#      """
#      Expected Output:
#               array([[6, 6, 6, 6, 6],
#                      [6, 6, 6, 6, 6]], dtype=uint32)
#      """ 

# In[33]:


import numpy as np


# In[34]:


x = np.full((2,5), 6, dtype=np.uint)


# In[35]:


print(x)


# In[37]:


x.dtype


# # task9
# def function9():
#     # Create an array of 2, 4, 6, 8, ..., 100.
#     
#     a = # write your code here
#   
#     return a
# 
#      """
#      Expected Output:
#               array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,
#                     28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,
#                     54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,
#                     80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])
#      """ 

# In[38]:


import numpy as np


# In[50]:


arr = np.array([[2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100]])


# In[51]:


print(arr)


# # task10
# def function10():
#     # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
#     
#     arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
#     brr = np.array([1,2,3])
#     subt = # write your code here 
#   
#     return subt
# 
#      """
#      Expected Output:
#                array([[2 2 2]
#                       [2 2 2]
#                       [2 2 2]])
#      """ 

# In[49]:


import numpy as np


# In[55]:


a = np.array([[3,3,3],[4,4,4],[5,5,5]])
b = np.array([1,2,3])


# In[56]:


c = a - b[:,None]


# In[57]:


print(c)


# # task11
# def function11():
#     # Replace all odd numbers in arr with -1 without changing arr.
#     
#     arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#               array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
#      """ 
#     

# In[58]:


import numpy as np


# In[59]:


a = np.array([0,1,2,3,4,5,6,7,8,9])


# In[60]:


odd_values = (a%2 == 1)


# In[61]:


a[odd_values] = -1


# In[62]:


print(a)


# # task12
# def function12():
#     # Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
#     # HINT: use stacking concept
#     
#     arr = np.array([1,2,3])
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#               array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
#      """ 

# In[70]:


import numpy as np


# In[71]:


arr1 = np.repeat(arr,3)


# In[72]:


arr2 = np.tile(arr,3)


# In[73]:


ans = np.hstack((arr1,arr2))


# In[74]:


print(ans)


# # task13
# def function13():
#     # Set a condition which gets all items between 5 and 10 from arr.
#     
#     
#     arr = np.array([2, 6, 1, 9, 10, 3, 27])
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#               array([6, 9])
#      """ 

# In[124]:


import numpy as np


# In[135]:


z = np.arange(11)


# In[140]:


z = [(3 < z) & (z < 10)] 


# In[141]:


print(z)


# In[ ]:





# In[ ]:





# # task14
# def function14():
#     # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
#     # Hint use split method
#     
#     
#     arr = np.arange(10, 34, 1) #write reshape code
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#        [array([[10, 11, 12],[13, 14, 15]]), 
#         array([[16, 17, 18],[19, 20, 21]]), 
#         array([[22, 23, 24],[25, 26, 27]]), 
#         array([[28, 29, 30],[31, 32, 33]])]
#      """ 
#     

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(10,34,1).reshape((8,3))


# In[3]:


print(arr)


# In[6]:


np.split(arr,4)


# # task15
# def function15():
#     #Sort following NumPy array by the second column
#     
#     
#     arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#            array([[-4,  1,  7],
#                    [ 8,  2, -2],
#                    [ 6,  3,  9]])
#      """ 
#     

# In[7]:


import numpy as np


# In[8]:


arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])


# In[11]:


arr[np.lexsort(arr[:,::-2].T)]


# # task16
# def function16():
#     #Write a NumPy program to join a sequence of arrays along depth.
#     
#     
#     x = np.array([[1], [2], [3]])
#     y = np.array([[2], [3], [4]])
#     ans = #write your code here 
#   
#     return ans
# 
#      """
#      Expected Output:
#                 [[[1 2]]
#                  [[2 3]]
#                  [[3 4]]]
#      """ 
#     
#     

# In[12]:


import numpy as np


# In[13]:


x = np.array([[1], [2], [3]])


# In[14]:


y = np.array([[2], [3], [4]])


# In[15]:


np.dstack((x,y))


# # Task17
# def function17():
#     # replace numbers with "YES" if it divided by 3 and 5
#     # otherwise it will be replaced with "NO"
#     # Hint: np.where
#     arr = np.arange(1,10*10+1).reshape((10,10))
#     return           # Write Your Code HERE
# 
# #Excpected Out
# """
# array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
#        ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
#       dtype='<U3')
# """
# 

# In[16]:


import numpy as np


# In[17]:


arr = np.arange(1,10*10+1).reshape((10,10))


# In[18]:


print(arr)


# In[19]:


arr = np.where(arr)


# In[20]:


print(arr)


# # Task18
# def function18():
#     # count values of "students" are exist in "piaic"
#     piaic = np.arange(100)
#     students = np.array([5,20,50,200,301,7001])
#     x = # Write you code Here
#     return x
# 
#     #Expected output: 3

# In[21]:


import numpy as np


# In[22]:


piaic = np.arange(100)


# In[23]:


students = np.array([5,20,50,200,301,7001])


# In[27]:


x = np.count_nonzero(x)


# In[28]:


print(x)


# # Task19
# def function19():
#     #Create variable "X" from 1,25 (both are included) range values
#     #Convert "X" variable dimension into 5 rows and 5 columns
#     #Create one more variable "W" copy of "X" 
#     #Swap "W" row and column axis (like transpose)
#     # then create variable "b" with value equal to 5
#     # Now return output as "(X*W)+b:
# 
#     X =   # Write your code here
#     W =   # Write your code here 
#     b =   # Write your code here
#     output =    # Write your code here
#     return output
#     #expected output
#     """
#     array([[  6,  17,  38,  69, 110],
#        [ 17,  54, 101, 158, 225],
#        [ 38, 101, 174, 257, 350],
#        [ 69, 158, 257, 366, 485],
#        [110, 225, 350, 485, 630]])
#     """
# 

# In[37]:


import numpy as np


# In[41]:


arr = np.arange(26)


# In[42]:


print("An array from 1 to 25\n" + repr(arr) + "\n")


# In[44]:


import numpy as np


# In[45]:


arr = np.arange(25).reshape((5,5))


# In[46]:


print(arr)


# In[ ]:





# In[ ]:





# # Task20
# def function20():
#     #apply fuction "abc" on each value of Array "X"
#     x = np.arange(1,11)
#     def abc(x):
#         return x*2+3-2
# 
#     return #Write your Code here
# #Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])

# In[29]:


import numpy as np


# In[30]:


x = np.arange(1,11)


# In[32]:


def abc(x): return x*2+3-2


# In[40]:


abc(x)


# In[ ]:




