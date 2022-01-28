#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q4. Write a program to print the first non-repeated character from a string?
'''


# In[1]:


str1 = input(">>>" )
found = None

for i in str1:
    if (str1.count(i) == 1):
        print("the first founded non-repeating string variable is: ",i)
        found = True
        break

if (found == False):
    print("there is non repeating char in str1")


# In[ ]:




