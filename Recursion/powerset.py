#!/usr/bin/env python
# coding: utf-8

# In[14]:


def powerset(arr):
    pSet =[]
    for i in range(0,2**len(arr)):
        s = []
        for j in range(0,len(arr)):
            if (i & 1<<j):
                s.append(arr[j])
                #print(arr[j], end=" ")
        pSet.append(s)
    return pSet

print(powerset([1,2,3]))


# In[ ]:




