#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
'''


# In[2]:


def sum_pairs(array , num , sum):
    for i in range(num):
        for j in range(i+1 , num):
            if array[i] + array[j] == sum:
                print("(",array[i],",",array[j],")",sep = "")
                
                
array = [5,6,4,5,7,3,8,2,9,1]
num = len(array)
sum = 11


sum_pairs(array, num, sum)


# In[ ]:




