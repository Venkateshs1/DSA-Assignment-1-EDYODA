#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Q8. Write a program to check if all the brackets are closed in a given code snippet.
'''


# In[1]:


def areBracketsBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:

            stack.append(char)
        else:

            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    if stack:
        return False
    return True

if __name__ == "__main__":
    expr = "{()}[]"

    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")


# In[ ]:




