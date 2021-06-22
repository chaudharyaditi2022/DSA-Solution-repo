#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def checkIfInterwovenString(a,b,resultant_string):
    current_char = 0
    cur_a =0
    cur_b = 0
    formed_string=""
    while ((cur_a<len(a) or cur_b<len(b)) and current_char<len(resultant_string)):
        #print("{} {} {}".format(resultant_string[current_char], a[cur_a],b[cur_b]))
        if cur_a < len(a):
            if resultant_string[current_char] == a[cur_a]:
                formed_string += a[cur_a]
                cur_a += 1
        if cur_b<len(b):
            if  resultant_string[current_char] == b[cur_b]:
                formed_string += b[cur_b]
                cur_b += 1
        current_char += 1
        
    print(formed_string)
    if formed_string == resultant_string:
        return True
    else:
        return False
        
    
    


# In[ ]:


one ="abc"
two = "123"
result = "abc123"
print(checkIfInterwovenString(one,two,result))


# In[ ]:




