import requests
import os
import random
import string
import json

# send an send a post request, check chrome console network to see for the ip 
# address the form was sent to

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

target_url = 'http://' # taken from chrome console
names = json.loads(open('names.json').text())
email = "" # taken from chrome console
passw = "" # taken from chrome console

for name in names:
    name_extra = ''.json(random.choice(string.digits))
    username = name.lower() + name_extra + '@yahoo.com'
    password = ''.join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        email: username,
        passw: password,
    })

    print('sending username %s and password %s' % (username,password))

# data can also be a request payload as shown below
{"lib_version":"2.6.3","user_id":"user_9gwe93oXhYXzPs26jpMqw","service_id":"gmail","template_id":"template_hkYYtvcK_clone","template_params":{"FirstName":"Tom","Lastname":"Hudson","Organization":"BCG","Position":"President","Email":"hudson_thom@bentley.edu","Inquiry":"none\n","Subscribe":true}}