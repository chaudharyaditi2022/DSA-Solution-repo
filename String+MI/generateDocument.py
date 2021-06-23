#!/usr/bin/env python
# coding: utf-8

# In[251]:


def countAlphabets(string):
    alphabet_count = {}
    for ch in string:
        if ch not in alphabet_count.keys():
            alphabet_count[ch] = 1
        else:
            alphabet_count[ch] += 1
        
    return alphabet_count

        
def generateDocument(string,document):
    alphabet_count = countAlphabets(string)
    for ch in document:
        if ch not in alphabet_count.keys():
            return False
        elif alphabet_count[ch] <= 0:
            return False
        else:
            alphabet_count[ch] -= 1
    return True

generateDocument("a bc*abc", "aa*bbcc ")
    
    

