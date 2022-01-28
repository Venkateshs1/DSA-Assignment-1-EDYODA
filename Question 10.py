#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q10. Write a program to find the smallest number using a stack.
'''


# In[1]:


First = []
num = int(input('How many numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    First.append(numbers)
    
print("Smallest number in the list is :  ", min(First))


# In[ ]:




