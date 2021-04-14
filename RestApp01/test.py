import requests

BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apijson'
resp=requests.get(BASE_URL+ENDPOINT)
data= resp.json()
print('#'*40)
print('Data is getting Now by the application')
print('#'*40)
print('Employe Number:',data['eno'])
print('Employe Name:',data['ename'])
print('Employe Salaer:',data['esal'])
print('Employe Addres:',data['eaddr'])
print('#'*22)
print('Thank You ')