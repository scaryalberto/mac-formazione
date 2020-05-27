# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:26:39 2020

@author: Utente
"""
import xmlrpclib
server = xmlrpclib.Server('http://localhost:8080')
msg = "Ich bin Giasone"
print(server.tellme(msg))







