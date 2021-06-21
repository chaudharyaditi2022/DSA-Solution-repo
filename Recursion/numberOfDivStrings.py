#!/usr/bin/env python
# coding: utf-8

# In[10]:


def generateValidString(openingTags , closingTags, string, result):
    if openingTags == closingTags == 0:
        result.append(string)
    if openingTags <= closingTags:
        if openingTags != 0:
            generateValidString(openingTags-1,closingTags,string+"<div>",result)
            generateValidString(openingTags,closingTags-1,string+"</div>",result)
        else:
            generateValidString(openingTags,closingTags-1,string+"</div>",result)
    elif openingTags > closingTags:
        return
    


# In[11]:


result=[]
generateValidString(3,3,"",result)
print(result)


# In[ ]:




