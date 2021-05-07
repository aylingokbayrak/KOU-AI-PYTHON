#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Kullanıcıdan alacağınız bir sayının çift sayı olup olmadığını kontrol edip ekrana sayı
#çiftse çift, çift değilse tek yazdırın. (Kullanıcıdan sayı almak için input fonksiyonuna
#bakabilirsiniz :))


# In[3]:


sayi=int(input("sayi: "))
if sayi%2==0:
    print('{} sayısı çift sayıdır'.format(sayi))
else:
    print('{} sayısı tek sayıdır'.format(sayi))
    


# In[ ]:




