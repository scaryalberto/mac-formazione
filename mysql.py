# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 21:32:51 2020

@author: Utente


description:
Connessione a un server MySQL
Creare un database MySQL
Aggiungere elementi a un database MySQL
"""
#https://www.html.it/pag/64159/python-api-per-laccesso-al-db/

import MySQLdb #pip install MySQL-python


#nome database: test
#nome utente: root
#password: password


'''
Se il database non è stato creato svolgere le seguenti righe di codice
db = MySQLdb.connect("localhost","admin","alberto")
mycursor=db.cursor()
mycursor.execute("CREATE DATABASE testdatabase") #NB: se il database non è stato creato svolgere prima
'''


# Connessione al Database
db = MySQLdb.connect("localhost","admin","alberto","testdatabase" )

#Ottenimento del cursore
mycursor=db.cursor()


#creiamo un dataset Persons con tante colonne
mycursor.execute('''CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
)''') #The PersonID column is of type int and will hold an integer. The LastName, FirstName, Address, and City columns are of type varchar and will hold characters, and the maximum length for these fields is 255 characters. The empty "Persons" table will now look like this:

#inseriamo un valore
mycursor.execute(''' INSERT INTO Persons VALUES (1, 'Scaringi', 'Alberto', 'Via Paciotti', 'Roma')''')



print(mycursor.rowcount, "Record inserted successfully into Laptop table")



#https://www.youtube.com/watch?v=91iNR0eG8kE -> creiamo un database con tutte le caratteristiche



# Esecuzione di una query SQL
mycursor.execute("SELECT VERSION()")
# Lettura di una singola riga dei risultati della query
data = mycursor.fetchone()
print("Database version : %s " % data)
# Disconnessione
db.close()
