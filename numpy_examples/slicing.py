
# coding: utf-8

# # Play with slicing arrays of different dimensions

# In[1]:


import numpy as np


# #### Create a 1D array with elements from 0 up to but not including 12

# In[2]:


data_1D = np.arange(12)
print(data_1D)


# ## 2D arrays

# #### We want to reshape this into a 3x4 array. Will this work?

# In[3]:


shape = (3,4)
print("Will array data_1D with size {} reshape to {}?\n{}"
      .format(data_1D.size, shape, data_1D.size == shape[0]*shape[1])
     )


# In[4]:


data_2D = np.reshape(data_1D, shape)
print(data_2D)


# #### Let's play with 2D slicing

# In[5]:


print("Slicing column 1:")
print(data_2D[:,1])


# In[6]:


print("Slicing the last row:")
print(data_2D[-1,:])


# In[7]:


print("Ignore the outer rows and columns:")
print(data_2D[1:-1,1:-1])


# ## 3D arrays

# #### Can we reshape data_1D to a 2x2x3 3D array?

# In[8]:


shape = (2,2,3)
print("Will array data_1D with size {} reshape to {}?\n{}"
      .format(data_1D.size, shape, 
              data_1D.size == shape[0]*shape[1]*shape[2])
     )


# In[9]:


data_3D = np.reshape(data_1D, shape)
print(data_3D)


# #### Now let's try 3D slicing

# In[10]:


print("Access the first slab:")
print(data_3D[0,:,:])


# In[11]:


print("Get the last column of each slab:")
print(data_3D[:,:,-1])


# In[12]:


print("Isolate the first row of the second slab:")
print(data_3D[1,0,:])

