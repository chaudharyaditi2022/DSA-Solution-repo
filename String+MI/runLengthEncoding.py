#!/usr/bin/env python
# coding: utf-8

# In[230]:


def runLengthEncoder(string):
    count=1
    encodedString = ""
    for index in range(1,len(string)):
        if string[index] == string[index-1] and count<9:
            count += 1
        else:
            encodedString += str(count)+ string[index-1]
            count = 1
    encodedString += str(count)+ string[index-1]
    return encodedString

                
runLengthEncoder("AAAAAAAAAAAABBCDDDDQQQQQQQQQ****")
        

