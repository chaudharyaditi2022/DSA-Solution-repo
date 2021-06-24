#!/usr/bin/env python
# coding: utf-8

# In[40]:



def arrangeAlphabetically(string, anagrams):
    sorted_string = "".join(sorted(string))
    if sorted_string not in anagrams.keys():
        anagrams[sorted_string] = []
    anagrams[sorted_string].append(string)
        
        
    
def groupanagrams(words):
    anagrams = {}
    for word in words:
        arrangeAlphabetically(word,anagrams)
    
    anagrams_groups = list(anagrams.values())
    return(anagrams_groups)
    


# In[41]:


words = ["yo", "act", "flop", "oy", "tac", "floo", "plof"]
groupanagrams(words)

