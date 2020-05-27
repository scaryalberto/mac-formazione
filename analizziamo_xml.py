# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:47:51 2020

@author: scaryalberto

descriptions: analizziamo xml
"""

#https://docs.python.org/3.4/library/xml.etree.elementtree.html

#We can import this data by reading from a file:
import xml.etree.ElementTree as ET
tree = ET.parse('file2.xml')
root = tree.getroot()


#root, come elemento, ha un tag e un dictionary di attributi:
root.tag
root.attrib#che però è vuoto adesso

#volendo, possiamo anche iterare sui nodi figli (scendiamo di un livello)
for child in root:
    print(child.tag, child.attrib)
    
    
#per accedere agli specifici elementi dei nodi figli, dobbiamo usare gli indici
root[0][1].text #0 indica il country, ed 1 year(il 2o nodo... del 1o nodo)


#accediamo a tutti gli elementi di uno specifico nodo
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)


#Element.findall() finds only elements with a tag which are direct children of the current element.
for country in root.findall('country'):
    
    rank = country.find('rank').text # Element.find() finds the first child with a particular tag
    name = country.get('name') # and Element.text accesses the element’s text content. Element.get() accesses the element’s attributes
    print(name, rank)



#modificare un file xml (ggiungendo un elemento)
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank)
    rank.set('updated', 'yes')
tree.write('output.xml')


#rimuoviamo un elemento (il paese con il rank superiore a 50)
for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank > 50:
      root.remove(country)
 
tree.write('output.xml')

#estrarre testo da xml: https://stackoverflow.com/questions/7691514/extracting-text-from-xml-using-python








    