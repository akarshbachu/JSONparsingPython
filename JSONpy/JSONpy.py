import json
#json Objects indicated by {}
#its a json object, in which it contains key value pairs
# name is key and value is string
# phone is key and value is object
# email is key and value is object
data='''{
"name":"Akarsh",
"phone":{
"type":"intl",
"number":"+917729862405"
   },
"email":{
    "hide":"yes"
   }
}'''

info=json.loads(data)#deserialize, it returns dictionary
print 'Name:',info["name"]
print 'Hide:',info["email"]["hide"]

#Json Lists indicated by []
#below is the list of two comma seperated objects like this [{},{}]
input='''[
    {
        "id":"001",
        "x":"1",
        "name":"Akarsh"
    },
    {
        "id":"002",
        "x":"2",
        "name":"Harun"
    }

]'''
info1=json.loads(input)
print len(info1),"----------"
for item in info1:
    print 'Name: ',item['name']
    print 'id: ',item['id']