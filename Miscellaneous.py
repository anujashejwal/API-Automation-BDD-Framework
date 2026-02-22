import requests

# http://rahulshettyacademy.com
# 'visit-month'

# Cookie = small key-value data sent to server to remember client info.

cookie = {'visit-month': 'February'}
response = requests.get('http://rahulshettyacademy.com', allow_redirects=False, cookies=cookie, timeout=1)
# 301,200
# print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})

res = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
print(res.text)

# Attachments
url = "https://petstore.swagger.io/v2/pet/64/uploadImage"
files = {'file': open('/Users/anujashejwal/Downloads/cat.jpg', 'rb')}
#rb read binary, mandatory for files
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)

#| Parameter               | Meaning                     |
#| ----------------------- | --------------------------- |
#| URL                     | Website you’re calling      |
#| `cookies=cookie`        | Send cookie with request    |
#| `allow_redirects=False` | Don’t auto-follow redirects |
#| `timeout=1`             | Wait max 1 second           |
