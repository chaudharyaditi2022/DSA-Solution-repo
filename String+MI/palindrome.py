#!/usr/bin/env python
# coding: utf-8

# In[186]:


def isPalindrome(string):
    length = len(string)
    for i in range(length//2):
        if string[i] != string[length - i - 1]:
            return False
    return True


# In[ ]:




