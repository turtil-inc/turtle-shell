import wget
import os
import zipfile as zf


# SETTINGS:
# program directory(sapp):
# NOTE: if letting sappdir blank it will ask you every time where u want to install the sapp package!!!
sappdir = ''


# NOTE: THIS IS A GITHUB INSTALLER BASED ON WGET!!!
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
    if sapp == 'test':
        pkg = 'https://github.com/nikkit001/test/archive/refs/heads/main.zip'
        branch = 'main'
        pkgfound = True
    else: pkgfound = False
    if pkgfound == True:
        wget.download(pkg)
        with zf.ZipFile(sapp + '-' + branch + '.zip') as f:
            f.extractall()
    else: print('package not found')

        
def webget():
    url = input('url: ')
    wget.download(url)
