# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:10:15 2020

@author: Utente
"""

import fasttext
import fasttext.util

fasttext.util.download_model('it', if_exists='ignore')
#ft = fasttext.load_model('cc.en.300.bin')

#https://dl.fbaipublicfiles.com/fasttext/vectors-wiki/wiki.it.zip