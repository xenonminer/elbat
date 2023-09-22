import requests

# Uploading a file to web server
def upload_file(url, file, headers):
    files = {'file': open(file, 'rb')}
    r = requests.post(url, files=files, headers=headers)
    return r.text

# Downloading a file from web server
def download_file(url, headers):
    r = requests.get(url, headers=headers)
    return r.content