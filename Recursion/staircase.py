#!/usr/bin/env python
# coding: utf-8

# In[7]:


def countways(height, maxsteps):
    if height <= 1:
        return 1
    count = 0
    for h in range(1, min(maxsteps,height)+1):
        count += countways(height - h, maxsteps)
    return count

def staircase(height, maxsteps):
    return countways(height, maxsteps)
            
    


# In[8]:


staircase(3,2)


# In[ ]:




