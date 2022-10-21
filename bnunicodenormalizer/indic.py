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
                language                        :   language identifier from 'devanagari', 'gujarati', 'odiya', 'tamil', 'panjabi', 'malayalam'
                allow_english                   :   allow english letters numbers and punctuations [default:False]
                
        '''        
        super(IndicNormalizer,self).__init__(language=language,allow_english=allow_english)    
            
    
  
