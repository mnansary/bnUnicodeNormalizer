
#-*- coding: utf-8 -*-
"""
@author:Bengali.ai
"""
#------------------------------------------------------------
from __future__ import print_function
#------------------------------------------------------------
from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='bnunicodenormalizer',
  version='0.0.23',
  description='Bangla Unicode Normalization Toolkit',
  long_description=open('README.md',encoding='utf-8').read() + '\n\n' + open('CHANGELOG.txt',encoding='utf-8').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/mnansary/bnUnicodeNormalizer',  
  author='Bengali.AI',
  author_email='research.bengaliai@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['bangla','unicode','text normalization'], 
  packages=find_packages(),
  install_requires=[''] 
)