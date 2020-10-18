# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 12:04:10 2020

@author: Jimit
"""

import requests

r = requests.get('http://www.google.com/ping?sitemap=https://jimit105.github.io/pytricks/sitemap.xml')

if r.status_code == 200:
    print('Successfully informed Google for updated sitemap')
else:
    print('Error while submitting sitemap to Google')
    