import os
import shutil as shtl


def delfile():
    file = input('file:')
    if os.path.exists(file):
        os.remove(file, dir_fd=None)
    else:
        print('file doesnt exist!')


def deldir():
    directory = input('sub-directory:')
    if os.path.exists(directory):
        yn = input('are you sure you want to delete "' + directory + '"? y/n ')
        if yn == 'y' or yn == 'yes':
            shtl.rmtree(directory)
        else: print('operation canceled!')
    else:
        print('directory doesnt exist!')


def createdir():
    os.mkdir(input('dir name: '))


def createfile():
    file = open(input('file name: '), "x")
    file.close()


def read():
    file = open(input('file name: '), "r")
    print(file.read())
    file.close()


def ls():
    print(os.listdir(os.getcwd()))


def rename():
    os.renames(input('file:'), input('new name:'))


def cd():
    ndir = input('new dir: ')
    if ndir == '..':
        os.chdir(os.path.dirname(os.getcwd()))
    else:
        os.chdir(ndir)


def echo():
    print(input('what do you want to print?'))


def clear():
    for i in range(1,500):
        print()
        