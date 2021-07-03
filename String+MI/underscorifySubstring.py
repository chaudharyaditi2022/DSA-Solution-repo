#!/usr/bin/env python
# coding: utf-8

# In[115]:


def UnderscorifySubstring(string, substring):
    substrlen = len(substring)
    locations = []
    for start,char in enumerate(string):
        if string[start:start+substrlen] == substring:
            if len(locations)!= 0 and (locations[-1][1] == start or locations[-1][1] == start+1):
                locations[-1][1] = start+substrlen
            else:
                locations.append([start,start+substrlen])
    
    index = 0
    finalString = ""
    for start,end in locations:
        if start == index:
            finalString += "_"+string[start:end]+"_"
            index = end
        else:
            finalString += string[index:start] + "_"+string[start:end]+"_"
            index = end
    
    finalString += string[index:len(string)]
    
    print(finalString)
    
    


# In[116]:


UnderscorifySubstring("testthis is a testtest to see if testestest it works", "test")

