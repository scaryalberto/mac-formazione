# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:08:22 2020

@author: scaryalberto

Aggiungere, recuperare e aggiornare elementi a un file DBM
"""


'''
Quelli che comunemente vengono definiti “file DBM” costituiscono una modalità di memorizzazione dei dati alternativa sia ai database relazionali (es. Mysql), sia ai comuni file di testo: si tratta di file binari nei quali le informazioni vengono salvate in coppie chiave=>valore.
'''
#https://flylib.com/books/en/2.723.1/dbm_files.html
#https://docs.python.org/3/library/dbm.html -> documentazione

import dbm

# creiamo il nostro database 
with dbm.open('dataaaa', 'c') as db:

    # salviamo alcune variabili 
    db[b'hello'] = b'there' #la b ci serve solo per ricordarci che sono e diventeranno bytes
    db['www.python.org'] = 'Python Website'
    db['www.cnn.com'] = 'Cable News Network'
    
    db['www.cnn.com']='grazie al cazzo' #sovrascriviamo semplicemente usando di nuovo il nome della chiave


    # recuperiamo le informazioni come se fosse un dizionario
    print(db.get('www.cnn.com'))

    # Storing a non-string key or value will raise an exception (most
    # likely a TypeError). Per memorizzare dati non stringa usare 'shelve'
    db['www.yahoo.com'] = 4 #in questo caso genererà errore
       

# db is automatically closed when leaving the with statement.
    
    
a = dbm.open('dataaaa','r')
for i in a:
    print(i) #in questo modo otteniamo la lista di chiavi, ed una volta ottenute potremmo recuperare il valore 

    
    
    
    
    
    