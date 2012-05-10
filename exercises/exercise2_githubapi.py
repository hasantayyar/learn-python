import requests
#call guthub api and get user info
url = 'https://api.github.com/user'
auth = ('hasantayyar', 'passwordpassword')

r = requests.get(url, auth=auth)
print r.content
