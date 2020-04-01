#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


random.random()


# In[3]:


k=random.randint(1,100)
k


# In[4]:


def get_random_numbers(n=10,min=-5,max=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min,max))
    return numbers
get_random_numbers()


# In[5]:


my_list=get_random_numbers(15,-4,4)
my_list


# In[6]:


my_list


# In[7]:


sorted(my_list)


# In[8]:


def my_frekans_dict(list):
    frekans_dict={} 
    for item in list:
        if(item in frekans_dict):
            frekans_dict[item]=frekans_dict[item]+1
        else:
            frekans_dict[item]=1
    return frekans_dict


# In[9]:


my_frekans_dict(my_list)


# In[10]:


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


# In[11]:


my_frekans_with_digits(my_list)


# In[12]:


my_list=[3,3,5,1,55,6,3,5,8,6,5,1,1,0,7,0]
res_1=my_frekans_dict(my_list)
res_2=my_frekans_with_digits(my_list)
res_1,res_2


# In[13]:


my_list_1=get_random_numbers(10)
my_hist_d=my_frekans_dict(my_list_1)
my_hist_d


# In[15]:


my_hist_1=my_frekans_with_digits(my_list_1)
my_hist_1


# In[23]:


def my_mode_with_dict(my_hist_d):
    
    frekans_max=-1 #hafıza amaçlı döngüde karşılaştırılacak değer
    mode=-1
    for key in my_hist_d.keys():
       # print(key,my_hist_d[key])
        if my_hist_d[key]>frekans_max:
            frekans_max=my_hist_d[key]
            mode=key
    return mode,frekans_max


# In[24]:


my_mode_with_dict(my_hist_d)


# In[ ]:




