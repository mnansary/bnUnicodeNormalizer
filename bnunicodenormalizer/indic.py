#-*- coding: utf-8 -*-
"""
@author:Bengali.AI
"""
from __future__ import print_function
#-------------------------------------------
# globals
#-------------------------------------------
from .base import BaseNormalizer,languages

#-------------------------------------------
# cleaner class
#-------------------------------------------

class IndicNormalizer(BaseNormalizer):
    def __init__(self,
                language,
                allow_english=False):

        '''
            initialize a normalizer
            args:
                language                        :   language identifier
                allow_english                   :   allow english letters numbers and punctuations [default:False]
                
        '''        
        super(IndicNormalizer,self).__init__(language=language,allow_english=allow_english)
        self.complex_roots=languages[language].complex_roots

        #-------------------------------------------------extended ops----------------------
        # complex root cleanup 
        self.decomp_level_ops["ComplexRootNormalization"]          =       self.convertComplexRoots

        
#-------------------------unicode ops-----------------------------------------------------------------------------    
    
    def checkComplexRoot(self,root):
        formed=[]
        formed_idx=[]
        for i,c in enumerate(root):
            if c != self.lang.connector and i not in formed_idx:
                r=c
                if i==len(root)-1:
                    formed.append(r)
                    continue
                for j in range(i+2,len(root),2):
                
                    d=root[j]
                    k=r+self.lang.connector+d
                    #if k==
                    if k not in self.complex_roots:
                        formed.append(r)
                        break
                    else:
                        if j!=len(root)-1:
                            r=k
                            formed_idx.append(j)
                        else:
                            r=k
                            formed_idx.append(j)
                            formed.append(k)
        return "".join(formed)

        
    
    def convertComplexRoots(self):
        self.fixNoSpaceChar()
        self.decomp=[x for x in self.decomp if x is not None] 
        self.constructComplexDecomp()
        for idx,d in enumerate(self.decomp):
            if d not in self.complex_roots and self.lang.connector in d:
                self.decomp[idx]=self.checkComplexRoot(d) 
        


#-------------------------unicode ops-----------------------------------------------------------------------------               
    
            
    
  
