# bnUnicodeNormalizer
Bangla Unicode Normalization
# install
```python
pip install bnunicodenormalizer
```
# useage
* initialization and cleaning
```python
# import
from bnunicodenormalizeri import Normalizer 
# initialize
bnorm=Normalizer()
# normalize
text='াটোবাকো কোম্পানি'
normalized_text=bnorm(text)
print(f"Non-norm:{text}; Norm:{normalized_text}")
```
> Non-norm:াটোবাকো কোম্পানি; Norm:টোবাকো কোম্পানি

* allow to use english text

```python
# initialize without english (default)
norm=Normalizer()
print("without english:",norm("ASD 123"))
# --> returns None
norm=Normalizer(use_english=True)
print("with english:",norm("ASD 123"))
```
> log:normalized text can not be formed for ASD 123

> without english: None

> with english: ASD 123

# Cases

**In all examples (a) is the non-normalized form and (b) is the normalized form**

*  Broken Vowel and consonanr diacritics
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
* Broken nukta unicode
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
* Invalid hosontos that come after / before the vowels and the modifiers
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
```
* Invalid hosonto is in between two vowel diacritics 
``` 
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
```
* 'ত'+hosonto 
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
* Unwanted consecutive double diacritics
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


* vowels followed by vowel diacritics
```
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
# Example-2:
(a)একএ==(b)একত্র-->False
    (a) breaks as ['এ', 'ক', 'এ']
    (b) breaks as ['এ', 'ক', 'ত', '্', 'র']
```             
* Repeated consonant diacritics (folas)
```
# Example-1:
(a)গ্র্রামকে==(b)গ্রামকে-->False
    (a) breaks as ['গ', '্', 'র', '্', 'র', 'া', 'ম', 'ক', 'ে']
    (b) breaks as ['গ', '্', 'র', 'া', 'ম', 'ক', 'ে']
```
* Removes invalid starts and ends

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
        self.assertEqual(norm('ASD1234'),None)
        self.assertEqual(ennorm('ASD1234'),'ASD1234')
        # random
        self.assertEqual(norm('িত'),'ত')
        self.assertEqual(norm('সং্যুক্তি'),"সংযুক্তি")
        # Ending
        self.assertEqual(norm("অজানা্"),"অজানা")
        #--------------------------------------------- insert your assertions here----------------------------------------
        '''
            ###  case: give a comment about your case
            ## (a) invalid text==(b) valid text <---- an example of your case
            self.assertEqual(norm(invalid text),expected output)
                        or
            self.assertEqual(ennorm(invalid text),expected output) <----- for including english text
            
        '''
        # your case goes here
    ```
    * perform the unit testing
    * make sure the unit test fails under true conditions    

# ABOUT US
* Authors: [Bengali.AI](https://bengali.ai/)
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