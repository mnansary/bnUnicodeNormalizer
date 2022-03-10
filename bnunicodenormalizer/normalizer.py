#-*- coding: utf-8 -*-
"""
@author:Bengali.AI
"""
from __future__ import print_function
#-------------------------------------------
# globals
#-------------------------------------------

op_map=["NonGylphUnicodes",
        "InvalidUnicodes",
        "InvalidEnds",
        "InvalidStarts",
        "NuktaUnicode",
        "InvalidHosonto",
        "InvalidToAndHosonto",
        "DoubleVowelDiacritics",
        "VowelDiacriticsComingAfterVowelsAndModifiers",
        "InvalidMultipleConsonantDiacritics"]

word_op_map=["MapLegacySymbols",
             "NormalizeAssamese", 
             "BrokenDiacritics"]
        
class english:
    lower                  =    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper                  =    ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    punctuations           =    ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
                                '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                                '{', '|', '}', '~']
    numbers                =    ["0","1","2","3","4","5","6","7","8","9"]
    valid                    =    sorted(lower+upper+numbers+punctuations)

default_legacy_maps={'ঀ':'৭',
                    'ঌ':'৯',
                    'ৡ':'৯',
                    '৵':'৯',
                    '৻':'ৎ',
                    'ৠ':'ঋ',
                    'ঽ':'ই'}

#-------------------------------------------
# cleaner class
#-------------------------------------------

class Normalizer(object):
    def __init__(self,
                allow_english=False,
                keep_legacy_symbols=False,
                legacy_maps=default_legacy_maps):

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
                                                    default_legacy_maps={'ঀ':'৭',
                                                                        'ঌ':'৯',
                                                                        'ৡ':'৯',
                                                                        '৵':'৯',
                                                                        '৻':'ৎ',
                                                                        'ৠ':'ঋ',
                                                                        'ঽ':'ই'}
                                                    
                                                    pass-   
                                                    * legacy_maps=None for keeping the legacy symbols as they are
                                                    * legacy_maps=custom dictionary which will map your desired legacy symbol to any of symbol you want
                                                        * the keys in the custiom dicts must belong to any of the legacy symbols
                                                        * the values in the custiom dicts must belong to either vowels,consonants of numbers  
                                                        vowels         =   ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']
                                                        consonants     =   ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ','জ', 'ঝ', 'ঞ', 
                                                                            'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 
                                                                            'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 
                                                                            'স', 'হ','ড়', 'ঢ়', 'য়','ৎ']    
                                                        numbers        =    ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
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
        # components    
        '''
            this division of vowel, consonant and modifier is done according to :https://bn.wikipedia.org/wiki/%E0%A7%8E 
        '''
        self.vowels                 =   ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']
        self.consonants             =   ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ','জ', 'ঝ', 'ঞ', 
                                         'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 
                                         'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 
                                         'স', 'হ','ড়', 'ঢ়', 'য়','ৎ']
        self.modifiers              =   ['ঁ', 'ং', 'ঃ']
        # diacritics
        self.vowel_diacritics       =   ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ']
        self.consonant_diacritics   =   ['ঁ', 'র্', 'র্য', '্য', '্র', '্র্য', 'র্্র']
        # special charecters
        self.nukta                  =   '়'
        self.hosonto                =   '্'
        self.special_charecters     =   [self.nukta,self.hosonto,'\u200d','\u200c',' ']
        
        self.numbers                =    ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
        self.punctuations           =    ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
                                        '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                                        '{', '|', '}', '~', '।','৳']
            
        self.non_gylph_unicodes     =['\u0984', '\u098d','\u098e','\u0991','\u0992','\u09a9','\u09b1','\u09b3','\u09b4','\u09b5',
                                    '\u09ba','\u09bb', '\u09c5','\u09c6','\u09c9','\u09ca','\u09cf','\u09d0','\u09d1','\u09d2',
                                    '\u09d3','\u09d4','\u09d5','\u09d6', '\u09d8','\u09d9','\u09da','\u09db','\u09de', '\u09e4',
                                    '\u09e5', 'ৼ','৽','৾','\u09ff']
        
        self.legacy_symbols         = ['৺','৻','ঀ','ঌ','ৡ','ঽ','ৠ','৲','৴','৵','৶','৷','৸','৹']
        # all valid unicode charecters
        self.valid_unicodes         =   self.vowels+self.consonants+self.modifiers+self.vowel_diacritics+self.special_charecters+self.numbers+self.punctuations 
        
        # error handling
        assert type(allow_english)==bool,"allow_english is not of type boolean [True/False]"
        assert type(keep_legacy_symbols)==bool,"keep_legacy_symbols is not of type boolean [True/False]"
        
        if legacy_maps is not None:
            assert type(legacy_maps)==dict,"legacy_maps is not of type dict or None"
            assert len(legacy_maps.keys())>0,"legacy_maps is an empty dict"
            for k,v in legacy_maps.items():
                assert k in self.legacy_symbols,f"{k} is not a legacy symbol.See README.md initialization section for legacy symbols"
                assert v in self.vowels+self.consonants+self.numbers,f"{v} is not a valid legacy map.See README.md initialization section for legacy symbols"
                
        self.legacy_maps=legacy_maps

        
        #------------------------- update valid unicodes-----------------------------------
        if allow_english:
            self.valid_unicodes=sorted(list(set(self.valid_unicodes+english.valid)))
        if keep_legacy_symbols:
            self.valid_unicodes=sorted(list(set(self.valid_unicodes+self.legacy_symbols)))

        '''
            some cases to handle
        '''
        
        # invalid unicodes for starting
        '''
            no vowel diacritic, consonant diacritic , special charecter or modifier can start a word
        '''   
        self.invalid_unicodes_for_starting_a_word=self.modifiers+self.vowel_diacritics+self.special_charecters+self.consonant_diacritics
        
        
        
        # invalid hosonto cases
        '''
            a hosonto can not come before:
                * the vowels
                * another hosonto [double consecutive hosonto]
            a hosonto can not come after:
                * the vowels
                * the modifiers
                * another hosonto [double consecutive hosonto] 
        '''
        self.invalid_unicodes_after_hosonto     =       self.vowels+[self.hosonto]
        self.invalid_unicodes_before_hosonto    =       self.vowels+self.modifiers+[self.hosonto]
        
        
        
        # to+hosonto case
        '''

            case-1:     if 'ত'+hosonto is followed by anything other than a consonant the word is an invalid word

            case-2:     The ত্‍ symbol which should be replaced by a 'ৎ' occurs for all consonants except:ত,থ,ন,ব,ম,য,র
                        # code to verify this manually 
                        for c in self.consonants:
                            print('ত'+self.hosonto+c)
 
        '''
        self.valid_consonants_after_to_and_hosonto      =       ['ত','থ','ন','ব','ম','য','র'] 
#-------------------------word ops----------------------------------------------------------------------------- 
    def __mapLegacySymbols(self):
        if self.legacy_maps is not None:
            for k,v in self.legacy_maps.items():
                self.word=self.word.replace(k,v)


    def __replaceAssamese(self):
        '''
            case: Assamese  normalization 
                'ৰ'-->'র'
                'ৱ'-->'ব'            
        '''
        self.word = self.word.replace('ৰ','র')
        self.word = self.word.replace('ৱ','ব')
        
        

    def __replaceDiacritics(self):
        '''
            case: replace  diacritic 
                # Example-1: 
                (a)'আরো'==(b)'আরো' ->  False 
                    (a) breaks as:['আ', 'র', 'ে', 'া']
                    (b) breaks as:['আ', 'র', 'ো']
                # Example-2:
                (a)পৌঁছে==(b)পৌঁছে ->  False
                    (a) breaks as:['প', 'ে', 'ৗ', 'ঁ', 'ছ', 'ে']
                    (b) breaks as:['প', 'ৌ', 'ঁ', 'ছ', 'ে']
                # Example-3:
                (a)সংস্কৄতি==(b)সংস্কৃতি ->  False
                    (a) breaks as:['স', 'ং', 'স', '্', 'ক', 'ৄ', 'ত', 'ি']
                    (b) breaks as:['স', 'ং', 'স', '্', 'ক', 'ৃ', 'ত', 'ি']
                
                            
        '''
        # broken vowel diacritic
        # e-kar+a-kar = o-kar
        self.word = self.word.replace('ে'+'া', 'ো')
        # e-kar+e-kar = ou-kar
        self.word = self.word.replace('ে'+'ৗ', 'ৌ')
        # 'অ'+ 'া'-->'আ'
        self.word = self.word.replace('অ'+ 'া','আ')
        # unicode normalization of 'ৄ'-> 'ৃ'
        self.word = self.word.replace('ৄ','ৃ')
#-------------------------base ops-----------------------------------------------------------------------------   
    def __checkDecomp(self):
        '''
            checks if the decomp has a valid length
        '''
        if len(self.decomp)>0:
            return True
        else:
            return False

    def __reconstructDecomp(self):
        '''
            reconstructs the word from decomp
        '''
        self.decomp=[x for x in self.decomp if x is not None] 
        self.word=''
        for ch in self.decomp:
            self.word+=ch 

#-------------------------unicode ops-----------------------------------------------------------------------------               
    def __cleanNonGylphUnicodes(self):
        '''
            cleans unicodes that are non gylphs
        '''
        try:
            for idx,d in enumerate(self.decomp):
                if d in self.non_gylph_unicodes:
                    self.decomp[idx]=None         
        except Exception as e:
            pass
    def __cleanInvalidUnicodes(self):
        try:
            for idx,d in enumerate(self.decomp):
                if d not in self.valid_unicodes:
                    self.decomp[idx]=None         
        except Exception as e:
            pass

    def __cleanInvalidEnds(self):
        '''
            cleans a word that has invalid ending i.e ends with '্' that does not make any sense
        '''
        while self.decomp[-1] == self.hosonto:
            self.decomp=self.decomp[:-1]
            if not self.__checkDecomp():
                self.return_none=True
                break 


    def __cleanInvalidStarts(self):
        '''
            cleans a word that has invalid starting
        '''
        while self.decomp[0] in self.invalid_unicodes_for_starting_a_word:
            self.decomp=self.decomp[1:]
            if not self.__checkDecomp():
                self.return_none=True
                break 

            

    def __cleanNuktaUnicode(self):
        '''
            handles nukta unicode as follows:
                * If the connecting char is with in the valid list ['য','ব','ড','ঢ'] then replace with ['য়','র','ড়', 'ঢ়']
                * Otherwise remove the nukta char completely
            **the connecting char**: is defined as the previous non-vowle-diacritic char 
            Example-1:If case-1
            (a)কেন্দ্রীয়==(b)কেন্দ্রীয় ->  False
                (a) breaks as:['ক', 'ে', 'ন', '্', 'দ', '্', 'র', 'ী', 'য', '়']
                (b) breaks as:['ক', 'ে', 'ন', '্', 'দ', '্', 'র', 'ী', 'য়']
            Example-2:Elif case-2
            (a)রযে়ছে==(b)রয়েছে ->  False
                (a) breaks as:['র', 'য', 'ে', '়', 'ছ', 'ে']
                (b) breaks as:['র', 'য়', 'ে', 'ছ', 'ে']
            Example-3:Otherwise 
            (a)জ়ন্য==(b)জন্য ->  False
                (a) breaks as:['জ', '়', 'ন', '্', 'য']
                (b) breaks as:['জ', 'ন', '্', 'য']
        '''            
        __valid_charecters_without_nukta    =   ['য','ব','ড','ঢ']
        __replacements                      =   ['য়','র','ড়','ঢ়']
        try:
            for idx,d in enumerate(self.decomp):
                if d==self.nukta:
                    check=False
                    # check the previous charecter is a valid charecter where the nukta can be added
                    if self.decomp[idx-1] in __valid_charecters_without_nukta:
                        cid=idx-1
                        check=True
                    # check the previous char before vowel diacritic
                    elif self.decomp[idx-2] in __valid_charecters_without_nukta and self.decomp[idx-1] in self.vowel_diacritics:
                        cid=idx-2
                        check=True
                    # remove unwanted extra nukta 
                    else:
                        self.decomp[idx]=None
                    if check:
                        rep_char_idx=__valid_charecters_without_nukta.index(self.decomp[cid])
                        # replace
                        self.decomp[cid]=__replacements[rep_char_idx]
                        # delete nukta
                        self.decomp[idx]=None
                              
        except Exception as e:
            pass

    def __cleanInvalidHosonto(self):
        '''
            case:take care of the in valid hosontos that come after / before the vowels and the modifiers
            # Example-1:
            (a)দুই্টি==(b)দুইটি-->False
                (a) breaks as ['দ', 'ু', 'ই', '্', 'ট', 'ি']
                (b) breaks as ['দ', 'ু', 'ই', 'ট', 'ি']
            # Example-2:
            (a)এ্তে==(b)এতে-->False
                (a) breaks as ['এ', '্', 'ত', 'ে']
                (b) breaks as ['এ', 'ত', 'ে']
            # Example-3:
            (a)নেট্ওয়ার্ক==(b)নেটওয়ার্ক-->False
                (a) breaks as ['ন', 'ে', 'ট', '্', 'ও', 'য়', 'া', 'র', '্', 'ক']
                (b) breaks as ['ন', 'ে', 'ট', 'ও', 'য়', 'া', 'র', '্', 'ক']
            # Example-4:
            (a)এস্আই==(b)এসআই-->False
                (a) breaks as ['এ', 'স', '্', 'আ', 'ই']
                (b) breaks as ['এ', 'স', 'আ', 'ই']

            case:if the hosonto is in between two vowel diacritics  
            # Example-1: 
            (a)'চু্ক্তি'==(b)'চুক্তি' ->  False 
                (a) breaks as:['চ', 'ু', '্', 'ক', '্', 'ত', 'ি']
                (b) breaks as:['চ', 'ু','ক', '্', 'ত', 'ি']
            # Example-2:
            (a)'যু্ক্ত'==(b)'যুক্ত' ->   False
                (a) breaks as:['য', 'ু', '্', 'ক', '্', 'ত']
                (b) breaks as:['য', 'ু', 'ক', '্', 'ত']
            # Example-3:
            (a)'কিছু্ই'==(b)'কিছুই' ->   False
                (a) breaks as:['ক', 'ি', 'ছ', 'ু', '্', 'ই']
                (b) breaks as:['ক', 'ি', 'ছ', 'ু','ই']
        '''
        try:
            for idx,d in enumerate(self.decomp):
                if d==self.hosonto:
                    check=False
                    # before case 
                    if self.decomp[idx-1] in self.invalid_unicodes_before_hosonto and self.decomp[idx+1]!='য':
                        check=True    
                    # after case
                    elif self.decomp[idx+1] in self.invalid_unicodes_after_hosonto:
                        check=True
                    # if the hosonto is in between two vowel diacritics
                    elif self.decomp[idx-1] in self.vowel_diacritics or self.decomp[idx+1] in self.vowel_diacritics:
                        check=True
                    # if the hosonto is after modifier
                    elif self.decomp[idx-1] in self.modifiers:
                        check=True
                    
                    if check:
                        self.decomp[idx]=None
        except Exception as e:
            pass                     
    
    def __cleanInvalidToAndHosonto(self):
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
        try:
            for idx,d in enumerate(self.decomp):
                # to + hosonto
                if d=='ত' and self.decomp[idx+1]==self.hosonto:
                    # for single case
                    if  self.decomp[idx+2] not in self.valid_consonants_after_to_and_hosonto:
                        # replace
                        self.decomp[idx]='ৎ'
                        # delete
                        self.decomp[idx+1]=None
                        
                    else: 
                        # valid replacement for to+hos double case
                        if self.decomp[idx+2]=='ত' and self.decomp[idx+3]==self.hosonto:
                            if self.decomp[idx+4] not in  ['ব','য','র']:
                                # if the next charecter after the double to+hos+to+hos is with in ['ত','থ','ন','ম'] 
                                # replace
                                self.decomp[idx]='ৎ'
                                # delete
                                self.decomp[idx+1]=None
                            if self.decomp[idx+4]=='র':
                                # delete
                                self.decomp[idx+3]=None
                            
        except Exception as e:
            pass
            

    def __cleanDoubleVowelDiacritics(self):
        '''
            removes unwanted doubles(consecutive doubles):
            case:unwanted doubles  
                # Example-1: 
                (a)'যুুদ্ধ'==(b)'যুদ্ধ' ->  False 
                    (a) breaks as:['য', 'ু', 'ু', 'দ', '্', 'ধ']
                    (b) breaks as:['য', 'ু', 'দ', '্', 'ধ']
                # Example-2:
                (a)'দুুই'==(b)'দুই' ->   False
                    (a) breaks as:['দ', 'ু', 'ু', 'ই']
                    (b) breaks as:['দ', 'ু', 'ই']
                # Example-3:
                (a)'প্রকৃৃতির'==(b)'প্রকৃতির' ->   False
                    (a) breaks as:['প', '্', 'র', 'ক', 'ৃ', 'ৃ', 'ত', 'ি', 'র']
                    (b) breaks as:['প', '্', 'র', 'ক', 'ৃ', 'ত', 'ি', 'র']

            case:invalid consecutive vowel diacritics where they are not the same 
            * since there is no way to ensure which one is right it simply returns none
            
        '''
        try:
            for idx,d in enumerate(self.decomp):
                # case of consecutive vowel diacritics
                if d in self.vowel_diacritics and self.decomp[idx+1] in self.vowel_diacritics:
                    #self.decomp[idx]=None
                    
                    # if they are same delete the current one
                    if d==self.decomp[idx+1]:
                        self.decomp[idx]=None
                    # if they are not same --> remove the last one
                    else:
                        self.decomp[idx+1]=None
        except Exception as e:
            pass

    
                
                                
    def __cleanVowelDiacriticsComingAfterVowelsAndModifiers(self):
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
        try:
            # THE WIERDEST THING I HAVE SEEN
            for idx,d in enumerate(self.decomp):
                # single case 
                if d=='এ' and idx>0 and idx<len(self.decomp)-1 and self.decomp[idx+1] in self.vowel_diacritics:
                    self.decomp[idx]='ত'+'্'+'র'
            self.decomp=[ch for ch in self.decomp]
            '''
                 self.decomp[idx-1:idx]='ত', '্', 'র'
                 this replacement does not work 
            '''

            for idx,d in enumerate(self.decomp):
                # if the current one is a VD and the previous char is a modifier or vowel
                if  d in self.vowel_diacritics and self.decomp[idx-1] in self.vowels+self.modifiers:
                    # if the vowel is not 'এ'
                    if self.decomp[idx-1] !='এ':
                        # remove diacritic
                         self.decomp[idx]=None
                    # normalization case
                    else:
                        self.decomp[idx]='ত'+'্'+'র'
            self.decomp=[ch for ch in self.decomp]
        except Exception as e:
            pass 

    def __cleanInvalidMultipleConsonantDiacritics(self):
        '''
            cleans repeated folas
            # Example-1:
            (a)গ্র্রামকে==(b)গ্রামকে-->False
                (a) breaks as ['গ', '্', 'র', '্', 'র', 'া', 'ম', 'ক', 'ে']
                (b) breaks as ['গ', '্', 'র', 'া', 'ম', 'ক', 'ে']
        '''
        try:
            for idx,d in enumerate(self.decomp):
                # if the current one is hosonto and the next one is within ['ব','য','র'] 
                if  d==self.hosonto  and self.decomp[idx+1] in ['ব','য','র']:
                    _pair=self.decomp[idx+1]
                    if self.decomp[idx+2]==self.hosonto and self.decomp[idx+3]==_pair:
                        self.decomp[idx]=None
                        self.decomp[idx+1]=None
            
        except Exception as e:
            pass
    
  
#----------------------entry-----------------------------------------------------------------------    
    def __call__(self,text):
        '''
            normalizes a given text
            args:
                text    : the string to normalize
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
        details=[]
        
        if not isinstance(text, str):
            raise TypeError("The provided argument/ word is not a string")     
        self.word=text
        # None-flag
        self.return_none = False
        #---------------------------------------------word ops-------------------------
        wops=[self.__mapLegacySymbols,
              self.__replaceDiacritics,
              self.__replaceAssamese]
        
        for idx,op in enumerate(wops):
            word_before_op=self.word[:]
            op()
            word_after_op=self.word[:]
            if word_before_op!=word_after_op:
                details.append({"operation":word_op_map[idx],"before":word_before_op,"after":word_after_op})
        #---------------------------------------------word ops-------------------------    
        self.decomp=[ch for ch in self.word]
        #---------------------------------------------unicode ops-------------------------    
        # list of operations
        ops=[self.__cleanNonGylphUnicodes,
             self.__cleanInvalidUnicodes,
             self.__cleanInvalidEnds,
             self.__cleanInvalidStarts,
             self.__cleanNuktaUnicode,
             self.__cleanInvalidHosonto,
             self.__cleanInvalidToAndHosonto,
             self.__cleanDoubleVowelDiacritics,
             self.__cleanVowelDiacriticsComingAfterVowelsAndModifiers,
             self.__cleanInvalidMultipleConsonantDiacritics,
             self.__reconstructDecomp]
        
        
        for idx,op in enumerate(ops):
            word_before_op="".join(self.decomp)
            # execute
            op()
            # reform
            self.decomp=[x for x in self.decomp if x is not None] 
            word_after_op="".join(self.decomp)
            if word_before_op!=word_after_op:
                details.append({"operation":op_map[idx],"before":word_before_op,"after":word_after_op})
        
            # check length
            if not self.__checkDecomp():
                return {"normalized":None,"given":text,"ops":details}
                
        return {"normalized":self.word,"given":text,"ops":details}
        