# -*- coding: utf-8 -*-
"""
Created on Sat May  2 11:59:14 2020

@author: scarylberto

descrizione: get file from ftp server

"""
# ftp-ex.py

import os
from ftplib import FTP


import socket
socket.getaddrinfo('ftp.fu-berlin.de', 21)

#link sito, username, password
ftp = FTP("ftp.fu-berlin.de", "", "") #la porta se non è criptata è 21, altrimenti 22 #ftp://ftp.fu-berlin.de
ftp.login()
ftp.retrlines("LIST")

#ftp.cwd("folderOne")
#ftp.cwd("doc/") # se voglio accedere ad una sottocartella

listing = []
ftp.retrlines("LIST", listing.append)


words = listing[0].split(None, 8)
filename = words[-1].lstrip()


#download the file
    
filename = words[-1].lstrip() 


#filename= #ed inseriamo a mano il nome del file desiderato
    
local_filename = os.path.join(r"C:\Users\Utente\Desktop\mac formazione python\salva_file_ftp_di_Berlino", filename)  #dove salvo?
lf = open(local_filename, "wb")
ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
lf.close()


