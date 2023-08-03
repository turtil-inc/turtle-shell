import numpy as np
import os

# SETTINGS:
# cntcs programdata directory:
prgrmdata = '/Volumes/2 TB/pogmanieren/python/cmdPIE/programs/programdata/cntcs/'


def save():
    global names
    np.save(prgrmdata + 'names.npy', names)
    global numbers
    np.save(prgrmdata + 'numbers.npy', numbers)
    global addresses
    np.save(prgrmdata + 'addresses.npy', addresses)
    global extras
    np.save(prgrmdata + 'extras.npy', extras)
    global extrasYN
    np.save(prgrmdata + 'extrasYN.npy', extrasYN)


def run():
    print(os.getcwd())
    print("loading contacts...")
    global names
    global numbers
    global addresses
    global extras
    global extrasYN
    names = np.load(prgrmdata + 'names.npy')
    numbers = np.load(prgrmdata + 'numbers.npy')
    addresses = np.load(prgrmdata + 'addresses.npy')
    extras = np.load(prgrmdata + 'extras.npy')
    extrasYN = np.load(prgrmdata + 'extrasYN.npy')
    print(" ")
    print("hi and welcome to cntcs!")
    print("what do u want to do?")
    while True:
        print("1. list contacts")
        print("2. create new contact")
        print("3. delete existing contact")
        print("4. open contact information")
        print("5. QUIT")
        cntcspt2 = str(input()).lower()
        if cntcspt2 == "1." or cntcspt2 == "1" or cntcspt2 == "list contacts":
            print(names)
        if cntcspt2 == "2." or cntcspt2 == "2" or cntcspt2 == "create new contact":
            name = np.array([str(input("How do u want to name ur contact? "))])
            number = np.array([str(input("whats ur new contacts number? "))])
            address = np.array([str(input("whats ur new contacts address? "))])
            extraPROMT = np.array([str(input("any additional info? y/n "))])
            names = np.append(names, name)
            numbers = np.append(numbers, number)
            addresses = np.append(addresses, address)
            if extraPROMT == "y" or extraPROMT == "yes":
                extra = np.array([str(input("extra info: "))])
                extras = np.append(extras, extra)
                extraYN = np.array(True)
                extrasYN = np.append(extrasYN, extraYN)
            else:
                extraYN = np.array(False)
                extrasYN = np.append(extrasYN, extraYN)
            save()

        if cntcspt2 == "3." or cntcspt2 == "3" or cntcspt2 == "quit" or cntcspt2 == "delete existing contact":
            ans = int(input("which contact do u want to delete? "
                            "(type in number starting from 0 BUT NOT THE PHONE NUMBER!!!) "))
            names = np.delete(names, [ans])
            numbers = np.delete(numbers, [ans])
            addresses = np.delete(addresses, [ans])
            if extrasYN[ans]:
                extrasYN = np.delete(extrasYN, [ans])
                extras = np.delete(extras, [ans])
            save()

        if cntcspt2 == "4." or cntcspt2 == "4" or cntcspt2 == "open contact information":
            ans = int(input("which contact do u want to open? "
                            "(type in number starting from 0 BUT NOT THE PHONE NUMBER!!!) "))
            print("name:", names[ans])
            print("number:", numbers[ans])
            print("address:", addresses[ans])
            if extrasYN[ans]:
                print("additional info:", extras[ans])

        if cntcspt2 == "5." or cntcspt2 == "5" or cntcspt2 == "quit" or cntcspt2 == "QUIT":
            break
