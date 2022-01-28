#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q2. Write a program to reverse an array in place? 
In place means you cannot create a new array. You have to update the original array.
'''


# In[5]:


def ReverseArray(Array, first, last):
    while first < last:
        Array[first],Array[last] = Array[last],Array[first]
        
        first += 1
        last -= 1
                
Array = [1,9,34,134,45,23,100,190]
print(Array)
ReverseArray(Array, 0, 7)
print("After Reversing, Updated Array")
print(Array)


# In[ ]:




