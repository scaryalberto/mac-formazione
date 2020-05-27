import requests #
r = requests.get('http://echo.jsontest.com/key/value/one/two')
print(r.text) # contenuto della risposta HTTP
print(r.json) # oggetto JSON
print(r.status_code) # codice di status
print(r.headers) # informazione contenuta negli headers della risposta
print(r.history) # informazioni sui reindirizzamenti