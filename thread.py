# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 23:44:51 2020

@author: scaryalberto
descriptions: come effettuare il multithreading
"""


#http://www.andreaminini.com/python/il-modulo-threading-di-python
from threading import Thread


class Lancio (Thread):
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    
    def run(self):
        #print ("Thread '" + self.nome + "' inizio")
        print ("Thread '" + self.nome + "' fine")
        






class Analisi (nomeFile, Thread): #analizziamo la 1a directory
    def __init__(self, nome):
        Thread.__init__(self)
        self.nome = nome
    
    def run(self):
        #print ("Thread '" + self.nome + "' inizio")
        print ("Thread '" + self.nome + "' fine")
        
    def carica(nomeFile):
        file = open(nomeFile, 'r', encoding='utf-8') #file .txt
        return file


#nel costruttore passo la direcory
        

#thread1 = Lancio("prova 1")
#thread1.start()
thread2 = Analisi('ciao.txt', "prova 2")
thread2.start()











