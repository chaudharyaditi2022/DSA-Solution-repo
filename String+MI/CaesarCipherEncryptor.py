#!/usr/bin/env python
# coding: utf-8

# In[211]:


def shiftAlphabet(string, k):
    newString = ""
    for alphabet in string:
        ascii_value = ord(alphabet)+k 
        if ascii_value > 122:
            ch = chr(97+(ascii_value-123))
        else:
            ch = chr(ascii_value )
        newString += ch
    return newString
        
shiftAlphabet("xyza",3)
        

