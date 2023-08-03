import time as t
import numpy as np
import os


def run():
    a = "a"
    if a == "a":
        print("welcome to quick.text!")
        print("")
        t.sleep(0.34)
        print("what do u wanna do?")
        print("1. open existing file")
        print("2. create new file")
        print("3. delete file")
        print("4. QUIT")
        ans = str(input())
        if ans == "1" or ans == "1." or ans == "open existing file" or ans == "open file":
            ans = str(input("which file do u wanna open?(without file extension) "))
            ans = ans + ".npy"
            file = np.load(ans)
            print(file)
            print("what do u wanna do next?")
            print("1. edit this file")
            print("2. go back to quick.txt menu")
            print("(please type only the number bcs why fingers cant type anymore THANK U :)")
            ans1 = str(input())
            if ans1 == "1" or ans1 == "1.":
                nfile = file + str(input(file))
                np.save(ans, nfile)
                run()
            else:
                run()

        if ans == "2" or ans == "2." or ans == "create new file" or ans == "create file":
            ans = str(input("how  to u wanna name ur file?"))
            nfile = input(ans + ": ")
            nfilewe = ans + ".npy"
            np.save(nfilewe, nfile)
            run()

        if ans == "3." or ans == "3" or ans == "delete file":
            os.remove(
                "data0/" + input("which file do u wanna delete? (note: don't delete any of cntcs files)") + ".npy",
                dir_fd=None)

        if ans == "4." or ans == "4" or ans == "quit" or ans == "QUIT":
            return
