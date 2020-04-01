#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


random.random()


# In[4]:


k=random.randint(1,100)
k


# In[8]:


def get_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers
get_random_numbers()
    


# In[9]:


my_list=get_random_numbers(15,-4,4)
my_list


# In[10]:


my_list


# In[11]:


sorted(my_list)


# In[13]:


def my_frekans_dict(list):
    frekans_dict={} 
    for item in list:
        if(item in frekans_dict):
            frekans_dict[item]=frekans_dict[item]+1
        else:
            frekans_dict[item]=1
    return frekans_dict
        
    


# In[14]:


my_frekans_dict(my_list)


# In[15]:


def my_frekans_with_digits(list_1):
    frekans_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frekans_list)):
            if(list_1[i]==frekans_list[j][0]):
                frekans_list[j][1]=frekans_list[j][1]+1
                s=True
        if(s==False):
            frekans_list.append([list_1[i],1])
    return frekans_list
        
        
    


# In[16]:


my_frekans_with_digits(my_list)


# In[17]:


my_list=[3,3,5,1,55,6,3,5,8,6,5,1,1,0,7,0]
res_1=my_frekans_dict(my_list)
res_2=my_frekans_with_digits(my_list)
res_1,res_2


# In[ ]:




