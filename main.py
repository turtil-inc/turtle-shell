import os

from programs import betterfetch as bf
from programs import cntcs as c
from programs import quick_text as qt
from programs import gamework as gw
from programs import system as s
from programs import printer as p
from programs import xget as xg
from programs import zippy as z


def help():
    print('exit: exits')
    print('betterfetch: prints out customizable info about the system and a customizable ascii art.')
    print('help or h: helps you')
    print('cntcs or contacts: a basic digital contact book')
    print('quick_text: a basic text editor')
    print('ttt or tic tac toe: a basic tic tac toe game!')
    print('delf: deletes file')
    print('deldir: deletes directory')
    print('mkdir: creates directory')
    print('mkfile: creates file')
    print('rd: reads file')
    print('ls: lists sub-directories in current folder')
    print('rnm: renames folder or directory')
    print('cd: changes directory. if input == ".." it changes to the parent dir')
    print('echo: prints ur outgoing input')
    print('clear: clears ur console')
    print('printer: a "printer"')
    print('webget: install a package/file in ypur current directory')
    print('sapp: installs a sh*ty a*s python package')
    print('sapp lp: lists all sapp packages')


def shell():
    print('')
    while True:
        crntdir = os.getcwd()
        i = str(input(crntdir + '=>'))
        if i == 'h' or i == 'help':
            help()
        elif i == 'betterfetch':
            bf.run()
        elif i == 'exit':
            print('exiting...')
            return
        elif i == 'cntcs' or i == 'contacts':
            c.run()
        elif i == 'quit_text':
            qt.run()
        elif i == 'ttt' or i == 'tic tac toe':
            gw.ttt()
        elif i == 'delf':
            s.delfile()
        elif i == 'deldir':
            s.deldir()
        elif i == 'mkdir':
            s.createdir()
        elif i == 'mkfile':
            s.createfile()
        elif i == 'rd':
            s.read()
        elif i == 'ls':
            s.ls()
        elif i == 'rnm':
            s.rename()
        elif i == 'cd':
            s.cd()
        elif i == 'echo':
            s.echo()
        elif i == 'clear':
            s.clear()
        elif i == 'printer':
            p.run()
        elif i == 'sapp':
            xg.sapp()
        elif i == 'webget':
            xg.webget()
        elif i == 'unzip':
            z.unzip()
        else:
            print('Module "' + i + '" not found. Try again')


s.clear()
shell()
