#-*- coding: utf-8 -*-
"""
@author:MD.Nazmuddoha Ansary
"""
from __future__ import print_function
#-------------------------------------------
# imports
#-------------------------------------------
import os 
import unittest
from bnunicodenormalizer import Normalizer
norm=Normalizer(use_english=False)
ennorm=Normalizer(use_english=True)
#-------------------------------------------
# unittestcase
#-------------------------------------------
class TestWordCleaner(unittest.TestCase):
    def test_values(self):
        '''
            test known failure cases
        '''
        # case:unwanted doubles
        ## (a)'যুুদ্ধ'==(b)'যুদ্ধ'
        self.assertEqual(norm('যুুদ্ধ'),'যুদ্ধ')
        ## (a)'দুুই'==(b)'দুই'
        self.assertEqual(norm('দুুই'),'দুই')
        # case:unwanted middle connector '্'  
        ## (a)'চু্ক্তি'==(b)'চুক্তি' 
        self.assertEqual(norm('চু্ক্তি'),'চুক্তি')
        ## (a)'যু্ক্ত'==(b)'যুক্ত' 
        self.assertEqual(norm('যু্ক্ত'),'যুক্ত')
        # case: replace broken diacritic 
        ## (a)'আরো'==(b)'আরো'
        self.assertEqual(norm('আরো'),'আরো')
        ## (a)'পৌঁছে'== (b)'পৌঁছে'
        self.assertEqual(norm('পৌঁছে'),'পৌঁছে')
        ## (a)সংস্কৄতি==(b)সংস্কৃতি
        self.assertEqual(norm('সংস্কৄতি'),'সংস্কৃতি')
        # case: nukta  
        ## (a)কেন্দ্রীয়==(b)কেন্দ্রীয়
        self.assertEqual(norm('কেন্দ্রীয়'),'কেন্দ্রীয়')
        ## (a)রযে়ছে==(b)রয়েছে
        self.assertEqual(norm('রযে়ছে'),'রয়েছে')
        ## (a)জ়ন্য==(b)জন্য
        self.assertEqual(norm('জ়ন্য'),'জন্য')
        ## missed case
        self.assertEqual(norm('য়'),'য়')

        # case: invalid hosonto after or before symbols
        ## (a)এ্তে==(b)এতে
        self.assertEqual(norm('এ্তে'),'এতে')
        ##(a)নেট্ওয়ার্ক==(b)নেটওয়ার্ক
        self.assertEqual(norm('নেট্ওয়ার্ক'),'নেটওয়ার্ক')
        
        ### case: Vowel Diacs after vowels (Also Normalizes 'এ' and 'ত্র')
        ## (a)উুলু==(b)উলু
        self.assertEqual(norm('উুলু'),'উলু')
        ## (a)একএে==(b)একত্রে
        self.assertEqual(norm('একএে'),'একত্রে')
        ## (a)একএ==(b)একত্র
        self.assertEqual(norm('একএ'),'একত্র')
        
        ### case: normalize to+hosonto
        ## (a)উত্স==(b)উৎস
        self.assertEqual(norm('উত্স'),'উৎস')
        ## স্নাতকোত্ত্তর
        self.assertEqual(norm('স্নাতকোত্ত্তর'),'স্নাতকোৎত্তর')
        
        
        ### case: multiple folas
        self.assertEqual(norm('ন্দ্ব্ব্ব্ব্ব'),'ন্দ্ব')
        

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
        
    def test_types(self):
        '''
            test the invalid input types
        '''
        # int
        self.assertRaises(TypeError,norm,123)
        # float
        self.assertRaises(TypeError,norm,123.456)
        # boolean
        self.assertRaises(TypeError,norm,True)
        # complex
        self.assertRaises(TypeError,norm,3+4j)
        # list
        self.assertRaises(TypeError,norm,['যুদ্ধ','চুক্তি'])

        
        
        


        
        
        
                


                
                