#!/usr/bin/env python
# coding: utf-8

# In[103]:


def reverseWords(string):
    string += " "
    length = len(string)
    start = 0
    resultantString = ""
    for index in range(length):
        if string[index] == " ":
            word = string[start:index]
            resultantString = word + " " +resultantString
            start = index+1
    
    return resultantString[:-1]


# In[105]:


reverseWords("Demo is the best")


# In[ ]:





# In[ ]:




