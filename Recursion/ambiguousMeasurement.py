#!/usr/bin/env python
# coding: utf-8

# In[11]:


def measurementAvailable(measuringCups, low, high):
    return isVolumePossible(measuringCups, low, high, 0, 0, None)


def isVolumePossible(measuringCups, low, high, currentLow, currentHigh,canMeasure):
    #print("{} {}".format(currentHigh,currentLow))
    if currentLow>=high or currentHigh>high:
        canMeasure=False
    if currentLow>=low and currentHigh<=high:
        canMeasure=True
    for cup in measuringCups:
        cupLow, cupHigh = cup
        if cupLow+currentLow < high and cupHigh+currentHigh<=high:
            canMeasure = isVolumePossible(measuringCups,low,high,currentLow+cupLow,currentHigh+cupHigh,canMeasure)
        if canMeasure:
            break
    return canMeasure
        
            
            


# In[12]:


cups = [
    [200,210],
    [450,465],
    [800,850]
]
low = 2100
high = 2300
measurementAvailable(cups, low, high)


# In[ ]:




