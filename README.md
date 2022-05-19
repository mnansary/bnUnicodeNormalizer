# bnUnicodeNormalizer
Bangla Unicode Normalization for word normalization
# install
```python
pip install bnunicodenormalizer
```
# useage
**initialization and cleaning**
```python
# import
from bnunicodenormalizer import Normalizer 
from pprint import pprint
# initialize
bnorm=Normalizer()
# normalize
word = 'াটোবাকো'
result=bnorm(word)
print(f"Non-norm:{word}; Norm:{result['normalized']}")
print("--------------------------------------------------")
pprint(result)
```
> output 

```
Non-norm:াটোবাকো; Norm:টোবাকো
--------------------------------------------------
{'given': 'াটোবাকো',
 'normalized': 'টোবাকো',
 'ops': [{'after': 'টোবাকো',
          'before': 'াটোবাকো',
          'operation': 'InvalidUnicode'}]}
```

**call to the normalizer returns a dictionary in the following format**

* ```given``` = provided text
* ```normalized``` = normalized text (gives None if during the operation length of the text becomes 0)
* ```ops``` = list of operations (dictionary) that were executed in given text to create normalized text
*  each dictionary in ops has:
    * ```operation```: the name of the operation / problem in given text
    * ```before``` : what the text looked like before the specific operation
    * ```after```  : what the text looks like after the specific operation  

**allow to use english text**

```python
# initialize without english (default)
norm=Normalizer()
print("without english:",norm("ASD123")["normalized"])
# --> returns None
norm=Normalizer(allow_english=True)
print("with english:",norm("ASD123")["normalized"])

```
> output

```
without english: None
with english: ASD123
```

 

# Initialization: Bangla Normalizer

```python
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

```

```python
my_legacy_maps={'ঌ':'ই',
                'ৡ':'ই',
                '৵':'ই',
                'ৠ':'ই',
                'ঽ':'ই'}
text="৺,৻,ঀ,ঌ,ৡ,ঽ,ৠ,৲,৴,৵,৶,৷,৸,৹"
# case 1
norm=Normalizer(keep_legacy_symbols=True,legacy_maps=None)
print("case-1 normalized text:  ",norm(text)["normalized"])
# case 2
norm=Normalizer(keep_legacy_symbols=True,legacy_maps=my_legacy_maps)
print("case-2 normalized text:  ",norm(text)["normalized"])
# case 2-defalut
norm=Normalizer(keep_legacy_symbols=True)
print("case-2 default normalized text:  ",norm(text)["normalized"])

# case 3
norm=Normalizer(keep_legacy_symbols=False,legacy_maps=None)
print("case-3 normalized text:  ",norm(text)["normalized"])
# case 4
norm=Normalizer(keep_legacy_symbols=False,legacy_maps=my_legacy_maps)
print("case-4 normalized text:  ",norm(text)["normalized"])
# case 4-defalut
norm=Normalizer(keep_legacy_symbols=False)
print("case-4 default normalized text:  ",norm(text)["normalized"])
```

> output

```
case-1 normalized text:   ৺,৻,ঀ,ঌ,ৡ,ঽ,ৠ,৲,৴,৵,৶,৷,৸,৹
case-2 normalized text:   ৺,৻,ঀ,ই,ই,ই,ই,৲,৴,ই,৶,৷,৸,৹
case-2 default normalized text:   ৺,৻,ঀ,ঌ,ৡ,ঽ,ৠ,৲,৴,৵,৶,৷,৸,৹
case-3 normalized text:   ,,,,,,,,,,,,,
case-4 normalized text:   ,,,ই,ই,ই,ই,,,ই,,,,
case-4 default normalized text:   ,,,,,,,,,,,,, 
```

# Operations
* base operations available for all indic languages:

```python
self.word_level_ops={"LegacySymbols"   :self.mapLegacySymbols,
                    "BrokenDiacritics" :self.fixBrokenDiacritics}

self.decomp_level_ops={"BrokenNukta"             :self.fixBrokenNukta,
                    "InvalidUnicode"             :self.cleanInvalidUnicodes,
                    "InvalidConnector"           :self.cleanInvalidConnector,
                    "FixDiacritics"              :self.cleanDiacritics,
                    "VowelDiacriticAfterVowel"   :self.cleanVowelDiacriticComingAfterVowel}
```
* extensions for bangla

```python
self.decomp_level_ops["ToAndHosontoNormalize"]             =       self.normalizeToandHosonto

# invalid folas 
self.decomp_level_ops["NormalizeConjunctsDiacritics"]      =       self.cleanInvalidConjunctDiacritics

# complex root cleanup 
self.decomp_level_ops["ComplexRootNormalization"]          =       self.convertComplexRoots

```

# Normalization Problem Examples
**In all examples (a) is the non-normalized form and (b) is the normalized form**

* Broken diacritics:
``` 
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
```
* Nukta Normalization:

```        
Example-1:
(a)কেন্দ্রীয়==(b)কেন্দ্রীয় ->  False
    (a) breaks as:['ক', 'ে', 'ন', '্', 'দ', '্', 'র', 'ী', 'য', '়']
    (b) breaks as:['ক', 'ে', 'ন', '্', 'দ', '্', 'র', 'ী', 'য়']
Example-2:
(a)রযে়ছে==(b)রয়েছে ->  False
    (a) breaks as:['র', 'য', 'ে', '়', 'ছ', 'ে']
    (b) breaks as:['র', 'য়', 'ে', 'ছ', 'ে']
Example-3: 
(a)জ়ন্য==(b)জন্য ->  False
    (a) breaks as:['জ', '়', 'ন', '্', 'য']
    (b) breaks as:['জ', 'ন', '্', 'য']
``` 
* Invalid hosonto
```
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
# Example-5: 
(a)'চু্ক্তি'==(b)'চুক্তি' ->  False 
    (a) breaks as:['চ', 'ু', '্', 'ক', '্', 'ত', 'ি']
    (b) breaks as:['চ', 'ু','ক', '্', 'ত', 'ি']
# Example-6:
(a)'যু্ক্ত'==(b)'যুক্ত' ->   False
    (a) breaks as:['য', 'ু', '্', 'ক', '্', 'ত']
    (b) breaks as:['য', 'ু', 'ক', '্', 'ত']
# Example-7:
(a)'কিছু্ই'==(b)'কিছুই' ->   False
    (a) breaks as:['ক', 'ি', 'ছ', 'ু', '্', 'ই']
    (b) breaks as:['ক', 'ি', 'ছ', 'ু','ই']
```

* To+hosonto: 

``` 
# Example-1:
(a)বুত্পত্তি==(b)বুৎপত্তি-->False
    (a) breaks as ['ব', 'ু', 'ত', '্', 'প', 'ত', '্', 'ত', 'ি']
    (b) breaks as ['ব', 'ু', 'ৎ', 'প', 'ত', '্', 'ত', 'ি']
# Example-2:
(a)উত্স==(b)উৎস-->False
    (a) breaks as ['উ', 'ত', '্', 'স']
    (b) breaks as ['উ', 'ৎ', 'স']
```

* Unwanted doubles(consecutive doubles):

```
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
# Example-4:
(a)আমাকোা==(b)'আমাকো'->   False
    (a) breaks as:['আ', 'ম', 'া', 'ক', 'ে', 'া', 'া']
    (b) breaks as:['আ', 'ম', 'া', 'ক', 'ো']
```

* Vowwels and modifier followed by vowel diacritics:

```
# Example-1:
(a)উুলু==(b)উলু-->False
    (a) breaks as ['উ', 'ু', 'ল', 'ু']
    (b) breaks as ['উ', 'ল', 'ু']
# Example-2:
(a)আর্কিওোলজি==(b)আর্কিওলজি-->False
    (a) breaks as ['আ', 'র', '্', 'ক', 'ি', 'ও', 'ো', 'ল', 'জ', 'ি']
    (b) breaks as ['আ', 'র', '্', 'ক', 'ি', 'ও', 'ল', 'জ', 'ি']
# Example-3:
(a)একএে==(b)একত্রে-->False
    (a) breaks as ['এ', 'ক', 'এ', 'ে']
    (b) breaks as ['এ', 'ক', 'ত', '্', 'র', 'ে']
```  

* Repeated folas:

```
# Example-1:
(a)গ্র্রামকে==(b)গ্রামকে-->False
    (a) breaks as ['গ', '্', 'র', '্', 'র', 'া', 'ম', 'ক', 'ে']
    (b) breaks as ['গ', '্', 'র', 'া', 'ম', 'ক', 'ে']
```

## IMPORTANT NOTE
**The normalization is purely based on how bangla text is used in ```Bangladesh```(bn:bd). It does not necesserily cover every variation of textual content available at other regions**

# unit testing
* clone the repository
* change working directory to ```tests```
* run: ```python3 -m unittest test_normalizer.py```

# Issue Reporting
* for reporting an issue please provide the specific information
    *  invalid text
    *  expected valid text
    *  why is the output expected 
    *  clone the repository
    *  add a test case in **tests/test_normalizer.py** after **line no:91**

    ```python
        # Dummy Non-Bangla,Numbers and Space cases/ Invalid start end cases
        # english
        self.assertEqual(norm('ASD1234')["normalized"],None)
        self.assertEqual(ennorm('ASD1234')["normalized"],'ASD1234')
        # random
        self.assertEqual(norm('িত')["normalized"],'ত')
        self.assertEqual(norm('সং্যুক্তি')["normalized"],"সংযুক্তি")
        # Ending
        self.assertEqual(norm("অজানা্")["normalized"],"অজানা")

        #--------------------------------------------- insert your assertions here----------------------------------------
        '''
            ###  case: give a comment about your case
            ## (a) invalid text==(b) valid text <---- an example of your case
            self.assertEqual(norm(invalid text)["normalized"],expected output)
                        or
            self.assertEqual(ennorm(invalid text)["normalized"],expected output) <----- for including english text
            
        '''
        # your case goes here-
            
    ```
    * perform the unit testing
    * make sure the unit test fails under true conditions    

# ABOUT US
* Authors: [Bengali.AI](https://bengali.ai/) in association with OCR Team , [APSIS Solutions Limited](https://apsissolutions.com/) 
* **Cite Bengali.AI multipurpose grapheme dataset paper**
```bibtext
@inproceedings{alam2021large,
  title={A large multi-target dataset of common bengali handwritten graphemes},
  author={Alam, Samiul and Reasat, Tahsin and Sushmit, Asif Shahriyar and Siddique, Sadi Mohammad and Rahman, Fuad and Hasan, Mahady and Humayun, Ahmed Imtiaz},
  booktitle={International Conference on Document Analysis and Recognition},
  pages={383--398},
  year={2021},
  organization={Springer}
}
```