import praw
import requests
import json
#TODO limit rate to 60 request per minute

#Open the json file, load it's contents into a JSON object
loginFile = open('login.json')
loginCreds = json.load(loginFile)

#Close the file for good measure
loginFile.close()

#Load the credentials from the JSON object into our variables
username = loginCreds['username']
password = loginCreds['password']
secretToken = loginCreds['secretToken']

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
auth = requests.auth.HTTPBasicAuth('lsdm-project', secretToken)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': username,
        'password': password}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)