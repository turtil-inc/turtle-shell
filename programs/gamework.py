def ttt():
    a1 = ' '
    a2 = ' '
    a3 = ' '
    b1 = ' '
    b2 = ' '
    b3 = ' '
    c1 = ' '
    c2 = ' '
    c3 = ' '
    while True:
        def tbl():
            print('  a | b | c')
            print('1', a1, '|', b1, '|', c1)
            print('2', a2, '|', b2, '|', c2)
            print('3', a3, '|', b3, '|', c3)
        tbl()
        turn = str(input('Enter field id for x: '))
        z = 'x'
        y = 'o'
        if turn == 'a1':
            if a1 == y:
                print('Haha you cant cheat!')
            else:
                a1 = z
        if turn == 'a2':
            if a2 == y:
                print('Haha you cant cheat!')
            else:
                a2 = z
        if turn == 'a3':
            if a3 == y:
                print('Haha you cant cheat!')
            else:
                a3 = z
        if turn == 'b1':
            if b1 == y:
                print('Haha you cant cheat!')
            else:
                b1 = z
        if turn == 'b2':
            if b2 == y:
                print('Haha you cant cheat!')
            else:
                b2 = z
        if turn == 'b3':
            if b3 == y:
                print('Haha you cant cheat!')
            else:
                b3 = z
        if turn == 'c1':
            if c1 == y:
                print('Haha you cant cheat!')
            else:
                c1 = z
        if turn == 'c2':
            if c2 == y:
                print('Haha you cant cheat!')
            else:
                c2 = z
        if turn == 'c3':
            if c3 == y:
                print('Haha you cant cheat!')
            else:
                c3 = z
        if a1 == 'x' and a1 == 'x' and a2 == 'x' and a3 == 'x' or a1 == 'x' and b2 == 'x' and c3 == 'x' or a1 == 'x' and b1 == 'x' and  c1 == 'x' or a3 == 'x' and b2 == 'x' and c1 == 'x' or a1 == 'x' and b1 == 'x' and b2 == 'x' and b3 == 'x' or a1 == 'x' and c1 == 'x' and c2 == 'x' and c3 == 'x':
            yn = input('x won! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
        if a1 == 'o' and a1 == 'o' and a2 == 'o' and a3 == 'o' or a1 == 'o' and b2 == 'o' and c3 == 'o' or a1 == 'o' and b1 == 'o' and  c1 == 'o' or a3 == 'o' and b2 == 'o' and c1 == 'o' or a1 == 'o' and b1 == 'o' and b2 == 'o' and b3 == 'o' or a1 == 'o' and c1 == 'o' and c2 == 'o' and c3 == 'o':
            yn = input('o won! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
        if a1 != ' ' and a2 != ' ' and a3!= ' ' and b1 != ' ' and b2 != ' ' and b3 != ' ' and c1 != ' ' and c2 != ' ' and c3 != ' ':
            yn = input('tie! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
        tbl()
        turn = str(input('Enter field id for o: '))
        z = 'o'
        y = 'x'
        if turn == 'a1':
            if a1 == y:
                print('Haha you cant cheat!')
            else:
               a1 = z
        if turn == 'a2':
            if a2 == y:
                print('Haha you cant cheat!')
            else:
                a2 = z
        if turn == 'a3':
            if a3 == y:
                print('Haha you cant cheat!')
            else:
                a3 = z
        if turn == 'b1':
            if b1 == y:
                print('Haha you cant cheat!')
            else:
                b1 = z
        if turn == 'b2':
            if b2 == y:
                print('Haha you cant cheat!')
            else:
                b2 = z
        if turn == 'b3':
            if b3 == y:
                print('Haha you cant cheat!')
            else:
                b3 = z
        if turn == 'c1':
            if c1 == y:
                print('Haha you cant cheat!')
            else:
                c1 = z
        if turn == 'c2':
            if c2 == y:
                print('Haha you cant cheat!')
            else:
               c2 = z
        if turn == 'c3':
            if c3 == y:
                print('Haha you cant cheat!')
            else:
               c3 = z
        if a1 == 'x' and a1 == 'x' and a2 == 'x' and a3 == 'x' or a1 == 'x' and b2 == 'x' and c3 == 'x' or a1 == 'x' and b1 == 'x' and c1 == 'x' or a3 == 'x' and b2 == 'x' and c1 == 'x' or a1 == 'x' and b1 == 'x' and b2 == 'x' and b3 == 'x' or a1 == 'x' and c1 == 'x' and c2 == 'x' and c3 == 'x':
            yn = input('x won! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
        if a1 == 'o' and a1 == 'o' and a2 == 'o' and a3 == 'o' or a1 == 'o' and b2 == 'o' and c3 == 'o' or a1 == 'o' and b1 == 'o' and c1 == 'o' or a3 == 'o' and b2 == 'o' and c1 == 'o' or a1 == 'o' and b1 == 'o' and b2 == 'o' and b3 == 'o' or a1 == 'o' and c1 == 'o' and c2 == 'o' and c3 == 'o':
            yn = input('o won! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
        if a1 != ' ' and a2 != ' ' and a3 != ' ' and b1 != ' ' and b2 != ' ' and b3 != ' ' and c1 != ' ' and c2 != ' ' and c3 != ' ':
            yn = input('tie! Do you want to play again? y/n ')
            if yn == 'y':
                ttt()
            else:
                return
