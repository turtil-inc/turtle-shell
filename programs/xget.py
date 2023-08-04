import os
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import requests as r
import wget as wg


# SETTINGS:
# program directory(sapp):
# NOTE: if letting sappdir blank it will ask you every time where u want to install the sapp package!!!
sappdir = ''


# NOTE: THIS IS A INSTALLER BASED ON WGET/URLLIB!!!
def sapp():
    global idir
    global pkg
    sapp = input('sapp pkg: ')
    if sappdir == '':
        idir = input('where do u want to install ' + sapp + '?')
        if idir == '' or idir == ' ':
            idir = os.getcwd()
    else:
        idir = sappdir
    response = r.get("https://github.com/turtil-inc/sapp-pkgs/raw/main/"+sapp+".zip")
    if response.status_code == 200:
        pkg = 'https://github.com/turtil-inc/sapp-pkgs/raw/main/'+sapp+'.zip'
        http_response = urlopen(pkg)
        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=idir)

    else: print('package not found')

        
def webget():
    url = input('url: ')
    wg.download(url)

def sapplp():
    wg.download('https://raw.githubusercontent.com/turtil-inc/sapp-pkgs/main/pkg-lists.txt')
    file = open('pkg-lists.txt', "r")
    print('')
    print(file.read())
    file.close()
