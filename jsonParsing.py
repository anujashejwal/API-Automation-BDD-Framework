import json

courses='{"name":"RahulShetty","languages":["Java","Python"]}'

#Load method to parse json string and it returns dictionary

#json.load() reads JSON from a file
#json.loads() reads JSON from a string

dict_courses = json.loads(courses)
print(type(dict_courses))
print(dict_courses)
print(dict_courses["name"])
print(dict_courses["languages"][0])

#parse content present in the json file
with open('course.json') as f:
    data = json.load(f)
    print(data)
    print(data['courses'][1]['title'])
    print(data['dashboard']['website'])
    print(type(data['dashboard']))

#price of course RPA
    print(type(data['courses'])) #list
    for c in data['courses']:
        if c['title'] == 'RPA':
            print(c['price'])

with open('course2.json') as f1:
    data2 = json.load(f1)

    assert data == data2


