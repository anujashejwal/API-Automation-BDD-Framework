#POST is an HTTP method used to send data to a server to create something new.

#performs:
#1. Read base URL from config
#2. Get endpoint from resources
#3. Build payload dynamically
#4. Send POST request
#5. Extract Book ID
#6. Send DELETE request
#7. Validate delete response

import json
import configparser
from payLoad import *
from utilities.resources import *
from utilities.configurations import *

import requests
#
url = getConfig()['API']['endpoint'] + ApiResources.addBook
headers = {"Content-Type": "application/json"}
query = 'select * from Books'
addBook_response = requests.post(url,json=addBookPayload("mant"),headers=headers, )
print(addBook_response.json())
response_json = addBook_response.json()
print(type(response_json))

bookId = response_json['ID']
print(bookId)
# Delete Book -
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={

    "ID": bookId
}, headers={"Content-Type": "application/json"},
                                    )

assert response_deleteBook.status_code == 200
res_json = response_deleteBook.json()

print(res_json["msg"])
assert res_json["msg"] == "book is successfully deleted"



#Authentication
se = requests.Session()
se.auth = auth=('abc@gmail.com', getPassword())

url = 'https://api.github.com/user'
github_response = se.get(url,verify=False, auth=('abc@gmail.com', getPassword()))
print(github_response.status_code)

url2 = 'https://api.github.com/user/repos'
response = se.get(url2,verify=False,auth=('abc@gmail.com', getPassword()))
print(response.status_code)