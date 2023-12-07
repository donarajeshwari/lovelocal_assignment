#!/usr/bin/env python
# coding: utf-8

# In[2]:


string=input()
str1=string
ans=0
count=0
for i in str1:
    if i==" ":
        ans=count
        count=0
    else:
        count+=1
print(count)


# In[ ]:




