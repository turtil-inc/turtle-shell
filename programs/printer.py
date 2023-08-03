def run():
    def main():
        print('which mode do u want to use?')
        print("1. infinite printing")
        print("2. defined number of prints")
        ans = int(input())
        wort = str(input("what do you want to print?"))
        if ans == 1:
            käse = 1
            while True:
                print(str(käse) + ". " + wort)
                int(käse)
                käse = käse + 1
        elif ans == 2:
            print('how often do you want to print"' + wort + '?')
            ans = int(input())
            for käse in range(1, ans + 1):
                print(str(käse) + ". " + wort)
                int(käse)
        else:
            print("try again.")
            print("------------------------------------")

    main()
