#!/usr/bin/env python
# coding: utf-8

# In[10]:


def phMnemonics(phoneNumber):
    current = ["0"] * len(phoneNumber)
    found = []
    findMnemonics(0, phoneNumber, current, mnemonicsFound)
    
    
def findMnemonics(start, phoneNumber, current, found):
    if start == len(phoneNumber):
        mnemonic = ""+current
        found.append(mnemonic)
    else:
        digit = phoneNumber[start]
        alphabets = DIGIT_ALPHA[digit]
        for alphabet in alphabets:
            current[start] = alphabet
            findMnemonics(start+1, phoneNumber, current, found)
            

DIGIT_ALPHA = {
    "0": ["0"],
    "1": ["1"],
    "2": ["a","b","c"],
    "3": ["d","e","f"],
    "4": ["g","h","i"],
    "5": ["j","k","l"],
    "6": ["m","n","o"],
    "7": ["p","q","r","s"],
    "8": ["t","u","v"],
    "9": ["w","x","y","z"],
}         


# In[ ]:




