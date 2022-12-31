#-*- coding: utf-8 -*-
"""
@author:Bengali.AI
"""
from __future__ import print_function
#-------------------------------------------
# globals
#-------------------------------------------
from .base import BaseNormalizer

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
                language                        :   language identifier from 'devanagari', 'gujarati', 'odiya', 'tamil', 'panjabi', 'malayalam','sylhetinagri'
                allow_english                   :   allow english letters numbers and punctuations [default:False]
                
        '''        
        super(IndicNormalizer,self).__init__(language=language,allow_english=allow_english)    
            
    
  
    def cleanInvalidUnicodes(self):
        # clean starts
        while self.checkDecomp() and self.decomp[0] in self.lang.invalid_starts:
            self.decomp=self.decomp[1:]         
        # clean endings
        
        # if the last one is a connector (allow halant ending)
        try:
            if self.decomp[-1] == self.lang.connector: 
                self.decomp=self.decomp[:-1]
                add_con=True
            else:
                add_con=False
        except Exception as e:
            add_con=False

            
        while self.checkDecomp() and self.decomp[-1] == self.lang.connector:
            self.decomp=self.decomp[:-1]
        
        # (allow halant ending)
        if add_con:self.decomp.append(self.lang.connector)
        
        if self.checkDecomp():
            # clean invalid unicodes
            for idx,d in enumerate(self.decomp):
                if d not in self.valid:
                    self.decomp[idx]=None 