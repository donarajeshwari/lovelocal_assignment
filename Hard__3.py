#!/usr/bin/env python
# coding: utf-8

# In[8]:


n=int(input())
count=0
for i in range(0,n+1):
    
    values=list(str(i))
    
    values=[int(k) for k in values]
    
    
    for j in values:
        if j==1:
            count+=1;
            
print(count)



# In[ ]:




