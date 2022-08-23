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

class Normalizer(BaseNormalizer):
    def __init__(self,
                allow_english=False,
                keep_legacy_symbols=False,
                legacy_maps=None):

        '''
            initialize a normalizer
            args:
                allow_english                   :   allow english letters numbers and punctuations [default:False]
                keep_legacy_symbols             :   legacy symbols will be considered as valid unicodes[default:False]
                                                    '৺':Isshar 
                                                    '৻':Ganda
                                                    'ঀ':Anji (not '৭')
                                                    'ঌ':li
                                                    'ৡ':dirgho li
                                                    'ঽ':Avagraha
                                                    'ৠ':Vocalic Rr (not 'ঋ')
                                                    '৲':rupi
                                                    '৴':currency numerator 1
                                                    '৵':currency numerator 2
                                                    '৶':currency numerator 3
                                                    '৷':currency numerator 4
                                                    '৸':currency numerator one less than the denominator
                                                    '৹':Currency Denominator Sixteen
                legacy_maps                     :   a dictionay for changing legacy symbols into a more used  unicode 
                                                    a default legacy map is included in the language class as well,
                                                    legacy_maps={'ঀ':'৭',
                                                                'ঌ':'৯',
                                                                'ৡ':'৯',
                                                                '৵':'৯',
                                                                '৻':'ৎ',
                                                                'ৠ':'ঋ',
                                                                'ঽ':'ই'}
                                            
                                                    pass-   
                                                    * legacy_maps=None; for keeping the legacy symbols as they are
                                                    * legacy_maps="default"; for using the default legacy map
                                                    * legacy_maps=custom dictionary(type-dict) ; which will map your desired legacy symbol to any of symbol you want
                                                        * the keys in the custiom dicts must belong to any of the legacy symbols
                                                        * the values in the custiom dicts must belong to either vowels,consonants,numbers or diacritics  
                                                        vowels         =   ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']
                                                        consonants     =   ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ','জ', 'ঝ', 'ঞ', 
                                                                            'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 
                                                                            'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 
                                                                            'স', 'হ','ড়', 'ঢ়', 'য়','ৎ']    
                                                        numbers        =    ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
                                                        vowel_diacritics       =   ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ']
                                                        consonant_diacritics   =   ['ঁ', 'ং', 'ঃ']
    
                                                        > for example you may want to map 'ঽ':Avagraha as 'হ' based on visual similiarity 
                                                            (default:'ই')

                ** legacy contions: keep_legacy_symbols and legacy_maps operates as follows 
                    case-1) keep_legacy_symbols=True and legacy_maps=None
                        : all legacy symbols will be considered valid unicodes. None of them will be changed
                    case-2) keep_legacy_symbols=True and legacy_maps=valid dictionary example:{'ঀ':'ক'}
                        : all legacy symbols will be considered valid unicodes. Only 'ঀ' will be changed to 'ক' , others will be untouched
                    case-3) keep_legacy_symbols=False and legacy_maps=None
                        : all legacy symbols will be removed
                    case-4) keep_legacy_symbols=False and legacy_maps=valid dictionary example:{'ঽ':'ই','ৠ':'ঋ'}
                        : 'ঽ' will be changed to 'ই' and 'ৠ' will be changed to 'ঋ'. All other legacy symbols will be removed
        '''
        if legacy_maps=="default":
            legacy_maps=languages["bangla"].legacy_maps

        self.complex_roots=languages["bangla"].complex_roots

        super(Normalizer,self).__init__(language="bangla",
                                        allow_english=allow_english,
                                        keep_legacy_symbols=keep_legacy_symbols,
                                        legacy_maps=legacy_maps)
        #-------------------------------------------------extended ops----------------------
        # assemese 
        self.assamese_map={'ৰ':'র','ৱ':'ব'}
        self.word_level_ops["AssameseReplacement"]      =       self.replaceAssamese
        
        # to+hosonto case
        '''

            case-1:     if 'ত'+hosonto is followed by anything other than a consonant the word is an invalid word

            case-2:     The ত্‍ symbol which should be replaced by a 'ৎ' occurs for all consonants except:ত,থ,ন,ব,ম,য,র
                        # code to verify this manually 
                        for c in self.consonants:
                            print('ত'+ self.lang.connector+c)
 
        '''
        
        self.valid_consonants_after_to_and_hosonto      =       ['ত','থ','ন','ব','ম','য','র'] 
        self.decomp_level_ops["base_bangla_compose"]    =       self.baseCompose
        self.decomp_level_ops["ToAndHosontoNormalize"]  =       self.normalizeToandHosonto

        # invalid folas 
        self.decomp_level_ops["NormalizeConjunctsDiacritics"]      =       self.cleanInvalidConjunctDiacritics

        # complex root cleanup 
        self.decomp_level_ops["ComplexRootNormalization"]          =       self.convertComplexRoots

        
#-------------------------word ops----------------------------------------------------------------------------- 
    def replaceAssamese(self):
        self.replaceMaps(self.assamese_map)
                        
#-------------------------unicode ops-----------------------------------------------------------------------------    
    def cleanConsonantDiacritics(self):
        # consonant diacritics
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d in self.lang.consonant_diacritics and self.decomp[idx+1] in self.lang.consonant_diacritics:
                    # if they are same delete the current one
                    if d==self.decomp[idx+1]:
                        self.decomp[idx]=None
                    elif d in ['ং', 'ঃ'] and self.decomp[idx+1]=='ঁ':
                        self.swapIdxs(idx,idx+1)
                    elif d=='ং' and self.decomp[idx+1]== 'ঃ':
                        self.decomp[idx+1]=None
                    elif d=='ঃ' and self.decomp[idx+1]== 'ং':
                        self.decomp[idx+1]=None
    
    def fixNoSpaceChar(self):
        # replace
        for idx,d in enumerate(self.decomp):
            if idx==0 and self.decomp[idx] in ["\u200c","\u200d"]:
                self.decomp[idx]=None
            else:
                if self.decomp[idx]=="\u200c":
                    self.decomp[idx]="\u200d"   
        self.decomp=[x for x in self.decomp if x is not None] 
        # strict
        for idx,d in enumerate(self.decomp):
            if idx>0:
                if self.decomp[idx]=="\u200d":
                    # last one
                    if idx==len(self.decomp)-1:
                        self.decomp[idx]=None 
                    # if previous one is a connector
                    if self.decomp[idx-1]==self.lang.connector:
                        self.decomp[idx]=None
                        self.decomp[idx-1]=None
                    # if previous one is not 'র'
                    elif self.decomp[idx-1]!='র':
                        self.decomp[idx]=None
                    else:
                        # if prev='র' and the prev-1 is not a connector
                        if idx>1 and self.decomp[idx-2]==self.lang.connector:
                            self.decomp[idx]=None
                        # if the next is not a connector
                        elif idx<len(self.decomp)-1 and self.decomp[idx+1]!=self.lang.connector:
                            self.decomp[idx]=None
                        # if the next one to connector is not "য"
                        elif idx<len(self.decomp)-2 and self.decomp[idx+2]!="য" and self.decomp[idx+1]!=self.lang.connector:
                            self.decomp[idx]=None
                        else:
                            # the actual allowed case
                            self.decomp[idx-1]+=self.decomp[idx]
                            self.decomp[idx]=None
                
             
##------------------------------------------------------------------------------------------------------    
    def cleanInvalidConnector(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d==self.lang.connector and self.decomp[idx+1]!="য" and self.decomp[idx-1] not in ['অ','এ']: # exception
                    if self.decomp[idx-1] in self.lang.invalid_connectors  or self.decomp[idx+1] in self.lang.invalid_connectors:
                        self.decomp[idx]=None 
                if d==self.lang.connector and self.decomp[idx-1]=="য" and self.decomp[idx+1]!="য":
                    self.decomp[idx]=None
                if d==self.lang.connector and self.decomp[idx-1]=="ব" and self.decomp[idx+1] not in ['জ', 'দ', 'ধ', 'ব', 'য', 'র', 'ল']:
                    self.decomp[idx]=None

        # handle exception
        self.decomp=[d for d in self.decomp if d is not None]
        word="".join(self.decomp)
        
        if "এ্যা" in word:
            word=word.replace("এ্যা","অ্যা")
        if 'অ্য' in word:
            word=word.replace('অ্য',"অ্যা")
        self.decomp=[ch for ch in word]
    
    def convertToAndHosonto(self):
        '''
            normalizes to+hosonto for ['ত','থ','ন','ব','ম','য','র'] 
            # Example-1:
            (a)বুত্পত্তি==(b)বুৎপত্তি-->False
                (a) breaks as ['ব', 'ু', 'ত', '্', 'প', 'ত', '্', 'ত', 'ি']
                (b) breaks as ['ব', 'ু', 'ৎ', 'প', 'ত', '্', 'ত', 'ি']
            # Example-2:
            (a)উত্স==(b)উৎস-->False
                (a) breaks as ['উ', 'ত', '্', 'স']
                (b) breaks as ['উ', 'ৎ', 'স']
        '''
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                # to + hosonto
                if d=='ত' and self.decomp[idx+1]== self.lang.connector:
                    # for single case
                    if  idx<len(self.decomp)-2: 
                        if self.decomp[idx+2] not in self.valid_consonants_after_to_and_hosonto:
                            # replace
                            self.decomp[idx]='ৎ'
                            # delete
                            self.decomp[idx+1]=None
                            
                        else: 
                            # valid replacement for to+hos double case
                            if idx<len(self.decomp)-3: 
                                if self.decomp[idx+2]=='ত' and self.decomp[idx+3]== self.lang.connector:
                                    if idx<len(self.decomp)-4: 
                                        if self.decomp[idx+4] not in  ['ব','য','র']:
                                            # if the next charecter after the double to+hos+to+hos is with in ['ত','থ','ন','ম'] 
                                            # replace
                                            self.decomp[idx]='ৎ'
                                            # delete
                                            self.decomp[idx+1]=None
                                    if idx<len(self.decomp)-4: 
                                        if self.decomp[idx+4]=='র':
                                            # delete
                                            self.decomp[idx+3]=None
        
    def swapToAndHosontoDiacritics(self):
        '''
            puts diacritics in right place
        '''
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d=='ৎ' and self.decomp[idx+1] in self.lang.diacritics:
                    self.swapIdxs(idx,idx+1)
###------------------------------------------------------------------------------------------------------               
    def normalizeToandHosonto(self):
        self.safeop(self.convertToAndHosonto)
        self.safeop(self.swapToAndHosontoDiacritics)
        self.baseCompose()
        
###------------------------------------------------------------------------------------------------------               
##------------------------------------------------------------------------------------------------------               
      
    def cleanVowelDiacriticComingAfterVowel(self):
        '''
            takes care of vowels and modifier followed by vowel diacritics
            # Example-1:
            (a)উুলু==(b)উলু-->False
                (a) breaks as ['উ', 'ু', 'ল', 'ু']
                (b) breaks as ['উ', 'ল', 'ু']
            # Example-2:
            (a)আর্কিওোলজি==(b)আর্কিওলজি-->False
                (a) breaks as ['আ', 'র', '্', 'ক', 'ি', 'ও', 'ো', 'ল', 'জ', 'ি']
                (b) breaks as ['আ', 'র', '্', 'ক', 'ি', 'ও', 'ল', 'জ', 'ি']
            

            Also Normalizes 'এ' and 'ত্র'
            # Example-1:
            (a)একএে==(b)একত্রে-->False
                (a) breaks as ['এ', 'ক', 'এ', 'ে']
                (b) breaks as ['এ', 'ক', 'ত', '্', 'র', 'ে']
                
        '''
        for idx,d in enumerate(self.decomp):
            # if the current one is a VD and the previous char is a vowel
            if  d in self.lang.vowel_diacritics and self.decomp[idx-1] in self.lang.vowels:
                # if the vowel is not 'এ'
                if self.decomp[idx-1] !='এ':
                    # remove diacritic
                    self.decomp[idx]=None
                # normalization case
                else:
                    self.decomp[idx-1]='ত'+'্'+'র'

##------------------------------------------------------------------------------------------------------               
    def fixTypoForJoFola(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if  d== self.lang.connector and self.decomp[idx+1]=='য়':
                    self.decomp[idx+1]='য'
        
    def cleanDoubleCC(self):
        # c,cc,c,cc
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-3:
                if  d== self.lang.connector and self.decomp[idx+1] in self.lang.consonants \
                    and self.decomp[idx+2]==self.lang.connector and self.decomp[idx+3] in self.lang.consonants:
                        if self.decomp[idx+3]==self.decomp[idx+1]:
                            self.decomp[idx]=None
                            self.decomp[idx+1]=None    

    
    
    def cleanDoubleRef(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-3:
                if  d=='র' and self.decomp[idx+1]==self.lang.connector\
                    and self.decomp[idx+2]=='র' and self.decomp[idx+3]== self.lang.connector:
                    self.decomp[idx]=None
                    self.decomp[idx+1]=None
        
    def fixRefOrder(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-3:
                if  d=='র' and self.decomp[idx-1]==self.lang.connector\
                    and self.decomp[idx+2]=='র' and self.decomp[idx+3]== self.lang.connector:
                    self.decomp[idx]=None
                    self.decomp[idx+1]=None
        
    def fixOrdersForCC(self):
        self.constructComplexDecomp()
        for idx,d in enumerate(self.decomp):
            if self.lang.connector in d:
                if d[0]=='র' and d[1]==self.lang.connector:
                    start=['র',self.lang.connector]
                    d=d[2:]
                else:
                    start=[]
                
                curr=[c for c in d if c!=self.lang.connector] 
                # recreate order
                order= ['ব','র','য']
                order=[k for k in order if k in curr]
                order=[c for c in curr if c not in order]+order
                # sort
                curr=sorted(curr,key=order.index)

                new=[]
                for i in range(len(curr)):
                    new.append(curr[i])
                    new.append(self.lang.connector)
                new=new[:-1]
                self.decomp[idx]="".join(start+new)
        

    def cleanConnectotForJoFola(self):
            for idx,d in enumerate(self.decomp):
                if idx<len(self.decomp)-2:
                    if  d== self.lang.connector and self.decomp[idx+1]=='য' and self.decomp[idx+2]==self.lang.connector:
                        self.decomp[idx+2]=None
        


    def cleanInvalidConjunctDiacritics(self):
        '''
            cleans repeated folas
            # Example-1:
            (a)গ্র্রামকে==(b)গ্রামকে-->False
                (a) breaks as ['গ', '্', 'র', '্', 'র', 'া', 'ম', 'ক', 'ে']
                (b) breaks as ['গ', '্', 'র', 'া', 'ম', 'ক', 'ে']
        '''
        self.safeop(self.fixTypoForJoFola)
        self.safeop(self.cleanDoubleCC)
        self.safeop(self.cleanDoubleRef)
        self.safeop(self.fixRefOrder)
        self.safeop(self.fixOrdersForCC)
        self.safeop(self.cleanConnectotForJoFola)
        self.baseCompose()
##------------------------------------------------------------------------------------------------------               
    def checkComplexRoot(self,root):
        formed=[]
        formed_idx=[]
        for i,c in enumerate(root):
            if c !='্' and i not in formed_idx:
                r=c
                if i==len(root)-1:
                    formed.append(r)
                    continue
                for j in range(i+2,len(root),2):
                
                    d=root[j]
                    k=r+'্'+d
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
    
            
    
  
