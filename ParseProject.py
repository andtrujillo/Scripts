# Python version: 3
# How to install:
# https://realpython.com/installing-python/
# ********************************************
# Script Author: 1713@holbertonschool.com
# Script Purpose: To parse project guidelines to paste at the top of your code.
# Imports: Beautiful Soup
# Function: Prints parse project source to text.
# References: realpython.org, crummy.com/software/beautifulsoup/bs4/doc
# =-=-=-=-==-=-=-===-=-=-=-=-=-=-=-=-=-=-=-=-=
# MIT LICENSE 3.0

# Instructions
# 1. Paste your project source code between the three double quotes. 
# 2. Linux
#	2a.python3 ./filename.py
# 3. Windows 
#	3. python filename.py
#**********************************************


html_doc=\
"""




"""
my_url = open('source.html', 'r')

import os
from bs4 import BeautifulSoup
soup = BeautifulSoup (my_url, 'html.parser')


#print(soup.get_text())


with open('url.txt', 'w', encoding='utf-8') as f__:
	f__.write(str(soup.get_text()))

os.system("./ProjectParser.sh")

