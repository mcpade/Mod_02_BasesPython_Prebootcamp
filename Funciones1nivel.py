#!/usr/bin/env python
# coding: utf-8

# In[1]:


def SumaTodos (limitTo, f):
    resultado = 0
    for i in range (limitTo+1):
        resultado += f(i)
    return resultado


# In[2]:


def normal (x):
    return x


# In[5]:


print (SumaTodos (100,normal))


# In[6]:


def cuadrado (x):
    return x*x


# In[8]:


print (SumaTodos (3,cuadrado))


# In[ ]:





# In[ ]:




