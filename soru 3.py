#!/usr/bin/env python
# coding: utf-8

# In[37]:


def temiz_veri():
    ilk_string ="Ah5me4t"
    ikinci_string = "M9eHm4eT"
    ucuncu_string ="Ha3K5a1n"
    
    ilk_string=[*ilk_string]
    ikinci_string=[*ikinci_string]
    ucuncu_string=[*ucuncu_string]
    
    x=['-']
    
    liste=ilk_string + x + ikinci_string + x + ucuncu_string
    print(liste)
    
    sayilar=['0','1','2','3','4','5','6','7','8','9']
    
    for harf in liste:
        
        for rakam in sayilar:
            
            if harf==str(rakam):
                liste.remove(harf)
            else:
                continue
                
    Birlesmis_deger=" ".join(liste)
    
    return Birlesmis_deger
            
print(temiz_veri())


# In[ ]:




