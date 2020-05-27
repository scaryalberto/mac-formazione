# -*- coding: utf-8 -*-
"""
Created on Fri May  1 15:00:56 2020

@author: scaryalberto

descriptions: inviare e mail con Python usando il protocollo 
"""

#SMTP = È un protocollo testuale relativamente semplice, nel quale vengono specificati uno o più destinatari di un messaggio e, dopo aver verificato la loro esistenza, il messaggio viene trasferito. 

import email
import smtplib

msg = email.message_from_string('Coropo della mail')
msg['From'] = "scaryalberto@hotmail.it"
msg['To'] = "lucacaligione1994@gmail.com"
msg['Subject'] = "Oggetto della mail"

s = smtplib.SMTP("smtp.live.com",587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('scaryalberto@hotmail.it', 'INSERIRE PASSWORD')

s.sendmail("scaryalberto@hotmail.it", "scaryalberto@hotmail.it", msg.as_string()) #da -> a

s.quit()