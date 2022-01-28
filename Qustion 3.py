#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q3. Write a program to check if two strings are a rotation of each other?
'''


# In[4]:


def is_rotation(string1,string2):
    if len(string1) != len(string2):
        return False
    s = string1 + string1
    return string2 in s

string1 = "ABCDEFG"
string2 = "DEFGABC"
if is_rotation(string1,string2):
    print("the string is rotating of each other")
else:
    print("the string is not rotating of each other")


# In[ ]:




