# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:28:43 2020

@author: Utente

descrizione: http server con Flask
"""

#https://www.youtube.com/watch?v=b9BYA483yVI&t=441s -> guida flask
    
from flask import Flask #NB. il file non si deve chiamare flask.py

app = Flask("__name__")

@app.route("/")
def hello():
    return "Hello, World!"







if __name__=="__main__":
	app.run()
    
    
    
    
    
    