#!/usr/bin/env python
# coding: utf-8

# In[30]:


def longestSubstringWithNoDuplication(string):
    hashtable = {}
    start = 0
    max_len = 0
    final_start = 0
    final_end = 0
    for index,char in enumerate(string):
        if char not in hashtable.keys():
            hashtable[char] = index
            #print(char,index)
            continue
            
        if hashtable[char] < start:
            hashtable[char] = index
        else:
            #print(char,start,index)
            substrlen = index-start
            if substrlen > max_len:
                final_start =start
                final_end = index
            start = hashtable[char] + 1
            hashtable[char] = index
                
    return string[final_start:final_end]
                
            
    


# In[31]:


longestSubstringWithNoDuplication("clementisacap")


# In[ ]:




