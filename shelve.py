# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 00:05:13 2020

@author: Utente

descrizione: shelve è del tutto simile a pikle, am si usa per file piu complessi come i dizionari
"""






import shelve

integers = [1, 2, 3, 4, 5]

with shelve.open('shelf-example', 'c') as shelf:
    shelf['ints'] = integers #mettiamo una chiave, che poi ci verrà stampata in console


#leggi il contenito
with shelve.open('shelf-example', 'r') as shelf:
    for key in shelf.keys():
        print(repr(key), repr(shelf[key]))











