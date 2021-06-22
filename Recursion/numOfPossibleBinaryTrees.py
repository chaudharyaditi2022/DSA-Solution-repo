#!/usr/bin/env python
# coding: utf-8

# In[23]:


def factorial(number):
    if number == 0 or number==1:
        return 1
    return factorial(number-1)*number

#Number of Binary Trees with n nodes = (2*n)!/(n! * (n+1)!) which is also called catlan number Cn
def numberOfBinaryTree(nodes):
    if nodes==0 or nodes == 1:
        return 1
    factN = factorial(nodes)
    return factorial(2*nodes)//(factN*factN*(nodes+1)) 
    


# In[25]:


numberOfBinaryTree(2)


# In[ ]:




