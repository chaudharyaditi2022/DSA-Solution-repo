#!/usr/bin/env python
# coding: utf-8

# In[57]:


def matchPatternForXY(string, pattern, x, y):
    start,end = 0,0
    x_str = ""
    y_str = ""
    for char in pattern:
        if char == 'x':
            end += x
            match_str = string[start:end]
            if x_str == "":
                x_str = match_str
            if x_str != match_str:
                return False,["",""]
            start += x
        
        elif char == 'y':
            end += y
            match_str = string[start:end]
            if y_str == "":
                y_str = match_str
            if y_str != match_str:
                return False,["",""]
            start += y
            
    return True,[x_str,y_str]
    


# In[58]:


def matchPattern(string, pattern):
    countX, countY = 0,0
    for i in pattern:
        if i == 'x':
            countX += 1
        else:
            countY += 1
            
    #Now countX * len(x) + countY*len(y) = len(string)
    #Find possible lengths of x and y
    patternPossible = False
    strlen = len(string)
    x,y = 1, 0
    while not patternPossible and countX*x <= strlen:
        y = (strlen - (countX*x))
        if y % countY == 0:
            y //= countY
            patternPossible, result = matchPatternForXY(string, pattern, x, y)
            if patternPossible:
                return result
        x += 1
            
    return patternPossible
    


# In[64]:


matchPattern("gogopowerrangergogopowerranger", "xyxy")


# In[ ]:




