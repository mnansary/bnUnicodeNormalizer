#-*- coding: utf-8 -*-
"""
@author:MD.Nazmuddoha Ansary
"""
from __future__ import print_function
#-------------------------------------------
# imports
#-------------------------------------------
import os
from tabnanny import verbose 
import unittest
from bnunicodenormalizer import Normalizer
norm=Normalizer(allow_english=False)
ennorm=Normalizer(allow_english=True)
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
        self.assertEqual(norm('যুুদ্ধ')["normalized"],'যুদ্ধ')
        ## (a)'দুুই'==(b)'দুই'
        self.assertEqual(norm('দুুই')["normalized"],'দুই')
        # case:unwanted middle connector '্'  
        ## (a)'চু্ক্তি'==(b)'চুক্তি' 
        self.assertEqual(norm('চু্ক্তি')["normalized"],'চুক্তি')
        ## (a)'যু্ক্ত'==(b)'যুক্ত' 
        self.assertEqual(norm('যু্ক্ত')["normalized"],'যুক্ত')
        # case: replace broken diacritic 
        ## (a)'আরো'==(b)'আরো'
        self.assertEqual(norm('আরো')["normalized"],'আরো')
        ## (a)'পৌঁছে'== (b)'পৌঁছে'
        self.assertEqual(norm('পৌঁছে')["normalized"],'পৌঁছে')
        ## (a)সংস্কৄতি==(b)সংস্কৃতি
        self.assertEqual(norm('সংস্কৄতি')["normalized"],'সংস্কৃতি')
        # case: nukta  
        ## (a)কেন্দ্রীয়==(b)কেন্দ্রীয়
        self.assertEqual(norm('কেন্দ্রীয়')["normalized"],'কেন্দ্রীয়')
        ## (a)রযে়ছে==(b)রয়েছে
        self.assertEqual(norm('রযে়ছে')["normalized"],'রয়েছে')
        ## (a)জ়ন্য==(b)জন্য
        self.assertEqual(norm('জ়ন্য')["normalized"],'জন্য')
        ## missed case
        self.assertEqual(norm('য়')["normalized"],'য়')

        # case: invalid hosonto after or before symbols
        ## (a)এ্তে==(b)এতে
        self.assertEqual(norm('এ্তে')["normalized"],'এতে')
        ##(a)নেট্ওয়ার্ক==(b)নেটওয়ার্ক
        self.assertEqual(norm('নেট্ওয়ার্ক')["normalized"],'নেটওয়ার্ক')
        
        ### case: Vowel Diacs after vowels (Also Normalizes 'এ' and 'ত্র')
        ## (a)উুলু==(b)উলু
        self.assertEqual(norm('উুলু')["normalized"],'উলু')
        ## (a)একএে==(b)একত্রে
        self.assertEqual(norm('একএে')["normalized"],'একত্রে')
        
        ### case: normalize to+hosonto
        ## (a)উত্স==(b)উৎস
        self.assertEqual(norm('উত্স')["normalized"],'উৎস')
        ## স্নাতকোত্ত্তর
        self.assertEqual(norm('স্নাতকোত্ত্তর')["normalized"],'স্নাতকোৎত্তর')
        ## বিদ্য্ৎু
        self.assertEqual(norm('বিদ্য্ৎু')["normalized"],'বিদ্যুৎ')
        ## 'ভর্ৎসনা'
        self.assertEqual(norm('ভর্ৎসনা')["normalized"],'ভরৎসনা')
        
        
        
        
        
        ### case: multiple folas
        self.assertEqual(norm('ন্দ্ব্ব্ব্ব্ব')["normalized"],'ন্দ্ব')

        ### case: complex roots
        self.assertEqual(norm('আকাক্ক্ঙ্ষা')["normalized"],'আকাক্কঙষা')
        

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

        
        
        


        
        
        
                


                
                