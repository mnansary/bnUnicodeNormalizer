#-*- coding: utf-8 -*-
"""
@author:Bengali.AI
"""
from __future__ import print_function
#-------------------------------------------
from .langs import languages
        
#-------------------------------------------
# cleaner class
#-------------------------------------------
class BaseNormalizer(object):
    def __init__(self,
                 language,
                 allow_english=False,
                 keep_legacy_symbols=False,
                 legacy_maps=None):

        '''
            initialize a normalizer
            args:
                language                        :   language identifier/name  type(str)
                allow_english                   :   allow english letters numbers and punctuations [default:False] type(bool)
                keep_legacy_symbols             :   legacy symbols will be considered as valid unicodes[default:False] type(bool)
                legacy_maps                     :   a dictionay for changing legacy symbols into a more used  unicode [default:None] type(dict/None)
                                                    
        '''
        # error handling
        assert type(language)==str,"language is not string type!!!"
        assert language in languages.keys(),"Language is not available"
        assert type(allow_english)==bool,"allow_english is not of type boolean [True/False]"
        assert type(keep_legacy_symbols)==bool,"keep_legacy_symbols is not of type boolean [True/False]"

        self.lang           =   languages[language]
        
        if legacy_maps is not None:
            assert type(legacy_maps)==dict,"legacy_maps is not of type dict or None"
            assert len(legacy_maps.keys())>0,"legacy_maps is an empty dict"
            for k,v in legacy_maps.items():
                assert k in self.lang.legacy_symbols,f"{k} is not a legacy symbol.See README.md initialization section for legacy symbols"
                assert v in self.lang.used,f"{v} is not a valid legacy map.See README.md initialization section for legacy symbols"
        # assignments  
        self.valid          =   self.lang.valid
        self.roots          =   self.lang.complex_roots
        self.legacy_maps    =   legacy_maps
        #------------------------- update valid and complex roots-----------------------------------
        if allow_english:
            self.valid=sorted(list(set(self.valid+languages["english"].valid)))
            self.roots=sorted(list(set(self.roots+languages["english"].valid)))
        if keep_legacy_symbols:
            self.valid=sorted(list(set(self.valid+self.lang.legacy_symbols)))
            self.roots=sorted(list(set(self.roots+self.lang.legacy_symbols)))

        self.word_level_ops={"LegacySymbols"   :self.mapLegacySymbols,
                             "BrokenDiacritics":self.fixBrokenDiacritics}

        self.decomp_level_ops={"BrokenNukta"                :self.fixBrokenNukta,
                               "InvalidUnicode"             :self.cleanInvalidUnicodes,
                               "InvalidConnector"           :self.cleanInvalidConnector,
                               "FixDiacritics"              :self.cleanDiacritics,
                               "VowelDiacriticAfterVowel"   :self.cleanVowelDiacriticComingAfterVowel}

#-------------------------common ops-----------------------------------------------------------------------------   
    def checkDecomp(self):
        if len(self.decomp)>0:return True
        else:return False

    def replaceMaps(self,map_dict):
        for k,v in map_dict.items():
            self.word=self.word.replace(k,v)

    def swapIdxs(self,idx1,idx2):
        temp=self.decomp[idx1]
        self.decomp[idx1]=self.decomp[idx2]
        self.decomp[idx2]=temp

    def safeop(self,op):
        #try:
        self.decomp=[x for x in self.decomp if x is not None]
        self.decomp=[x for x in "".join(self.decomp) if x is not None] 
        op()
        # reform
        self.decomp=[x for x in self.decomp if x is not None] 
        self.decomp=[x for x in "".join(self.decomp) if x is not None] 
        
        # except IndexError:
        #     self.decomp=[x for x in self.decomp if x is not None] 
        #     pass

    def constructComplexDecomp(self):
        '''
            creates grapheme root based decomp 
        '''
        
        if self.lang.connector in self.decomp:   
            c_idxs = [i for i, x in enumerate(self.decomp) if x == self.lang.connector]
            # component wise index map    
            comps=[[cid-1,cid,cid+1] for cid in c_idxs ]
            # merge multi root
            r_decomp = []
            while len(comps)>0:
                first, *rest = comps
                first = set(first)

                lf = -1
                while len(first)>lf:
                    lf = len(first)

                    rest2 = []
                    for r in rest:
                        if len(first.intersection(set(r)))>0:
                            first |= set(r)
                        else:
                            rest2.append(r)     
                    rest = rest2

                r_decomp.append(sorted(list(first)))
                comps = rest
            
            # add    
            combs=[]
            for ridx in r_decomp:
                comb=''
                for i in ridx:
                    comb+=self.decomp[i]
                combs.append(comb)
                for i in ridx:
                    if i==ridx[-1]:
                        self.decomp[i]=comb
                    else:
                        self.decomp[i]=None
            self.decomp=[d for d in self.decomp if d is not None]
            
        
#-------------------------common ops-----------------------------------------------------------------------------   
#-------------------------word ops----------------------------------------------------------------------------- 
    def mapLegacySymbols(self):
        if self.legacy_maps is not None:
            self.replaceMaps(self.legacy_maps)

    def fixBrokenDiacritics(self):
        if self.lang.diacritic_map is not None:
            self.replaceMaps(self.lang.diacritic_map)
    
            
#-------------------------word ops----------------------------------------------------------------------------- 
#-------------------------unicode ops-----------------------------------------------------------------------------   
    def fixBrokenNukta(self):
        if self.lang.nukta_map is not None:
            for idx,d in enumerate(self.decomp):
                if d==self.lang.nukta:
                    for cidx in range(idx-1,-1,-1):
                        if self.decomp[cidx] in self.lang.nukta_map.keys():
                            self.decomp[cidx]=self.lang.nukta_map[self.decomp[cidx]]
                            self.decomp[idx]=None
                            break
                    
    def cleanInvalidUnicodes(self):
        # clean starts
        while self.checkDecomp() and self.decomp[0] in self.lang.invalid_starts:
            self.decomp=self.decomp[1:]         
        # clean endings
        while self.checkDecomp() and self.decomp[-1] == self.lang.connector:
            self.decomp=self.decomp[:-1]
        if self.checkDecomp():
            # clean invalid unicodes
            for idx,d in enumerate(self.decomp):
                if d not in self.valid:
                    self.decomp[idx]=None         
        
    def cleanInvalidConnector(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d==self.lang.connector : 
                    if self.decomp[idx-1] in self.lang.invalid_connectors  or self.decomp[idx+1] in self.lang.invalid_connectors:
                        self.decomp[idx]=None 

    def cleanVowelDiacritics(self):
        # vowel diacritics
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d in self.lang.vowel_diacritics and self.decomp[idx+1] in self.lang.vowel_diacritics :
                    # if they are same delete the current one
                    if d==self.decomp[idx+1]:
                        self.decomp[idx]=None
                    # if they are not same --> remove the last one
                    else:
                        self.decomp[idx+1]=None
    def cleanConsonantDiacritics(self):
        # consonant diacritics
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d in self.lang.consonant_diacritics and self.decomp[idx+1] in self.lang.consonant_diacritics:
                    # if they are same delete the current one
                    if d==self.decomp[idx+1]:
                        self.decomp[idx]=None
        
    def fixDiacriticOrder(self):
        for idx,d in enumerate(self.decomp):
            if idx<len(self.decomp)-1:
                if d in self.lang.consonant_diacritics and self.decomp[idx+1] in self.lang.vowel_diacritics:
                    self.swapIdxs(idx,idx+1)

    def cleanNonCharDiacs(self):
        for idx,d in enumerate(self.decomp):
            if idx>0:
                if d in self.lang.diacritics and self.decomp[idx-1] in self.lang.non_chars:
                    self.decomp[idx]=None


    def cleanDiacritics(self):
        self.safeop(self.cleanVowelDiacritics)
        self.safeop(self.cleanConsonantDiacritics)
        self.safeop(self.fixDiacriticOrder)
        self.safeop(self.cleanNonCharDiacs)
    
    def cleanVowelDiacriticComingAfterVowel(self):
        for idx,d in enumerate(self.decomp):
            if  d in self.lang.vowel_diacritics and self.decomp[idx-1] in self.lang.vowels:
                # remove diacritic
                self.decomp[idx]=None
    def fixNoSpaceChar(self):
        for idx,d in enumerate(self.decomp):
            if idx==0 and self.decomp[idx] in ["\u200c","\u200d"]:
                self.decomp[idx]=None
            else:
                if self.decomp[idx]=="\u200c":
                    self.decomp[idx]="\u200d"
                    
#----------------------composite ops-----------------------------------------------------------------------    
    def baseCompose(self):
        self.safeop(self.cleanInvalidUnicodes)
        self.safeop(self.cleanInvalidConnector)
        self.safeop(self.cleanDiacritics)
        self.safeop(self.cleanVowelDiacriticComingAfterVowel)
        self.safeop(self.fixNoSpaceChar)
        

                
#----------------------entry-----------------------------------------------------------------------    
    def __call__(self,word):
        '''
            normalizes a given word
            args:
                word    : the string to normalize
            returns: 
                a dictionary- 
                * "given" = provided text
                * "normalized = normalized text (gives None if during the operation length of the text becomes 0)
                * "ops" = list of operations (dictionary) that were executed in given text to create normalized text
                *  each dictionary in ops has:
                    * "operation": the name of the operation / problem in given text
                    * "before" : what the text looked like before the specific operation
                    * "after"  : what the text looks like after the specific operation   
        '''
        # algorithm:
        #         * execute word level ops
        #         > create unicode based decomp
        #         * execute unicode level ops
        #         > create root based decomp
        #         * execute root level ops

        details=[]
        self.check=word
        if not isinstance(self.check, str):
            raise TypeError("The provided argument/ word is not a string")  
        if len(self.check.strip().split(" "))>1:
            raise ValueError(f"The provided string has hultiple words.Make sure no space exists in the middle of the text.probable word:{self.check.replace(' ','')}")
        self.word=word
        #---------------------------------------------word ops-------------------------
        for op_id,op in self.word_level_ops.items():
            word_before_op=self.word[:]
            op()
            word_after_op=self.word[:]
            if word_before_op!=word_after_op:
                details.append({"operation":op_id,"before":word_before_op,"after":word_after_op})
        #---------------------------------------------word ops-------------------------    
        self.decomp=[ch for ch in self.word]
        #---------------------------------------------unicode ops-------------------------    
        for op_id,op in self.decomp_level_ops.items():
            word_before_op="".join(self.decomp)
            # execute
            self.safeop(op)
            # check length
            if not self.checkDecomp():
                return {"normalized":None,"given":self.check,"ops":details}
            
            word_after_op="".join(self.decomp)
            if word_before_op!=word_after_op:
                details.append({"operation":op_id,"before":word_before_op,"after":word_after_op})
        
            
        #----------------------------------------------------------------------------------------------------------
        self.safeop(self.baseCompose)
        self.word="".join([x for x in self.decomp if x is not None])     
        
        return {"normalized":self.word,"given":self.check,"ops":details}
        