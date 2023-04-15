#-*- coding: utf-8 -*-
"""
@author:Bengali.AI
indic generall ref: https://r12a.github.io/scripts/
"""
from __future__ import print_function
#--------------------------------------------------------------------------------------------------------------------------------------------
# language classes
#--------------------------------------------------------------------------------------------------------------------------------------------
class english:
    lower                  =    ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper                  =    ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    punctuations           =    ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', 
                                 '@', '[', '\\', ']', '^', '_', '`','{', '|', '}', '~']
    numbers                =    ["0","1","2","3","4","5","6","7","8","9"]

    valid                  =    sorted(lower+upper+numbers+punctuations)
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
class bangla:
    '''
        * vowel and consonant division according to : http://bn.wikipedia.org/wiki/%E0%A7%8E
        * consonant conjuncts according to: http://bn.wiktionary.org/wiki/উইকিঅভিধান:বাংলা_যুক্তবর্ণের_তালিকা
        * punctuations according to: https://bn.wikipedia.org/wiki/যতিচিহ্ন
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =    "bangla"
    nukta                  =   '়'
    vowels                 =   ['অ', 'আ', 'ই', 'ঈ', 'উ', 'ঊ', 'ঋ', 'এ', 'ঐ', 'ও', 'ঔ']
    consonants             =   ['ক', 'খ', 'গ', 'ঘ', 'ঙ', 'চ', 'ছ','জ', 'ঝ', 'ঞ', 'ট', 'ঠ', 'ড', 'ঢ', 'ণ', 'ত', 'থ', 'দ', 'ধ', 'ন', 
                                'প', 'ফ', 'ব', 'ভ', 'ম', 'য', 'র', 'ল', 'শ', 'ষ', 'স', 'হ','ড়', 'ঢ়', 'য়','ৎ']
    vowel_diacritics       =   ['া', 'ি', 'ী', 'ু', 'ূ', 'ৃ', 'ে', 'ৈ', 'ো', 'ৌ']
    consonant_diacritics   =   ['ঁ', 'ং', 'ঃ']
    numbers                =   ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯']
    punctuations           =   ['!', '"', "'", '(', ')', ',', '-', '.', '...', ':', ':-', ';', '<', '=', '>', '?', '[', ']', '{', '}', '।', '৷', '–', '—', '”', '√']
    symbols                =   ['৳']
    connector              =   '্'
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0984', '\u098d','\u098e','\u0991','\u0992','\u09a9','\u09b1','\u09b3','\u09b4','\u09b5',
                                '\u09ba','\u09bb', '\u09c5','\u09c6','\u09c9','\u09ca','\u09cf','\u09d0','\u09d1','\u09d2',
                                '\u09d3','\u09d4','\u09d5','\u09d6', '\u09d8','\u09d9','\u09da','\u09db','\u09de', '\u09e4',
                                '\u09e5', 'ৼ','৽','৾','\u09ff']
    legacy_symbols         =   ['৺','৻','ঀ','ঌ','ৡ','ঽ','ৠ','৲','৴','৵','৶','৷','৸','৹']
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   ['এ্য','অ্য','ক্ক','ক্ট','ক্ট্য','ক্ট্র','ক্ত','ক্ত্র','ক্ব','ক্ম','ক্য','ক্র','ক্র্য','ক্ল','ক্ল্য','ক্ষ','ক্ষ্ণ','ক্ষ্ব','ক্ষ্ম','ক্ষ্ম্য','ক্ষ্য',
                                'ক্স','ক্স্য','খ্য','খ্র','গ্ণ','গ্ধ','গ্ধ্য','গ্ধ্র','গ্ন','গ্ন্য','গ্ব','গ্ম','গ্য','গ্র','গ্র্য','গ্ল','গ্ল্য','ঘ্ন','ঘ্য','ঘ্র',
                                'ঙ্ক','ঙ্ক্ত','ঙ্ক্য','ঙ্ক্ষ','ঙ্খ','ঙ্খ্য','ঙ্গ','ঙ্গ্য','ঙ্ঘ','ঙ্ঘ্য','ঙ্ঘ্র','ঙ্ম','চ্চ','চ্ছ','চ্ছ্ব','চ্ছ্র','চ্ঞ','চ্ব','চ্য','জ্জ',
                                'জ্জ্ব','জ্ঝ','জ্ঞ','জ্ব','জ্য','জ্র','ঞ্চ','ঞ্ছ','ঞ্জ','ঞ্ঝ','ট্ট','ট্ব','ট্ম','ট্য','ট্র','ট্র্য','ড্ড','ড্ব','ড্য','ড্র',
                                'ড্র্য','ঢ্য','ঢ্র','ণ্ট','ণ্ঠ','ণ্ঠ্য','ণ্ড','ণ্ড্য','ণ্ড্র','ণ্ঢ','ণ্ণ','ণ্ব','ণ্ম','ণ্য','ত্ত','ত্ত্ব','ত্ত্য','ত্থ','ত্ন','ত্ব',
                                'ত্ম','ত্ম্য','ত্য','ত্র','ত্র্য','থ্ব','থ্য','থ্র','থ্র্য','দ্গ','দ্ঘ','দ্দ','দ্দ্ব','দ্ধ','দ্ব','দ্ভ','দ্ভ্র','দ্ম','দ্য','দ্র',
                                'দ্র্য','ধ্ন','ধ্ব','ধ্ম','ধ্য','ধ্র','ন্ক','ন্ট','ন্ট্য','ন্ট্র','ন্ট্র্য','ন্ঠ','ন্ড','ন্ড্ব','ন্ড্য','ন্ড্র','ন্ত','ন্ত্ব','ন্ত্য','ন্ত্র',
                                'ন্ত্র্য','ন্থ','ন্থ্য','ন্থ্র','ন্দ','ন্দ্ব','ন্দ্য','ন্দ্র','ন্ধ','ন্ধ্য','ন্ধ্র','ন্ন','ন্ব','ন্ম','ন্য','ন্শ্য','ন্স','ন্স্য','প্ট','প্ট্য',
                                'প্ত','প্ন','প্প','প্য','প্র','প্র্য','প্ল','প্ল্য','প্স','ফ্য','ফ্র','ফ্র্য','ফ্ল','ফ্ল্য','ব্জ','ব্দ','ব্ধ','ব্ব','ব্য','ব্র',
                                'ব্র্য','ব্ল','ভ্ব','ভ্য','ভ্র','ম্ন','ম্ন্য','ম্প','ম্প্য','ম্প্র','ম্ফ','ম্ব','ম্ব্র','ম্ভ','ম্ভ্র','ম্ম','ম্য','ম্র','ম্ল','য্য',
                                'র্ক','র্ক্ট','র্ক্য','র্খ','র্গ','র্গ্য','র্গ্র','র্ঘ','র্ঘ্য','র্চ','র্চ্য','র্ছ','র্জ','র্জ্ঞ','র্জ্য','র্ঝ','র্ট','র্ট্য','র্ট্র','র্ড',
                                'র্ড্র','র্ঢ্য','র্ণ','র্ণ্য','র্ত','র্ত্ম','র্ত্য','র্ত্র','র্থ','র্থ্য','র্দ','র্দ্ব','র্দ্র','র্ধ','র্ধ্ব','র্ন','র্ন্ড','র্প','র্প্ট','র্প্ল',
                                'র্ফ','র্ব','র্ব্য','র্ভ','র্ম','র্ম্থ','র্ম্প','র্ম্য','র্য','র্ল','র্ল্ড','র্ল্য','র্শ','র্শ্ব','র্শ্য','র্ষ','র্ষ্য','র্স','র্স','র্স্ট',
                                'র্স্ম','র্স্য','র্হ','র্হ্য','র্হ্য','র‍্য','ল্ক','ল্ক্য','ল্গ','ল্চ','ল্ট','ল্ট্য','ল্ট্র','ল্ড','ল্ড্য','ল্ড্র','ল্প','ল্ফ','ল্ব','ল্ব্য',
                                'ল্ভ','ল্ম','ল্য','ল্ল','শ্চ','শ্ছ','শ্ন','শ্ব','শ্ম','শ্য','শ্র','শ্র্য','শ্ল','ষ্ক','ষ্ক্র','ষ্ট','ষ্ট্য','ষ্ট্র','ষ্ঠ','ষ্ঠ্য',
                                'ষ্ণ','ষ্প','ষ্প্র','ষ্ফ','ষ্ব','ষ্ম','ষ্য','স্ক','স্ক্য','স্ক্র','স্ক্র্য','স্খ','স্চ','স্ট','স্ট্য','স্ট্র','স্ট্র্য','স্ত','স্ত্ব','স্ত্য',
                                'স্ত্র','স্থ','স্থ্য','স্ন','স্ন্য','স্প','স্প্য','স্প্র','স্প্র্য','স্প্ল','স্প্ল্য','স্ফ','স্ব','স্ম','স্ম্য','স্য','স্র','স্ল','স্ল্য','হ্ণ',
                                'হ্ন','হ্ব','হ্ম','হ্য','হ্র','হ্ল','য়্য','ব্ল্য','র্ন্ত','ঠ্য','ভ্ল']
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps             =   {'ঀ':'৭',
                                'ঌ':'৯',
                                'ৡ':'৯',
                                '৵':'৯',
                                '৻':'ৎ',
                                'ৠ':'ঋ',
                                'ঽ':'ই'}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
    nukta_map              =   {'য':'য়',
                                'ব':'র',
                                'ড':'ড়',
                                'ঢ':'ঢ়'}
    diacritic_map           =   {'ো':'ো',
                                'ৌ':'ৌ',
                                'অা':'আ',
                                'ৄ':'ৃ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
            * khondo to
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+['ৎ']+numbers+punctuations)       
    
class devanagari:
    '''
        * vowel and consonant division according to :https://unicode-table.com/en/blocks/devanagari/
        * consonant conjuncts according to: https://en.wikipedia.org/wiki/Devanagari_conjuncts
        * punctuations according to: https://www.learnsanskrit.org/guide/devanagari/numerals-and-punctuation/ 
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "devanagari"
    nukta                  =   '़'
    vowels                 =   ['ऄ', 'अ', 'आ', 'इ', 'ई', 'उ', 'ऊ', 'ऋ', 'ऌ', 'ऍ', 'ऎ', 'ए', 'ऐ', 'ऑ', 'ऒ', 'ओ', 'औ','ॠ', 'ॡ', 'ॢ', 'ॣ','ॲ','ॳ', 'ॴ', 'ॵ','ॶ', 'ॷ']
    consonants             =   ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'ऩ', 'प', 'फ', 'ब', 
                                'भ', 'म', 'य', 'र', 'ऱ', 'ल', 'ळ', 'ऴ', 'व', 'श', 'ष', 'स', 'ह','क़', 'ख़', 'ग़', 'ज़', 'ड़', 'ढ़', 'फ़', 'य़','ॸ', 'ॹ', 'ॺ']

    vowel_diacritics       =   ['ऺ', 'ऻ','ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॅ', 'ॆ', 'े', 'ै', 'ॉ', 'ॊ', 'ो', 'ौ','ॎ', 'ॏ','ॕ','ॖ', 'ॗ']

    
    consonant_diacritics   =   ['ऀ', 'ँ', 'ं', 'ः']

    numbers                =   ['०', '१', '२', '३', '४', '५', '६', '७', '८', '९'] 
    punctuations           =   ['।', '॥', ':', ';', '!', '—', '?', 'ऽ']
    symbols                =   []  
    connector              =   '्'
    
    
    non_gylph_unicodes     =   [] 

    legacy_symbols         =   []      
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
   
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------

    nukta_map              =   {'क':'क़',
                                'ख':'ख़',
                                'ग':'ग़',
                                'ज':'ज़',
                                'ड':'ड़',
                                'ढ':'ढ़',
                                'फ':'फ़',
                                'य':'य़',
                                'ळ':'ऴ',
                                'न':'ऩ'}
  
    diacritic_map          =   {'ाे':'ो',
                                'ाै':'ौ',
                                'अा':'आ',
                                'अो':'ओ',
                                'अौ': 'औ',
                                'एे': 'ऐ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
class gujarati:
    '''
        * vowel and consonant division according to : https://unicode-table.com/en/blocks/gujarati/
        * consonant conjuncts according to: https://en.wikipedia.org/wiki/Gujarati_script
        * punctuations according to: https://github.com/BengaliAI/syntheticWords/blob/main/coreLib/languages.py
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "gujarati"
    nukta                  =   '઼'
    vowels                 =   ['અ', 'આ', 'ઇ', 'ઈ', 'ઉ', 'ઊ', 'ઋ', 'ઌ', 'ઍ', 'એ', 'ઐ', 'ઑ', 'ઓ', 'ઔ','ૠ', 'ૡ', 'ૢ', 'ૣ']
    consonants             =   ['ક', 'ખ', 'ગ', 'ઘ', 'ઙ', 'ચ', 'છ', 'જ', 'ઝ', 'ઞ', 'ટ', 'ઠ', 'ડ', 'ઢ', 'ણ', 'ત', 'થ', 'દ', 'ધ', 'ન', 'પ', 'ફ', 'બ', 'ભ', 'મ', 'ય', 'ર', 'લ', 'ળ', 'વ', 'શ', 'ષ', 'સ', 'હ','ૹ']
    vowel_diacritics       =   ['ા', 'િ', 'ી', 'ુ', 'ૂ', 'ૃ', 'ૄ', 'ૅ', 'ે', 'ૈ', 'ૉ', 'ો', 'ૌ']
    consonant_diacritics   =   ['ઁ', 'ં', 'ઃ']
    numbers                =   ['૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯']
    punctuations           =   ['ઽ',',',';','।','?','!',':','—',':-',"'",'”','(', ')','{', '}','[',']','√','<','>','=','...','.','-'] 
    symbols                =   ['૱']
    connector              =   '્'
    
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0a80', '\u0a84', '\u0aa9', '\u0ab1', '\u0ab4', '\u0aba', '\u0abb', '\u0ac6', '\u0aca', '\u0ace', '\u0acf', 
                                '\u0ad1', '\u0ad2', '\u0ad3', '\u0ad4', '\u0ad5', '\u0ad6', '\u0ad7', '\u0ad8', '\u0ad9', '\u0ada', '\u0adb', 
                                '\u0adc', '\u0add', '\u0ade', '\u0adf', '\u0ae4', '\u0ae5', '\u0af1', '\u0af2', '\u0af3', '\u0af4', '\u0af5', 
                                '\u0af6', '\u0af7', '\u0af8']

    legacy_symbols         =   []  
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
    
    nukta_map              =   {} # NONE

    diacritic_map          =   {'ાે': 'ો',
                                'ાૅ': 'ૉ',
                                'ાૈ': 'ૌ',
                                'અા': 'આ',
                                'અે': 'એ',
                                'અો': 'ઓ',
                                'અૅ': 'ઍ',
                                'અૉ': 'ઑ',
                                'અૈ': 'ઐ',
                                'અૌ': 'ઔ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
class odiya:
    '''
        * vowel and consonant division according to : https://unicode-table.com/en/blocks/oriya/
        * consonant conjuncts according to: https://en.wikipedia.org/wiki/Odia_script
        * punctuations according to: https://github.com/BengaliAI/syntheticWords/blob/main/coreLib/languages.py
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "odiya"
    nukta                  =   '଼'
    vowels                 =   ['ଅ', 'ଆ', 'ଇ', 'ଈ', 'ଉ', 'ଊ', 'ଋ', 'ଌ', 'ଏ', 'ଐ', 'ଓ', 'ଔ','ୠ', 'ୡ']
    consonants             =   ['କ', 'ଖ', 'ଗ', 'ଘ', 'ଙ', 'ଚ', 'ଛ', 'ଜ', 'ଝ', 'ଞ', 'ଟ', 'ଠ', 'ଡ', 'ଢ', 'ଣ', 
                                'ତ', 'ଥ', 'ଦ', 'ଧ', 'ନ', 'ପ', 'ଫ', 'ବ', 'ଭ', 'ମ', 'ଯ', 'ର', 'ଲ', 'ଳ', 'ଵ', 
                                'ଶ', 'ଷ', 'ସ', 'ହ','ଡ଼', 'ଢ଼', 'ୟ','ୱ']
    vowel_diacritics       =   ['ା', 'ି', 'ୀ', 'ୁ', 'ୂ', 'ୃ', 'ୄ', 'େ', 'ୈ','ୋ', 'ୌ','ୢ', 'ୣ']
    consonant_diacritics   =   ['ଁ', 'ଂ', 'ଃ']
    numbers                =   ['୦', '୧', '୨', '୩', '୪', '୫', '୬', '୭', '୮', '୯']
    punctuations           =   [',',';','।','?','!',':','—',':-',"'",'”','(', ')','{', '}','[',']','√','<','>','=','...','.','-'] 
    symbols                =   ['୲', '୳', '୴', '୵', '୶', '୷']
    connector              =   '୍'
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0b00', '\u0b04', '\u0b0d', '\u0b0e', '\u0b11', '\u0b12', '\u0b29', '\u0b31', '\u0b34', '\u0b3a', '\u0b3b', 
                                '\u0b45', '\u0b46', '\u0b49', '\u0b4a', '\u0b4e', '\u0b4f', '\u0b50', '\u0b51', '\u0b52', '\u0b53', '\u0b54', 
                                '\u0b58', '\u0b59', '\u0b5a', '\u0b5b', '\u0b5e', '\u0b64', '\u0b65', '\u0b78', '\u0b79', '\u0b7a', '\u0b7b', 
                                '\u0b7c', '\u0b7d', '\u0b7e', '\u0b7f']
    legacy_symbols         =   []  
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
    nukta_map              =   {'ଡ':'ଡ଼',
                                'ଢ':'ଢ଼'}
     
    diacritic_map          =   {'ୋ':'ୋ',
                                'ୈା':'ୌ',
                                'ଓୗ':'ଔ',
                                'ଏୗ':'ଐ',
                                'ଅା':'ଆ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
        
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------

class tamil:
    '''
        * vowel and consonant division according to : https://unicode-table.com/en/blocks/tamil/
        * consonant conjuncts according to: https://en.wikipedia.org/wiki/Tamil_script
        * punctuations according to: https://github.com/BengaliAI/syntheticWords/blob/main/coreLib/languages.py
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "tamil"
    nukta                  =   ''  
    vowels                 =   ['அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ']
    consonants             =   ['க', 'ங', 'ச', 'ஜ', 'ஞ', 'ட', 'ண', 'த', 'ந', 'ன', 'ப', 'ம', 'ய', 'ர', 'ற', 'ல', 'ள', 'ழ', 'வ', 'ஶ', 'ஷ', 'ஸ', 'ஹ']
    vowel_diacritics       =   ['ா', 'ி', 'ீ', 'ு', 'ூ', 'ெ', 'ே', 'ை','ொ', 'ோ', 'ௌ']
    consonant_diacritics   =   ['ஂ', 'ஃ']
    numbers                =   ['௦', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯','௰', '௱', '௲']
    punctuations           =   [',',';','।','?','!',':','—',':-',"'",'”','(', ')','{', '}','[',']','√','<','>','=','...','.','-']
    symbols                =   ['௳', '௴', '௵','௹','௶', '௷', '௸','௺']
    connector              =   '்' 
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0b80', '\u0b81', '\u0b84', '\u0b8b', '\u0b8c', '\u0b8d', '\u0b91', '\u0b96', '\u0b97', '\u0b98', '\u0b9b', 
                                '\u0b9d', '\u0ba0', '\u0ba1', '\u0ba2', '\u0ba5', '\u0ba6', '\u0ba7', '\u0bab', '\u0bac', '\u0bad', '\u0bba', 
                                '\u0bbb', '\u0bbc', '\u0bbd', '\u0bc3', '\u0bc4', '\u0bc5', '\u0bc9', '\u0bce', '\u0bcf', '\u0bd8', '\u0bd9', 
                                '\u0bda', '\u0bdb', '\u0bdc', '\u0bdd', '\u0bde', '\u0bdf', '\u0be0', '\u0be1', '\u0be2', '\u0be3', '\u0bd1', 
                                '\u0bd2', '\u0bd3', '\u0bd4', '\u0bd5', '\u0bd6', '\u0bd8', '\u0bd9', '\u0bda', '\u0bdb', '\u0bdc', '\u0bdd', 
                                '\u0bde', '\u0bdf', '\u0be0', '\u0be1', '\u0be2', '\u0be3', '\u0be4', '\u0be5', '\u0bfb', '\u0bfc', '\u0bfd', 
                                '\u0bfe', '\u0bff']
    legacy_symbols         =   []  
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    # this is a customizeable map : this map is purely based on visual similiarity 
     
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
     
    nukta_map              =   {} # NONE
     
    diacritic_map          =   {'ொ':'ொ',
                                "ோ":'ோ'} 
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
        
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
class panjabi:
    '''
        * vowel and consonant division according to : https://unicode-table.com/en/blocks/gurmukhi/
        * consonant conjuncts according to: NOT USED
        * punctuations according to: https://github.com/BengaliAI/syntheticWords/blob/main/coreLib/languages.py
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "panjabi"
    nukta                  =   '਼'
    vowels                 =   ['ਅ', 'ਆ', 'ਇ', 'ਈ', 'ਉ', 'ਊ', 'ਏ', 'ਐ', 'ਓ', 'ਔ','ੲ', 'ੳ']
    consonants             =   ['ਕ', 'ਖ', 'ਗ', 'ਘ', 'ਙ', 'ਚ', 'ਛ', 'ਜ', 'ਝ', 'ਞ', 'ਟ', 'ਠ', 'ਡ', 'ਢ', 'ਣ', 'ਤ', 'ਥ', 
                                'ਦ', 'ਧ', 'ਨ', 'ਪ', 'ਫ', 'ਬ', 'ਭ', 'ਮ', 'ਯ', 'ਰ', 'ਲ', 'ਲ਼', 'ਵ', 'ਸ਼', 'ਸ', 'ਹ','ਖ਼', 
                                'ਗ਼', 'ਜ਼', 'ੜ', 'ਫ਼']
    vowel_diacritics       =   ['ਾ', 'ਿ', 'ੀ', 'ੁ', 'ੂ', 'ੇ', 'ੈ', 'ੋ', 'ੌ']
    consonant_diacritics   =   ['ਁ', 'ਂ', 'ਃ'] # Not found!
    numbers                =   ['੦', '੧', '੨', '੩', '੪', '੫', '੬', '੭', '੮', '੯']
    punctuations           =   [',',';','।','?','!',':','—',':-',"'",'”','(', ')','{', '}','[',']','√','<','>','=','...','.','-']
    symbols                =   []
    connector              =   '੍'
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0a00', '\u0a04', '\u0a0b', '\u0a0c', '\u0a0d', '\u0a0e', '\u0a11', '\u0a12', '\u0a29', '\u0a31', 
                                '\u0a34', '\u0a37', '\u0a3a', '\u0a3b', '\u0a3d', '\u0a43', '\u0a44', '\u0a45', '\u0a46', '\u0a49', 
                                '\u0a4a', '\u0a4e', '\u0a4f', '\u0a50', '\u0a52', '\u0a53', '\u0a54', '\u0a55', '\u0a56', '\u0a57', 
                                '\u0a58', '\u0a5d', '\u0a5f', '\u0a60', '\u0a61', '\u0a62', '\u0a63', '\u0a64', '\u0a65', '\u0a76', 
                                '\u0a77', '\u0a78', '\u0a79', '\u0a7a', '\u0a7b', '\u0a7c', '\u0a7d', '\u0a7e', '\u0a7f']
    legacy_symbols         =   []
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
    nukta_map              =   {'ਖ':'ਖ਼',
                                'ਗ':'ਗ਼',
                                'ਜ':'ਜ਼',
                                'ਲ':'ਲ਼',
                                'ਸ':'ਸ਼',
                                'ਫ':'ਫ਼'
                                }
    diacritic_map          =   {'ੇੋ': 'ੌ',
                                'ਾੇ': 'ੀ',
                                'ਾੋ': 'ੀ',
                                'ਅੈ': 'ਐ',
                                'ਅੌ': 'ਔ',
                                'ਅਾ': 'ਆ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
        
        
    
#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
class malayalam:
    '''
        * vowel and consonant division according to: https://unicode-table.com/en/blocks/malayalam/
        * consonant conjuncts according to: Self Generated
        * punctuations according to: https://github.com/BengaliAI/syntheticWords/blob/main/coreLib/languages.py
    '''
    
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "malayalam"
    nukta                  =   '়'
    vowels                 =   ['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ഌ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ','ൠ', 'ൡ'] 
    consonants             =   ['ക', 'ഖ', 'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ', 'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 
                                'ദ', 'ധ', 'ന', 'ഩ', 'പ', 'ഫ', 'ബ', 'ഭ', 'മ', 'യ', 'ര', 'റ', 'ല', 'ള', 'ഴ', 'വ', 'ശ', 'ഷ', 
                                'സ', 'ഹ', 'ഺ']
    vowel_diacritics       =   ['ാ', 'ി', 'ീ', 'ു', 'ൂ', 'ൃ', 'ൄ',     'െ', 'േ', 'ൈ','ൊ', 'ോ', 'ൌ','ൗ','ൢ', 'ൣ']
    consonant_diacritics   =   ['ഀ', 'ഁ', 'ം', 'ഃ', 'ഄ']
    numbers                =   ['൦', '൧', '൨', '൩', '൪', '൫', '൬', '൭', '൮', '൯','൘', '൙', '൚', '൛', '൜', '൝', '൞','൰', '൱', '൲','൳', '൴', '൵', '൶', '൷', '൸']
    punctuations           =    [',',';','।','?','!',':','—',':-',"'",'”','(', ')','{', '}','[',']','√','<','>','=','...','.','-']
    symbols                =   ['ഽ', '൏', '൹']

    
    
    connector              =   '്' # There are two other this shit '഻', '഼'
    
    # based on unicode range : \u0980-\u09FF
    non_gylph_unicodes     =   ['\u0d64', '\u0d65', '\u0d50', '\u0d51', '\u0d52', '\u0d53', '\u0d49', '\u0d45', '\u0d11', '\u0d0d']
    legacy_symbols         =   ['ൟ']
    
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    
    # this is a customizeable map : this map is purely based on visual similiarity 
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    
    #---------------------------------------------------normalization maps---------------------------------------------------------
    nukta_map              =   {}
    diacritic_map          =   {} #NONE--<>
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts) 
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
             
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)     
        
        
class sylhetinagri:
    '''
        * according to asif sushmit
    '''
    #-----------------------------------------------------basic-------------------------------------------------------------------
    iden                   =   "sylhetinagri"
    nukta                  =   '' #done
    vowels                 =   ['ꠀ', 'ꠁ', 'ꠃ', 'ꠄ', 'ꠅ'] #done
    consonants             =   ['ꠇ', 'ꠈ', 'ꠉ', 'ꠊ',
                                 'ꠌ', 'ꠍ', 'ꠎ', 'ꠏ',
                                 'ꠐ', 'ꠑ', 'ꠒ', 'ꠓ',
                                 'ꠔ', 'ꠕ', 'ꠖ', 'ꠗ', 'ꠘ',
                                 'ꠙ', 'ꠚ', 'ꠛ', 'ꠜ', 'ꠝ',
                                 'ꠞ', 'ꠟ', 'ꠠ', 'ꠡ', 'ꠢ'] #done
    vowel_diacritics       =   ['ꠣ', 'ꠤ', 'ꠥ', 'ꠦ', 'ꠧ'] #done
    consonant_diacritics   =   ['ꠋ', 'ꠂ', '꠬'] #done
    numbers                =   ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '०', '१', '२', '३', '४', '५', '६', '७', '८', '९']
    punctuations           =   ['।', '॥', ':', ';', '!', '—', '?', 'ऽ', '.', ',']
    symbols                =   ['꠨', '꠩', '꠪', '꠫']
    connector              =   '꠆' #done
    non_gylph_unicodes     =   []
    legacy_symbols         =   []
    non_chars              =   numbers+punctuations+symbols+non_gylph_unicodes+legacy_symbols
    #-----------------------------------------------------basic-------------------------------------------------------------------
    #---------------------------------------------------changeables----------------------------------------------------------------
    conjuncts              =   []
    # this is a customizeable map : this map is purely based on visual similiarity
    legacy_maps            =   {}
    #---------------------------------------------------changeables----------------------------------------------------------------
    #---------------------------------------------------normalization maps---------------------------------------------------------
    nukta_map              =   {}
    diacritic_map           =   {'ꠦꠣ':'ꠧ',
                                'ꠣꠦ':'ꠧ'}
    #---------------------------------------------------normalization maps---------------------------------------------------------
    diacritics             =   sorted(vowel_diacritics+consonant_diacritics)
    used                   =   sorted(vowels+consonants+vowel_diacritics+consonant_diacritics+numbers)
    valid                  =   sorted([' ']+used+punctuations+[connector]+["\u200d","\u200c"])
    complex_roots          =   sorted([' ']+vowels+consonants+numbers+punctuations+symbols+conjuncts)
    # these unicodes can not start a word
    invalid_starts         =   sorted(diacritics+[connector])
    # invalid connector cases
    '''
        a connector can not be sorrounded by/ can not come after or before:
            * the vowels
            * the diacritics
            * another connector [double consecutive hosonto]
    '''
    invalid_connectors     =    sorted(invalid_starts+vowels+numbers+punctuations)

#--------------------------------------------------------------------------------------------------------------------------------------------
#############################################################################################################################################
#--------------------------------------------------------------------------------------------------------------------------------------------
languages={}
languages["english"]    =english
languages["bangla"]     =bangla
languages["devanagari"] =devanagari
languages["gujarati"]   =gujarati
languages["odiya"]      =odiya
languages["tamil"]      =tamil
languages["panjabi"]    =panjabi
languages["malayalam"]  =malayalam
languages["sylhetinagri"]=sylhetinagri
