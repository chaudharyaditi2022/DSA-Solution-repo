#!/usr/bin/env python
# coding: utf-8

# In[278]:


def longestPalindromicSubstring(a,b,lena,lenb):
    if lena <= 0 or lenb <=0:
        return ""
    
    if a[lena] == b[lenb]:
        return a[lena]+longestPalindromicSubstring(a,b,lena-1,lenb-1)
    else:
        x = longestPalindromicSubstring(a,b,lena-1,lenb)
        y = longestPalindromicSubstring(a,b,lena,lenb-1)
        if len(x) > len(y):
            return x
        else:
            return y
    


# In[279]:


a = "abaxyzzyxf"
n = len(a)
longestPalindromicSubstring(a, a[::-1], n-1, n-1)


# In[ ]:




