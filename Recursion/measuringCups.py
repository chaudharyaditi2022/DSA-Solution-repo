#!/usr/bin/env python
# coding: utf-8

# In[4]:


def isVolumePossible(measuringCups, low, high, memoization):
    key = HashKey(low,high)
    if key in memoization:
        return memoization[key]
    
    if low<=0 and high<=0:
        canMeasure =False
    else:
        for cup in measuringCups:
            curLow, curHigh = cup
            if low<=curLow and high<=curHigh:
                canMeasure = True
                break
            newLow, newHigh = max(0,low-curLow), max(0,high-curHigh)
            canMeasure = isVolumePossible(measuringCups, newLow, newHigh, memoization)
            if canMeasure:
                break
        memoization[key] = canMeasure
        return canMeasure
    
def HashKey(low,high):
    return str(low)+":"+str(high)

def measurements(measuringCups, low, high):
    memoization = {}
    return isVolumePossible(measuringCups, low, high, memoization)
            
            
measurements([
    [200,210],
    [450,465],
    [800,850]],2100,2300)    
    


# In[ ]:




