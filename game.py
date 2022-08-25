def rating(u):
    if u < 201:
        temp = [10, 20, 0, 0, "new", "noob", 0, 2]  # [win, win21, lose, lose21, rank, rankrod, coins, num]
    elif u < 401 and u > 200:
        temp = [10, 19, -1, -1, "bronze", "bronze", 10, 3]
    elif u < 601 and u > 400:
        temp = [9, 18, -2, -2, "silver", "silver", 50, 4]
    elif u < 801 and u > 600:
        temp = [8, 16, -2, -3, "gold", "gold", 120, 5]
    elif u < 1001 and u > 800:
        temp = [8, 15, -3, -5, "crystal", "crystal", 320, 6]
    elif u < 1201 and u > 1000:
        temp = [7, 13, -4, -7, "diamond", "diamond", 670, 7]
    elif u < 1401 and u > 1200:
        temp = [6, 12, -5, -9, "emerald", "emerald", 1130, 8]
    elif u < 1601 and u > 1400:
        temp = [5, 10, -5, -10, "ruby", "ruby", 1200, 9]
    elif u < 1801 and u > 1600:
        temp = [4, 9, -6, -11, "titan", "titan", 1350, 10]
    elif u < 2001 and u > 1800:
        temp = [4, 8, -6, -12, "platinum", "platinum", 1550, 11]
    elif u < 2201 and u > 2000:
        temp = [3, 7, -7, -13, "legend I", "legend I", 2100, 12]
    elif u < 2401 and u > 2200:
        temp = [2, 5, -8, -15, "legend II", "legend II", 2400, 18]
    elif u < 2601 and u > 2400:
        temp = [1, 2, -9, -18, "legend III", "legend III", 2700, 19]
    elif u < 2801 and u > 2600:
        temp = [0, 0, -10, -19, "legend IV", "legend IV", 3000, 20]
    elif u < 3001 and u > 2600:
        temp = [-2, -1, -11, -20, "legend V", "legend V", 4000, 21]
    else:
        temp = [-4, -2, -13, -21, "legend VI", "legend VI", 5000, 22]
    return temp


def hasdevineshield(lvl, r, k):
    if lvl == '1':
        b = [round(-0.25 * r[k]), 0, 0, 0]
        return random.choice(b)
    elif lvl == '2':
        b = [round(-0.25 * r[k]), 0, 0]
        return random.choice(b)
    elif lvl == '3':
        b = [round(-0.5 * r[k]), 0, 0]
        return random.choice(b)
    elif lvl == '4':
        b = [round(-0.5 * r[k]), 0]
        return random.choice(b)
    elif lvl == 'cheatcoded':
        return -r[k]
    elif lvl == 'cheatcodedcopying':
        return -r[k] - r[k - 2]
    else:
        return 0


def screenappending(num, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s14, s15, s16, s17):
    if num == '1':
        s1.append('  #---------------------#')
        s2.append('  |                     |')
        s3.append('  |                     |')
        s4.append('  |           #         |')
        s5.append('  |          ##         |')
        s6.append('  |         # #         |')
        s7.append('  |           #         |')
        s8.append('  |           #         |')
        s9.append('  |           #         |')
        s10.append(' |           #         |')
        s11.append(' |           #         |')
        s12.append(' |           #         |')
        s13.append(' |           #         |')
        s14.append(' |          ###        |')
    elif num == '2':
        s4.append('  |        ######       |')
        s5.append('  |       #      #      |')
        s6.append('  |               #     |')
        s7.append('  |              #      |')
        s8.append('  |             #       |')
        s9.append('  |          ###        |')
        s10.append(' |         #           |')
        s11.append(' |        #            |')
        s12.append(' |       #             |')
        s13.append(' |       #             |')
        s14.append(' |       #########     |')
    elif num == '3':
        s4.append('  |        ######       |')
        s5.append('  |       #      #      |')
        s6.append('  |               #     |')
        s7.append('  |              #      |')
        s8.append('  |             #       |')
        s9.append('  |          ###        |')
        s10.append(' |             #       |')
        s11.append(' |              #      |')
        s12.append(' |               #     |')
        s13.append(' |       #      #      |')
        s14.append(' |        ######       |')
    elif num == '4':
        s4.append('  |            #        |')
        s5.append('  |            #        |')
        s6.append('  |           ##        |')
        s7.append('  |          # #        |')
        s8.append('  |         #  #        |')
        s9.append('  |        #   #        |')
        s10.append(' |       ########      |')
        s11.append(' |            #        |')
        s12.append(' |            #        |')
        s13.append(' |            #        |')
        s14.append(' |           ###       |')
    elif num == '5':
        s4.append('  |       ########      |')
        s5.append('  |       #      #      |')
        s6.append('  |       #             |')
        s7.append('  |       #             |')
        s8.append('  |       #             |')
        s9.append('  |       # ####        |')
        s10.append(' |       ##    #       |')
        s11.append(' |              #      |')
        s12.append(' |              #      |')
        s13.append(' |       #      #      |')
        s14.append(' |        ######       |')
    elif num == '6':
        s4.append('  |        ######       |')
        s5.append('  |       #      #      |')
        s6.append('  |       #             |')
        s7.append('  |       #             |')
        s8.append('  |       #             |')
        s9.append('  |       # ####        |')
        s10.append(' |       ##    #       |')
        s11.append(' |       #      #      |')
        s12.append(' |       #      #      |')
        s13.append(' |       #      #      |')
        s14.append(' |        ######       |')
    elif num == '7':
        s4.append('  |      ##########     |')
        s5.append('  |      #        #     |')
        s6.append('  |       #      #      |')
        s7.append('  |              #      |')
        s8.append('  |              #      |')
        s9.append('  |             #       |')
        s10.append(' |            #       |')
        s11.append(' |           #         |')
        s12.append(' |           #         |')
        s13.append(' |           #         |')
        s14.append(' |           #         |')
    elif num == '8':
        s4.append('  |        ######       |')
        s5.append('  |       #      #      |')
        s6.append('  |       #      #      |')
        s7.append('  |       #      #      |')
        s8.append('  |        #    #       |')
        s9.append('  |         ####        |')
        s10.append(' |        #    #       |')
        s11.append(' |       #      #      |')
        s12.append(' |       #      #      |')
        s13.append(' |       #      #      |')
        s14.append(' |        ######       |')
    elif num == '9':
        s4.append('  |        ######       |')
        s5.append('  |       #      #      |')
        s6.append('  |       #      #      |')
        s7.append('  |       #      #      |')
        s8.append('  |        #    ##      |')
        s9.append('  |         #### #      |')
        s10.append(' |              #      |')
        s11.append(' |              #      |')
        s12.append(' |              #      |')
        s13.append(' |       #      #      |')
        s14.append(' |        ######       |')
    elif num == '10':
        s4.append('  |       #  ####       |')
        s5.append('  |      ## #    #      |')
        s6.append('  |     # # #    #      |')
        s7.append('  |       # #    #      |')
        s8.append('  |       # #    #      |')
        s9.append('  |       # #    #      |')
        s10.append(' |       # #    #      |')
        s11.append(' |       # #    #      |')
        s12.append(' |       # #    #      |')
        s13.append(' |       # #    #      |')
        s14.append(' |      ##  ####       |')
        s15.append(' |                     |')
        s16.append(' |                     |')
        s17.append(' #---------------------#')


def gameyeah(a, nota, trap):
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nplayer ' + str(
        a) + ':' + '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    p1, p2, no, gameover, deck, lendeck, strg1, strg2, strg3, strg4, strg5, strg6, strg7, strg8, strg9, strg10, strg11, strg12, strg13, strg14, strg15, strg16, strg17, strg1a, strg2a, strg3a, strg4a, strg5a, strg6a, strg7a, strg8a, strg9a, strg10a, strg11a, strg12a, strg13a, strg14a, strg15a, strg16a, strg17a = 0, 0, 0, 1, [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8,
                                         9], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
    if trap == 1:
        deck, lendeck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    while gameover != 0:
        mb111 = tkinter.messagebox.askquestion('card? player turn: ' + a, a + ': take a card?')
        if mb111 == 'yes':
            sbrty = random.choice(lendeck)
            p1 += deck[sbrty]
            screenappending(str(deck[sbrty]), strg1, strg2, strg3, strg4, strg5, strg6, strg7, strg8, strg9, strg10,
                            strg11, strg12, strg13, strg14, strg15, strg16, strg17)
            print(''.join(strg1a) + '\n' + ''.join(strg2a) + '\n' + ''.join(strg3a) + '\n' + ''.join(
                strg4a) + '\n' + ''.join(strg5a) + '\n' + ''.join(strg6a) + '\n' + ''.join(strg7a) + '\n' + ''.join(
                strg8a) + '\n' + ''.join(strg9a) + '\n' + ''.join(strg10a) + '\n' + ''.join(strg11a) + '\n' + ''.join(
                strg12a) + '\n' + ''.join(strg13a) + '\n' + ''.join(strg14a) + '\n' + ''.join(strg15a) + '\n' + ''.join(
                strg16a) + '\n' + ''.join(strg17a) + '\n \nplayer ' + str(
                nota) + ':' + '\n \n \n \n \n \n \n \n \n \nplayer ' + str(a) + ':' + '\n \n' + ''.join(
                strg1) + '\n' + ''.join(strg2) + '\n' + ''.join(strg3) + '\n' + ''.join(strg4) + '\n' + ''.join(
                strg5) + '\n' + ''.join(strg6) + '\n' + ''.join(strg7) + '\n' + ''.join(strg8) + '\n' + ''.join(
                strg9) + '\n' + ''.join(strg10) + '\n' + ''.join(strg11) + '\n' + ''.join(strg12) + '\n' + ''.join(
                strg13))
            del lendeck[-1]
            del deck[sbrty]
            no = 0
        else:
            print(''.join(strg1a) + '\n' + ''.join(strg2a) + '\n' + ''.join(strg3a) + '\n' + ''.join(
                strg4a) + '\n' + ''.join(strg5a) + '\n' + ''.join(strg6a) + '\n' + ''.join(strg7a) + '\n' + ''.join(
                strg8a) + '\n' + ''.join(strg9a) + '\n' + ''.join(strg10a) + '\n' + ''.join(strg11a) + '\n' + ''.join(
                strg12a) + '\n' + ''.join(strg13a) + '\n' + ''.join(strg14a) + '\n' + ''.join(strg15a) + '\n' + ''.join(
                strg16a) + '\n' + ''.join(strg17a) + '\n \nplayer ' + str(
                nota) + ':' + '\n \n \n \n \n \n \n \n \n \nplayer ' + str(a) + ':' + '\n \n' + ''.join(
                strg1) + '\n' + ''.join(strg2) + '\n' + ''.join(strg3) + '\n' + ''.join(strg4) + '\n' + ''.join(
                strg5) + '\n' + ''.join(strg6) + '\n' + ''.join(strg7) + '\n' + ''.join(strg8) + '\n' + ''.join(
                strg9) + '\n' + ''.join(strg10) + '\n' + ''.join(strg11) + '\n' + ''.join(strg12) + '\n' + ''.join(
                strg13))
            no += 1
        if p1 == 21:
            return [a, '21', "won, have a 21!"]
        elif p1 > 21:
            return [nota, '0', 'won, cause the opponent took an extra card!']
        elif no > 1 and p1 == p2 and p2 != 0:
            return ['ddd427456781929', '122334', "players agreed on a deal!"]
        elif no > 3 and p1 > p2:
            return [a, '0', 'won, cause the opponent refused to take a card while having not enough sum!']
        elif no > 3 and p1 < p2:
            return [nota, '0', 'won, cause the opponent refused to take a card while having not enough sum!']
        mb111 = tkinter.messagebox.askquestion('card? player turn: ' + nota, nota + ': take a card?')
        if mb111 == 'yes':
            sbrty = random.choice(lendeck)
            p2 += deck[sbrty]
            screenappending(str(deck[sbrty]), strg1a, strg2a, strg3a, strg4a, strg5a, strg6a, strg7a, strg8a, strg9a,
                            strg10a, strg11a, strg12a, strg13a, strg14a, strg15a, strg16a, strg17a)
            print(
                ''.join(strg1) + '\n' + ''.join(strg2) + '\n' + ''.join(strg3) + '\n' + ''.join(strg4) + '\n' + ''.join(
                    strg5) + '\n' + ''.join(strg6) + '\n' + ''.join(strg7) + '\n' + ''.join(strg8) + '\n' + ''.join(
                    strg9) + '\n' + ''.join(strg10) + '\n' + ''.join(strg11) + '\n' + ''.join(strg12) + '\n' + ''.join(
                    strg13) + '\n' + ''.join(strg14) + '\n' + ''.join(strg15) + '\n' + ''.join(strg16) + '\n' + ''.join(
                    strg17) + '\n \nplayer ' + str(a) + ':' + '\n \n \n \n \n \n \n \n \n \nplayer ' + str(
                    nota) + ':' + '\n \n' + ''.join(strg1a) + '\n' + ''.join(strg2a) + '\n' + ''.join(
                    strg3a) + '\n' + ''.join(strg4a) + '\n' + ''.join(strg5a) + '\n' + ''.join(strg6a) + '\n' + ''.join(
                    strg7a) + '\n' + ''.join(strg8a) + '\n' + ''.join(strg9a) + '\n' + ''.join(
                    strg10a) + '\n' + ''.join(strg11a) + '\n' + ''.join(strg12a) + '\n' + ''.join(strg13a))
            del lendeck[-1]
            del deck[sbrty]
            no = 0
        else:
            print(
                ''.join(strg1) + '\n' + ''.join(strg2) + '\n' + ''.join(strg3) + '\n' + ''.join(strg4) + '\n' + ''.join(
                    strg5) + '\n' + ''.join(strg6) + '\n' + ''.join(strg7) + '\n' + ''.join(strg8) + '\n' + ''.join(
                    strg9) + '\n' + ''.join(strg10) + '\n' + ''.join(strg11) + '\n' + ''.join(strg12) + '\n' + ''.join(
                    strg13) + '\n' + ''.join(strg14) + '\n' + ''.join(strg15) + '\n' + ''.join(strg16) + '\n' + ''.join(
                    strg17) + '\n \nplayer ' + str(a) + ':' + '\n \n \n \n \n \n \n \n \n \nplayer ' + str(
                    nota) + ':' + '\n \n' + ''.join(strg1a) + '\n' + ''.join(strg2a) + '\n' + ''.join(
                    strg3a) + '\n' + ''.join(strg4a) + '\n' + ''.join(strg5a) + '\n' + ''.join(strg6a) + '\n' + ''.join(
                    strg7a) + '\n' + ''.join(strg8a) + '\n' + ''.join(strg9a) + '\n' + ''.join(
                    strg10a) + '\n' + ''.join(strg11a) + '\n' + ''.join(strg12a) + '\n' + ''.join(strg13a))
            no += 1
        if p2 == 21:
            return [a, '21', "won, have a 21!"]
        elif p2 > 21:
            return [nota, '0', 'won, cause the opponent took an extra card!']
        elif no > 1 and p1 == p2 and p1 != 0:
            return ['ddd427456781929', '122334', "players agreed on a deal!"]
        elif no > 3 and p1 < p2:
            return [a, '0', 'won, cause the opponent refused to take a card while having not enough sum!']
        elif no > 3 and p1 > p2:
            return [nota, '0', 'won, cause the opponent refused to take a card while having not enough sum!']


def newbar(lp, lpn):
    temp = [str(lpn), str(lp[1]), str(lp[2]), str(lp[3]), str(lp[4]), str(lp[5]), str(lp[6]), str(lp[7]), str(lp[8]),
            str(lp[9]), str(lp[10]), str(lp[11]), str(lp[12]), str(lp[13]), str(lp[14]), str(lp[15]), str(lp[16]),
            str(lp[17]), str(lp[18]), str(lp[19]), str(lp[20]), str(lp[21]), str(lp[22])]
    temp = ' '.join(temp)
    return temp


def starting(p):
    f = open(p, 'a')
    f.close()
    f = open(p, 'r')
    lines1 = 0
    for k in f:
        lines1 += 1
    f.close()
    if lines1 == 0:
        f = open(p, 'w')
        start = '0 100 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
        f.write(start)
        f.close()
        f = open(p, 'r')
        return f
    else:
        f = open(p, 'r')
        return f


def playersdatafileopen(pl):
    temp = [pl, '.txt']
    temp = ''.join(temp)
    return temp


def countation(nameofplayer):
    countd = 0
    for k in nameofplayer:
        countd += 1
    if countd == 0:
        print('\n---> nickname need to have at least one character!\n')
    elif countd > 20:
        print('\n---> Max is 20 characters!\n')
    else:
        return 'confirmed'


def countationreal(word):
    countd = 0
    for k in word:
        countd += 1
    return countd


def extandation(word, numofextadation):
    numofletters = countationreal(word)
    lenofword = numofextadation - numofletters
    temp = []
    while lenofword != 0:
        temp.append(' ')
        lenofword -= 1
    return ''.join(temp)


import tkinter.messagebox
import random

step, bigspace = ' \n \n \n \n \n', '                                                                    '
if __name__ == '__main__':
    while True:
        confirmidation = 'unconfirmed'
        while confirmidation != 'confirmed':
            player1 = input("enter player nickname #1: ")
            confirmidation = countation(player1)
        print(' ')
        confirmidation = 'unconfirmed'
        while confirmidation != 'confirmed':
            player2 = input("enter player nickname #2: ")
            confirmidation = countation(player2)
        print(step, step, step, step, step, step, step, step, step, step, step, step, step, step)
        pl1, pl2, winstreak1, winstreak2, game, winornot, gamerow = playersdatafileopen(player1), playersdatafileopen(
            player2), 0, 0, 'a', 'a', 1
        while game != '/з':
            fi1, fi2 = starting(pl1), starting(pl2)
            lp1, lp2 = fi1.readlines()[0].split(), fi2.readlines()[0].split()
            lp1[0], lp2[0] = int(lp1[0]), int(lp2[0])
            fi1.close()
            fi2.close()
            players = [player1, player2]
            a = random.choice(players)
            if a == player1:
                nota = player2
            else:
                nota = player1
            print('                                                                                round №' + str(
                gamerow))
            print(
                '_______________________________________________________________________________________________________________________________________________________________________')
            print("                                                                            Game starts with:", a)
            print(
                '_______________________________________________________________________________________________________________________________________________________________________')
            winornot = 'go'
            mb = tkinter.messagebox.askyesnocancel('GAME', 'playing?')
            if mb == True:
                pas = 0
                if lp1[14] != '0':
                    mb34 = tkinter.messagebox.askquestion('trap?',
                                                          player1 + ': setting a trap? (' + str(lp1[14]) + ')')
                    if mb34 == 'yes':
                        lp1[14] = str(int(lp1[14]) - 1)
                        print('Attention! trap has been set!')
                        pas = 1
                if lp2[14] != '0' and pas == 0:
                    mb34 = tkinter.messagebox.askquestion('trap?',
                                                          player2 + ': setting a trap? (' + str(lp2[14]) + ')')
                    if mb34 == 'yes':
                        lp2[14] = str(int(lp2[14]) - 1)
                        print('Attention! trap has been set!')
                        pas = 1
                dfghytresbn = gameyeah(a, nota, pas)
                if dfghytresbn[0] == player1 and dfghytresbn[1] == '0':
                    tkinter.messagebox.showinfo(player1, 'player ' + player1 + ' ' + dfghytresbn[2])
                    winornot = "г1"
                elif dfghytresbn[0] == player2 and dfghytresbn[1] == '0':
                    tkinter.messagebox.showinfo(player2, 'player ' + player2 + ' ' + dfghytresbn[2])
                    winornot = "г2"
                elif dfghytresbn[0] == player2 and dfghytresbn[1] == '21':
                    tkinter.messagebox.showinfo(player2, 'player ' + player2 + ' ' + dfghytresbn[2])
                    winornot = "г221"
                elif dfghytresbn[0] == player1 and dfghytresbn[1] == '21':
                    tkinter.messagebox.showinfo(player1, 'player ' + player1 + ' ' + dfghytresbn[2])
                    winornot = "г121"
                else:
                    winornot = 'u'
            elif mb == False:
                winornot = '0'
                mbshop = tkinter.messagebox.askquestion('store',
                                                        'do you want to enter a store?\nto leave the store enter the command "/к"\nto cancel all purchase before you exited the store - restart the game!')
                if mbshop == 'yes':
                    comd = 'a'
                    while comd != "/к":
                        print(
                            " \n \n \n \n \n#store#")
                        print(
                            '|    ||                                                                                                                                                         ||    |')
                        print(
                            '|    ||                             player ' + player1 + ': ' + str(lp1[1]) + extandation(
                                player1, 20) + extandation(str(lp1[1]), 20) + '  ' + extandation(player2,
                                                                                                 20) + extandation(
                                str(lp2[1]), 20) + ' player ' + player2 + ': ' + str(
                                lp2[1]) + '                     ||    |')
                        print(
                            '|    ||                                                                                                                                                         ||    |')
                        print(
                            '#____##_________________________________________________________________________________________________________________________________________________________##____#')
                        print(
                            '||invebtory                                      ||goods======================================================================||info                             |')
                        print(
                            '|                                               ||                                                                           ||                                       |')
                        print('| player ' + player1 + ':' + extandation(player1,
                                                                         20) + '                 ||                                                                           ||                                       |')
                        print(
                            '|                                               ||                                                                           ||                                       |')
                        print(
                            '|      passive strength "extra  rating"        ||     #---------------------------------------------------------------#     ||                                       |')
                        print(
                            '|                                               ||     |      |passive strength "extra  rating"                       |     ||                                       |')
                        print('|               level: (' + str(lp1[
                                                                    13]) + ')                     ||     |   1  |you get more rating for winning!                |     ||                                       |')
                        print(
                            '|                                               ||     |      |price: 100, 500, 1200, 3000, 10000                       |     ||                                       |')
                        print(
                            '|           passive strength "gilding"             ||     #---------------------------------------------------------------#     ||                                       |')
                        print(
                            '|                                               ||                                                                           ||                                       |')
                        print('|               level: (' + str(lp1[
                                                                    16]) + ')                     ||                                                                           ||                                       |')
                        print(
                            '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                        print(
                            '|       passive strength "royal shield"         ||     |      |one time strength "trap"                                |     ||                                       |')
                        print(
                            '|                                               ||     |   2  |you shuffle a deck of 10th and shuffle it!         |     ||                                       |')
                        print('|               level: (' + str(lp1[
                                                                    17]) + ')                     ||     |      |price: 1750                                              |     ||                                       |')
                        print(
                            '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                        print('|       one time strength "trap"  (' + str(lp1[14]) + ')' + extandation(str(lp1[14]),
                                                                                                        2) + '         ||                                                                           ||                                       |')
                        print(
                            '|                                               ||                                                                           ||                                       |')
                        print('| player ' + player2 + ':' + extandation(player2,
                                                                         20) + '                 ||     #---------------------------------------------------------------#     ||                                       |')
                        print(
                            '|                                               ||     |      |passive strength "gilding"                                 |     ||                                       |')
                        print(
                            '|      passive strength "extra rating"        ||     |   3  |you turn the rating lost by your opponent into gold!  |     ||                                       |')
                        print(
                            '|                                               ||     |      |price: 15000                                             |     ||                                       |')
                        print('|               level: (' + str(lp2[
                                                                    13]) + ')                     ||     #---------------------------------------------------------------#     ||                                       |')
                        print(
                            '|                                               ||                                                                           ||                                       |')
                        print(
                            '|           passive strength "gilding"             ||                                                                           ||                                       |')
                        print(
                            '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                        print('|               level: (' + str(lp2[
                                                                    16]) + ')                     ||     |      |passive strength "royal shield"                         |     ||                                       |')
                        print(
                            '|                                               ||     |   4  |for some chance and percentage reduces the loss of rating!    |     ||                                       |')
                        print(
                            '|       passive strength "royal shield"         ||     |      |price: 10000, 25000, 50000, 100000                       |     ||                                       |')
                        print(
                            '|                                               ||     #---------------------------------------------------------------#     ||             #---------------------#   |')
                        print('|               level: (' + str(lp2[
                                                                    17]) + ')                     ||                                                                           ||             |                     |   |')
                        print(
                            '|                                               ||                                                                           ||       #---------------------#     |   |')
                        print('|        one time strength "trap"  (' + str(lp2[14]) + ')' + extandation(str(lp2[14]),
                                                                                                        2) + '         ||                                                                           ||       |                     |     |   |')
                        print(
                            '|                                               ||                                                                           ||  #---------------------#    |     |   |')
                        print(
                            '|                                               ||                                                                           ||  |                     |    |     |   |')
                        print(
                            '|                                               ||                                                                           ||  |                     |    |     |   |')
                        print(
                            '#_______________________________________________##===========================================================================##__|_____________________|____|_____|___#')
                        comand = input('#                                                 enter command: ')
                        if comand == '/к':
                            comd = "/к"
                        elif comand == '1':
                            print(
                                " \n \n \n \n \n#store_____________________________________________________________________________________________________________________________________________________________#")
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print('|    ||                             player ' + player1 + ': ' + str(
                                lp1[1]) + extandation(player1, 20) + extandation(str(lp1[1]), 20) + '  ' + extandation(
                                player2, 20) + extandation(str(lp2[1]), 20) + ' player ' + player2 + ': ' + str(
                                lp2[1]) + '                     ||    |')
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print(
                                '#____##_________________________________________________________________________________________________________________________________________________________##____#')
                            print(
                                '||inventory                                      ||goods======================================================================||info                             |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player1 + ':' + extandation(player1,
                                                                             20) + '                 ||                                                                           ||          "extra rating"         |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|      passive strength "extra rating"        ||     @@====================================================================@@   type: passive strength (always working out)   |')
                            print(
                                '|                                               ||     ||     |passive strength "extra rating"                                                                      |')
                            print('|               level: (' + str(lp1[
                                                                        13]) + ')                     ||     ||  1  |you will get more rating for wins!                           have 5 levels, level of the strength      |')
                            print(
                                '|                                               ||     ||     |price: 100, 500, 1200, 3000, 10000                                  indicates the amount of extras     |')
                            print(
                                '|           passive strength "gilding"             ||     @@====================================================================@@     rating, that you get       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        16]) + ')                     ||                                                                           ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||    price:                              |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |one time strength "trap"                                |     ||       1st level: 100                 |')
                            print(
                                '|                                               ||     |   2  |you shuffle a deck of 10th and shuffle it!         |     ||       2nd level: 500                 |')
                            print('|               level: (' + str(lp1[
                                                                        17]) + ')                     ||     |      |price: 1750                                              |     ||       3rd level: 1200                |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||       4th level: 3000                |')
                            print(
                                '|        one time strength "trap"  (' + str(lp1[14]) + ')' + extandation(str(lp1[14]),
                                                                                                          2) + '         ||                                                                           ||       5th level: 10000               |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player2 + ':' + extandation(player2,
                                                                             20) + '                 ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||     |      |passive strength "gilding"                                 |     ||     work only if you won     |')
                            print(
                                '|      passive strength "extra rating"        ||     |   3  |you turn the rating lost by your opponent into gold!  |     ||                                       |')
                            print(
                                '|                                               ||     |      |price: 15000                                             |     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        13]) + ')                     ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|           passive strength "gilding"             ||                                                                           ||     take it! you will need it!     |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        16]) + ')                     ||     |      |passive strength "royal shield"                         |     ||                                       |')
                            print(
                                '|                                               ||     |   4  |for some chance and percentage reduces the loss of rating!    |     ||                                       |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |price: 10000, 25000, 50000, 100000                       |     ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||             #---------------------#   |')
                            print('|               level: (' + str(lp2[
                                                                        17]) + ')                     ||                                                                           ||             |                     |   |')
                            print(
                                '|                                               ||                                                                           ||       #---------------------#     |   |')
                            print(
                                '|        one time strength "trap"  (' + str(lp2[14]) + ')' + extandation(str(lp2[14]),
                                                                                                          2) + '         ||                                                                           ||       |                     |     |   |')
                            print(
                                '|                                               ||                                                                           ||  #---------------------#    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '#_______________________________________________##===========================================================================##__|_____________________|____|_____|___#')
                            mbwhobuys = tkinter.messagebox.askquestion('buy/upgrade passive strength "extra rating +1"', "buy/upgrade " + a + '?')
                            if mbwhobuys == 'yes':
                                if a == player1:
                                    if lp1[13] == '0':
                                        if int(lp1[1]) >= 100:
                                            mbactually = tkinter.messagebox.askquestion("confirm a purchase",
                                                                                        "player " + a + ' gets a passive strength "extra rating" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -100
                                                lp1[13] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets an extra rating" 1st level and for win +1 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '1':
                                        if int(lp1[1]) >= 500:
                                            mbactually = tkinter.messagebox.askquestion("confirm an upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -500
                                                lp1[13] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 2nd level and for wins gets +2 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                500 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '2':
                                        if int(lp1[1]) >= 1200:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -1200
                                                lp1[13] = '3'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 3rd level and for wins gets +3 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                1200 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '3':
                                        if int(lp1[1]) >= 3000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -3000
                                                lp1[13] = '4'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 4th level and for wins gets +4 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                3000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '4':
                                        if int(lp1[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 5th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -10000
                                                lp1[13] = '5'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 5th level and for wins gets +5 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp1[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "extra rating" you have got max of 5 levels!')
                                else:
                                    if lp2[13] == '0':
                                        if int(lp2[1]) >= 100:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "extra raring" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -100
                                                lp2[13] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets "extra rating" to 1st level and for wins gets +1 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '1':
                                        if int(lp2[1]) >= 500:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -500
                                                lp2[13] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 2nd level and for wins gets +2 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                500 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '2':
                                        if int(lp2[1]) >= 1200:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -1200
                                                lp2[13] = '3'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 3rd level and for wins gets +3 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                1200 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '3':
                                        if int(lp2[1]) >= 3000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -3000
                                                lp2[13] = '4'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + '  increased "extra rating" to 4th level and for wins gets +4 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                3000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '4':
                                        if int(lp2[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' increase passive strength "extra rating" to 5th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -10000
                                                lp2[13] = '5'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' increased "extra rating" to 5th level and for wins gets +5 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp2[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "extra rating" you have got max of 5 levels!')
                            else:
                                if a == player1:
                                    actuala = a
                                    a = nota
                                    if lp2[13] == '0':
                                        if int(lp2[1]) >= 100:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "extra rating" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -100
                                                lp2[13] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets "extra rating" to 1st level and for win gets +1 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '1':
                                        if int(lp2[1]) >= 500:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' strenghened passive strength "extra rating" to 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -500
                                                lp2[13] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' strenghened "extra rating" to 2nd level and for win gets +2 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                500 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '2':
                                        if int(lp2[1]) >= 1200:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' strenghened passive strength "extra rating" to 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -1200
                                                lp2[13] = '3'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' strenghened "extra rating" to 3rd level and for win gets +3 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                1200 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '3':
                                        if int(lp2[1]) >= 3000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' strenghened passive strength "extra rating" to 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -3000
                                                lp2[13] = '4'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' strenghened "extra rating" to 4th level and for win gets +4 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                3000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[13] == '4':
                                        if int(lp2[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' upgrade passive strength "extra rating" to 5th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -10000
                                                lp2[13] = '5'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "extra rating" to 5th max level and for win gets +5 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp2[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "extra rating" you have max 5th level!')
                                    a = actuala
                                else:
                                    actuala = a
                                    a = nota
                                    if lp1[13] == '0':
                                        if int(lp1[1]) >= 100:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "extra rating" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -100
                                                lp1[13] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' got "extra rating" 1st level and for win gets +1 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '1':
                                        if int(lp1[1]) >= 500:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' upgrade passive strength "extra rating" to 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -500
                                                lp1[13] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "extra rating" to 2nd level and for win gets +2 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                500 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '2':
                                        if int(lp1[1]) >= 1200:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' upgrade passive strength "extra rating" to 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -1200
                                                lp1[13] = '3'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "extra rating" to 3rd level and for win gets +3 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                1200 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '3':
                                        if int(lp1[1]) >= 3000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' upgrade passive strength "extra rating" to 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -3000
                                                lp1[13] = '4'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "extra rating" to 4th level and for win gets +4 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                3000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[13] == '4':
                                        if int(lp1[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm upgrade",
                                                                                        "player " + a + ' upgraded passive strength "extra rating" to 5th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -10000
                                                lp1[13] = '5'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "extra rating" to 5th (max) level and for win gets +5 extra rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp1[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "extra ratingг" you have max 5th level!')
                                    a = actuala
                        elif comand == '2':
                            print(
                                " \n \n \n \n \n#store_____________________________________________________________________________________________________________________________________________________________#")
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print('|    ||                             player ' + player1 + ': ' + str(
                                lp1[1]) + extandation(player1, 20) + extandation(str(lp1[1]), 20) + '  ' + extandation(
                                player2, 20) + extandation(str(lp2[1]), 20) + ' player ' + player2 + ': ' + str(
                                lp2[1]) + '                     ||    |')
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print(
                                '#____##_________________________________________________________________________________________________________________________________________________________##____#')
                            print(
                                '||inventory                                      ||goods======================================================================||info                             |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player1 + ':' + extandation(player1,
                                                                             20) + '                 ||                                                                           ||               "trap"                |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|      passive strength "extra rating"        ||     #---------------------------------------------------------------#     ||   type: one time strength                |')
                            print(
                                '|                                               ||     |      |passive strength "extra rating"                       |     ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        13]) + ')                     ||     |   1  |you get more rating for winnig!                |     ||  if you lova a hardcore, so you need to-  |')
                            print(
                                '|                                               ||     |      |price: 100, 500, 1200, 3000, 10000                       |     ||   think about purchasing 99    |')
                            print(
                                '|           passive strength "gilding"             ||     #---------------------------------------------------------------#     || traps, but would be better |')
                            print(
                                '|                                               ||                                                                           ||         them all in one round         |')
                            print('|               level: (' + str(lp1[
                                                                        16]) + ')                     ||                                                                           ||                                       |')
                            print(
                                '|                                               ||     @@====================================================================@@                                       |')
                            print(
                                '|       passive strength "royal shield"         ||     ||     |one time strength "trap"                                                                               |')
                            print(
                                '|                                               ||     ||  2  |you shuffle a deck of 10th and shuffle it!                     price:                              |')
                            print('|               level: (' + str(lp1[
                                                                        17]) + ')                     ||     ||     |price: 1750                                                              for one: 1750                 |')
                            print(
                                '|                                               ||     @@====================================================================@@                                       |')
                            print(
                                '|        one time strength "trap"  (' + str(lp1[14]) + ')' + extandation(str(lp1[14]),
                                                                                                          2) + '         ||                                                                           ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player2 + ':' + extandation(player2,
                                                                             20) + '                 ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||     |      |passive strength "gilding"                                 |     ||  if you want to waste your money - buy! |')
                            print(
                                '|      passive strength "extra rating"        ||     |   3  |you turn the rating lost by your opponent into gold!  |     ||                                       |')
                            print(
                                '|                                               ||     |      |price: 15000                                             |     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        13]) + ')                     ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|           passive strength "gilding"             ||                                                                           ||  made just to waste your money  |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        16]) + ')                     ||     |      |passive strength "royal shield"                         |     ||                                       |')
                            print(
                                '|                                               ||     |   4  |for some chance and percentage reduces the loss of rating!    |     ||                                       |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |price: 10000, 25000, 50000, 100000                       |     ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||             #---------------------#   |')
                            print('|               level: (' + str(lp2[
                                                                        17]) + ')                     ||                                                                           ||             |                     |   |')
                            print(
                                '|                                               ||                                                                           ||       #---------------------#     |   |')
                            print(
                                '|        one time strength "trap"  (' + str(lp2[14]) + ')' + extandation(str(lp2[14]),
                                                                                                          2) + '         ||                                                                           ||       |                     |     |   |')
                            print(
                                '|                                               ||                                                                           ||  #---------------------#    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '#_______________________________________________##===========================================================================##__|_____________________|____|_____|___#')
                            mbwhobuys = tkinter.messagebox.askquestion('purchasing one time strength "trap"',
                                                                       "purchase " + a + '?')
                            if mbwhobuys == 'yes':
                                if a == player1 and int(lp1[14]) < 100:
                                    if int(lp1[1]) >= 1750:
                                        mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                    "player " + a + ' getting one time strength "trap"! all right?')
                                        if mbactually == 'yes':
                                            lp1[1] = int(lp1[1])
                                            lp1[1] += -1750
                                            lp1[14] = str(int(lp1[14]) + 1)
                                            mbnah = tkinter.messagebox.showinfo('congrats with purchase!',
                                                                                'player ' + a + ' got "trap"!')
                                    else:
                                        mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                            'not enough coins: ' + str(
                                                                                lp1[1]) + '/1750!')
                                elif a == player2 and int(lp2[14]) < 100:
                                    if int(lp2[1]) >= 1750:
                                        mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                    "player " + a + ' getting one time strength "trap"! all right?')
                                        if mbactually == 'yes':
                                            lp2[1] = int(lp2[1])
                                            lp2[1] += -1750
                                            lp2[14] = str(int(lp1[14]) + 1)
                                            mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                'player ' + a + ' got "trap"!')
                                    else:
                                        mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                            'not enough coins: ' + str(
                                                                                lp2[1]) + '/1750!')
                                else:
                                    mbnah = tkinter.messagebox.showinfo('player ' + a, 'you already have enough!')
                            else:
                                if a == player1 and int(lp2[14]) < 100:
                                    actuala = a
                                    a = nota
                                    if int(lp2[1]) >= 1750:
                                        mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                    "player " + a + ' getting one time strength "trap"! all right?')
                                        if mbactually == 'yes':
                                            lp2[1] = int(lp2[1])
                                            lp2[1] += -1750
                                            lp2[14] = str(int(lp1[14]) + 1)
                                            mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                'player ' + a + ' got "trap"!')
                                    else:
                                        mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                            'not enough coins: ' + str(
                                                                                lp2[1]) + '/1750!')
                                    a = actuala
                                elif a == player2 and int(lp1[14]) < 100:
                                    actuala = a
                                    a = nota
                                    if int(lp1[1]) >= 1750:
                                        mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                    "player " + a + ' getting one time strength "trap"! all right?')
                                        if mbactually == 'yes':
                                            lp1[1] = int(lp1[1])
                                            lp1[1] += -1750
                                            lp1[14] = str(int(lp1[14]) + 1)
                                            mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                'player ' + a + ' got "trap"!')
                                    else:
                                        mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                            'not enough coins: ' + str(
                                                                                lp1[1]) + '/1750!')
                                    a = actuala
                                else:
                                    mbnah = tkinter.messagebox.showinfo('player ' + a, 'you already have enough!')
                        elif comand == '3':
                            print(
                                " \n \n \n \n \n#store_____________________________________________________________________________________________________________________________________________________________#")
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print('|    ||                             player ' + player1 + ': ' + str(
                                lp1[1]) + extandation(player1, 20) + extandation(str(lp1[1]), 20) + '  ' + extandation(
                                player2, 20) + extandation(str(lp2[1]), 20) + ' player ' + player2 + ': ' + str(
                                lp2[1]) + '                     ||    |')
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print(
                                '#____##_________________________________________________________________________________________________________________________________________________________##____#')
                            print(
                                '||inventory                                      ||goods======================================================================||info                             |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player1 + ':' + extandation(player1,
                                                                             20) + '                 ||                                                                           ||               "gilding"              |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|      passive strength "extra rating"        ||     #---------------------------------------------------------------#     ||   type: passive strength (always work out)   |')
                            print(
                                '|                                               ||     |      |passive strength "extra rating"                       |     ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        13]) + ')                     ||     |   1  |you get extra rating for win!                |     ||  have 1 level, made for  |')
                            print(
                                '|                                               ||     |      |price: 100, 500, 1200, 3000, 10000                       |     || lost opponent rating  |')
                            print(
                                '|           passive strength "gilding"             ||     #---------------------------------------------------------------#     ||               in gold                |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        16]) + ')                     ||                                                                           ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||    price:                              |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |one time strength "trap"                                |     ||       1st level: 15000               |')
                            print(
                                '|                                               ||     |   2  |you shuffle a deck of 10th and shuffle it!         |     ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        17]) + ')                     ||     |      |price: 1750                                              |     ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|        one time strength "trap"  (' + str(lp1[14]) + ')' + extandation(str(lp1[14]),
                                                                                                          2) + '         ||                                                                           ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player2 + ':' + extandation(player2,
                                                                             20) + '                 ||     @@====================================================================@@                                       |')
                            print(
                                '|                                               ||     ||     |passive strength "gilding"                                              works only if you won     |')
                            print(
                                '|      passive strength "extra rating"        ||     ||  3  |you turn the rating lost by your opponent into gold!                                                 |')
                            print(
                                '|                                               ||     ||     |price: 15000                                                                                            |')
                            print('|               level: (' + str(lp2[
                                                                        13]) + ')                     ||     @@====================================================================@@                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|           passive strength "gilding"             ||                                                                           ||     Buy it! Always needed!    |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        16]) + ')                     ||     |      |passive strength "royal shield"                         |     ||                                       |')
                            print(
                                '|                                               ||     |   4  for some chance and percentage reduces the loss of rating!    |     ||                                       |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |price: 10000, 25000, 50000, 100000                       |     ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||             #---------------------#   |')
                            print('|               level: (' + str(lp2[
                                                                        17]) + ')                     ||                                                                           ||             |                     |   |')
                            print(
                                '|                                               ||                                                                           ||       #---------------------#     |   |')
                            print(
                                '|        one time strength "trap"  (' + str(lp2[14]) + ')' + extandation(str(lp2[14]),
                                                                                                          2) + '         ||                                                                           ||       |                     |     |   |')
                            print(
                                '|                                               ||                                                                           ||  #---------------------#    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '#_______________________________________________##===========================================================================##__|_____________________|____|_____|___#')
                            mbwhobuys = tkinter.messagebox.askquestion('purchasing passive strength "gilding"',
                                                                       "purchase " + a + '?')
                            if mbwhobuys == 'yes':
                                if a == player1:
                                    if lp1[16] == '0':
                                        if int(lp1[1]) >= 15000:
                                            mbactually = tkinter.messagebox.askquestion("confirmation of purchase",
                                                                                        "player " + a + ' gets passive strength "gilding"! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -15000
                                                lp1[16] = '1'
                                                mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                    'player ' + a + ' got "gilding" and for win gets gold fot lost rating by your opponent!')
                                        else:
                                            mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                                'not enough coins: ' + str(
                                                                                    lp1[1]) + '/15000!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a, 'you already have "gilding"!')
                                else:
                                    if lp2[16] == '0':
                                        if int(lp2[1]) >= 15000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "gilding"! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -15000
                                                lp2[16] = '1'
                                                mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                    'player ' + a + ' got "gilding" and for win gets gold fot lost rating by your opponent!')
                                        else:
                                            mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                                'not enough coins: ' + str(
                                                                                    lp2[1]) + '/15000!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a, 'ypu already have "gilding"!')
                            else:
                                if a == player1:
                                    actuala = a
                                    a = nota
                                    if lp2[16] == '0':
                                        if int(lp2[1]) >= 15000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "gilding"! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -15000
                                                lp2[16] = '1'
                                                mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                    'player ' + a + ' got "gilding" and for win gets gold fot lost rating by your opponent!')
                                        else:
                                            mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                                'not enough coins: ' + str(
                                                                                    lp2[1]) + '/15000!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a, 'you already have "gilding"!')
                                    a = actuala
                                else:
                                    actuala = a
                                    a = nota
                                    if lp1[16] == '0':
                                        if int(lp1[1]) >= 15000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "gilding"! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -15000
                                                lp1[16] = '1'
                                                mbnah = tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                                    'player ' + a + ' got "gilding" and for win gets gold fot lost rating by your opponent!')
                                        else:
                                            mbnah = tkinter.messagebox.showinfo('player ' + a,
                                                                                'not enough coins: ' + str(
                                                                                    lp1[1]) + '/15000!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a, 'you already have "gilding"!')
                                    a = actuala
                        elif comand == '4':
                            print(
                                " \n \n \n \n \n#store_____________________________________________________________________________________________________________________________________________________________#")
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print('|    ||                             player ' + player1 + ': ' + str(
                                lp1[1]) + extandation(player1, 20) + extandation(str(lp1[1]), 20) + '  ' + extandation(
                                player2, 20) + extandation(str(lp2[1]), 20) + ' player ' + player2 + ': ' + str(
                                lp2[1]) + '                     ||    |')
                            print(
                                '|    ||                                                                                                                                                         ||    |')
                            print(
                                '#____##_________________________________________________________________________________________________________________________________________________________##____#')
                            print(
                                '||inventory                                      ||goods======================================================================||info                             |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player1 + ':' + extandation(player1,
                                                                             20) + '                 ||                                                                           ||           "royal shield"          |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|      passive strength "extra rating"        ||     #---------------------------------------------------------------#     ||   type: passive strength (always work out)   |')
                            print(
                                '|                                               ||     |      |passive strength "extra rating"                       |     ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        13]) + ')                     ||     |   1  |you get more for the win!                |     ||   have 4 levels, level of this strength       |')
                            print(
                                '|                                               ||     |      |price: 100, 500, 1200, 3000, 10000                       |     || increase chance and amound of saved |')
                            print(
                                '|           passive strength "gilding"             ||     #---------------------------------------------------------------#     ||               rating                |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('|               level: (' + str(lp1[
                                                                        16]) + ')                     ||                                                                           ||                                       |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||    price:                              |')
                            print(
                                '|       passive strength "royal shield"         ||     |      |one time strength "trap"                                |     ||       1st level: 10000               |')
                            print(
                                '|                                               ||     |   2  |you shuffle a deck of 10th and shuffle it!         |     ||       2nd level: 25000               |')
                            print('|               level: (' + str(lp1[
                                                                        17]) + ')                     ||     |      |price: 1750                                              |     ||       3rd level: 50000               |')
                            print(
                                '|                                               ||     #---------------------------------------------------------------#     ||       4th level: 100000              |')
                            print(
                                '|        one time strength "trap"  (' + str(lp1[14]) + ')' + extandation(str(lp1[14]),
                                                                                                          2) + '         ||                                                                           ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print('| player ' + player2 + ':' + extandation(player2,
                                                                             20) + '                 ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||     |      |passive strength "gilding"                                 |     ||     works only if you loss      |')
                            print(
                                '|      passive strength "extra rating"        ||     |   3  |you turn the rating lost by your opponent into gold!  |     ||                                       |')
                            print(
                                '|                                               ||     |      |price: 15000                                             |     ||                                       |')
                            print('|               level: (' + str(lp2[
                                                                        13]) + ')                     ||     #---------------------------------------------------------------#     ||                                       |')
                            print(
                                '|                                               ||                                                                           ||                                       |')
                            print(
                                '|           passive strength "gilding"             ||                                                                           ||     buy it! always needed!     |')
                            print(
                                '|                                               ||     @@====================================================================@@                                       |')
                            print('|               level: (' + str(lp2[
                                                                        16]) + ')                     ||     ||     |passive strength "royal shield"                                                                        |')
                            print(
                                '|                                               ||     ||  4  |for some chance and percentage reduces the loss of rating!                                                   |')
                            print(
                                '|       passive strength "royal shield"         ||     ||     |price: 10000, 25000, 50000, 100000                                                                      |')
                            print(
                                '|                                               ||     @@====================================================================@@             #---------------------#   |')
                            print('|               level: (' + str(lp2[
                                                                        17]) + ')                     ||                                                                           ||             |                     |   |')
                            print(
                                '|                                               ||                                                                           ||       #---------------------#     |   |')
                            print(
                                '|        one time strength "trap"  (' + str(lp2[14]) + ')' + extandation(str(lp2[14]),
                                                                                                          2) + '         ||                                                                           ||       |                     |     |   |')
                            print(
                                '|                                               ||                                                                           ||  #---------------------#    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '|                                               ||                                                                           ||  |                     |    |     |   |')
                            print(
                                '#_______________________________________________##===========================================================================##__|_____________________|____|_____|___#')
                            mbwhobuys = tkinter.messagebox.askquestion(
                                'buy/upgrade passive strength "royal shield"', "buy/upgrade " + a + '?')

                            if mbwhobuys == 'yes':
                                if a == player1:
                                    if lp1[17] == '0':
                                        if int(lp1[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -10000
                                                lp1[17] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets "royal shield" 1st level and for defeat loses with a 25% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '1':
                                        if int(lp1[1]) >= 25000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -25000
                                                lp1[17] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "royal shield" to 2nd level and for defeat loses with a 33% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                25000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '2':
                                        if int(lp1[1]) >= 50000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -50000
                                                lp1[17] = '3'
                                                tkinter.messagebox.showinfo('congrats with strengthening!',
                                                                            'player ' + a + ' strenghtened "royal shield" to 3rd level and for defeat loses with a 33% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                50000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '3':
                                        if int(lp1[1]) >= 100000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -100000
                                                lp1[17] = '4'
                                                tkinter.messagebox.showinfo('congrats with conversion!',
                                                                            'player ' + a + ' conversed "royal shield" to 4th level and for defeat loses with a *50*% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100000 - int(lp1[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "royal shield" you have max 4th level!')
                                else:
                                    if lp2[17] == '0':
                                        if int(lp2[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -10000
                                                lp2[17] = '1'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' gets "royal shield" 1st level and for defeat loses with a 25% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '1':
                                        if int(lp2[1]) >= 25000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -25000
                                                lp2[17] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "royal shield" to *2nd level and for defeat loses with a 33% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                25000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '2':
                                        if int(lp2[1]) >= 50000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -50000
                                                lp2[17] = '3'
                                                tkinter.messagebox.showinfo('congrats with strengthening!',
                                                                            'player ' + a + ' strenghtened "royal shield" to 3rd level and for defeat loses with a 33% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                50000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '3':
                                        if int(lp2[1]) >= 100000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -100000
                                                lp2[17] = '4'
                                                tkinter.messagebox.showinfo('congrats with conversion!',
                                                                            'player ' + a + ' conversed "royal shield" to 4th level and for defeat loses with a 50% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100000 - int(lp2[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "royal shield" to max 4th level!')
                            else:
                                if a == player1:
                                    actuala = a
                                    a = nota
                                    if lp2[17] == '0':
                                        if int(lp2[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -10000
                                                lp2[17] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets "royal shield" 1st level and for defeat loses with a 25% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '1':
                                        if int(lp2[1]) >= 25000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -25000
                                                lp2[17] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "royal shield" to 2nd level and for defeat loses with a 33% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                25000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '2':
                                        if int(lp2[1]) >= 50000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -50000
                                                lp2[17] = '3'
                                                tkinter.messagebox.showinfo('congrats with strengthening!',
                                                                            'player ' + a + ' strenghtened "royal shield" to 3rd level and for defeat loses with a 33% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                50000 - int(lp2[1])) + ' not enough gold!')
                                    elif lp2[17] == '3':
                                        if int(lp2[1]) >= 100000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp2[1] = int(lp2[1])
                                                lp2[1] += -100000
                                                lp2[17] = '4'
                                                tkinter.messagebox.showinfo('congrats with conversion!',
                                                                            'player ' + a + ' conversed "royal shield" to 4th level and for defeat loses with a 50% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100000 - int(lp2[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "royal shield" to max 4th level!')
                                    a = actuala
                                else:
                                    actuala = a
                                    a = nota
                                    if lp1[17] == '0':
                                        if int(lp1[1]) >= 10000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 1st level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -10000
                                                lp1[17] = '1'
                                                tkinter.messagebox.showinfo('congrats with purchase!',
                                                                            'player ' + a + ' gets "royal shield" 1st level and for defeat loses with a 25% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                10000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '1':
                                        if int(lp1[1]) >= 25000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 2nd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -25000
                                                lp1[17] = '2'
                                                tkinter.messagebox.showinfo('congrats with upgrade!',
                                                                            'player ' + a + ' upgraded "royal shield" to 2nd level and for defeat loses with a 33% chance of 25% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                25000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '2':
                                        if int(lp1[1]) >= 50000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 3rd level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -50000
                                                lp1[17] = '3'
                                                tkinter.messagebox.showinfo('congrats with strengthening!',
                                                                            'player ' + a + ' strenghtened "royal shield" to 3rd level and for defeat loses with a 33% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                50000 - int(lp1[1])) + ' not enough gold!')
                                    elif lp1[17] == '3':
                                        if int(lp1[1]) >= 100000:
                                            mbactually = tkinter.messagebox.askquestion("confirm of purchase",
                                                                                        "player " + a + ' gets passive strength "royal shield" 4th level! all right?')
                                            if mbactually == 'yes':
                                                lp1[1] = int(lp1[1])
                                                lp1[1] += -100000
                                                lp1[17] = '4'
                                                tkinter.messagebox.showinfo('congrats with conversion!',
                                                                            'player ' + a + ' conversioned "royal shield" to 4th level and for defeat loses with a *50*% chance of 50% less rating!')
                                        else:
                                            tkinter.messagebox.showinfo('player ' + a, 'not enough coins! ' + str(
                                                100000 - int(lp1[1])) + ' not enough gold!')
                                    else:
                                        tkinter.messagebox.showinfo('player ' + a,
                                                                    'passive strength "royal shield" you have max 4th level!')
                                    a = actuala
            if winornot == 'г1':
                if lp1[13] != 'empty':
                    temporaryvalue = int(lp1[13])
                else:
                    temporaryvalue = 0
                yea = hasdevineshield(lp2[17], rating(lp2[0]), 2)
                if lp1[16] != 'empty':
                    lp1[1] = int(lp1[1])
                    lp1[1] += -rating(lp2[0])[2] - yea
                lp1n = lp1[0] + rating(lp1[0])[0] + winstreak1 // 5 + temporaryvalue
                lp2n = lp2[0] + rating(lp2[0])[2] + yea
                lp1n = str(lp1n)
                lp2n = str(lp2n)
                fi1 = open(pl1, 'w')
                fi2 = open(pl2, 'w')
                print(
                    step + '_______________________________________________________________________________________________________________________________________________________________________')
                print(player1, 'won', ' \n \n')
                print(bigspace, player1 + ': ' + str(lp1[0]) + '(' + str(
                    rating(lp1[0])[0] + winstreak1 // 5 + temporaryvalue) + ')', '>>>', lp1n, 'rank:',
                      rating(int(lp1n))[4])
                if lp1[13] != 'empty':
                    print(bigspace, '>>> "extra rating" worked out' + str(temporaryvalue) + ' level (' + str(
                        rating(lp1[0])[0] + winstreak1 // 5) + '+' + str(temporaryvalue) + ')')
                print(' ')
                print(bigspace, player2 + ': ' + str(lp2[0]) + '(' + str(rating(lp2[0])[2] + yea) + ') >>>', lp2n,
                      'rank:', rating(int(lp2n))[4])
                if yea != 0:
                    print(bigspace, '>>> "royal shield" worked out and saved you', int(yea), 'rating')
                print(' ')
                print(
                    '_______________________________________________________________________________________________________________________________________________________________________\n \n \n')
                winstreak1 += 1
                if rating(lp1[0])[4] != rating(int(lp1n))[4]:
                    print('for', player1 + ':', 'congrats, you are upgrated to', rating(int(lp1n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp1n))[0]) + '(' + str(rating(int(lp1n))[1]) + '), for loss:',
                          str(rating(int(lp1n))[2]) + '(' + str(rating(int(lp1n))[3]) + ')')
                    if lp1[rating(int(lp1n))[7]] == '0':
                        lp1[rating(int(lp1n))[7]] = '1'
                        lp1[1] = int(lp1[1])
                        lp1[1] += rating(int(lp1n))[6]
                        print('current balance:', lp1[1])
                if winstreak1 % 5 == 0 and winstreak1 != 0:
                    print('for', player1 + ':', 'you won', winstreak1,
                          "times in a row and it's impressive, so you'll get an extra rating in size '" + str(
                              winstreak1 // 5) + "'")
                if rating(lp2[0])[4] != rating(int(lp2n))[4]:
                    print('for', player2 + ':', 'unfortunately, you are demoted to', rating(int(lp2n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp2n))[0]) + '(' + str(rating(int(lp2n))[1]) + '), for loss:',
                          str(rating(int(lp2n))[2]) + '(' + str(rating(int(lp2n))[3]) + ')')
                if winstreak2 > 3:
                    print('for', player2 + ':', 'unfortunately, you lost series of', winstreak2, "won")
                winstreak2 = 0
                print(step)
                fi1.write(newbar(lp1, lp1n))
                fi2.write(newbar(lp2, lp2n))
                fi1.close()
                fi2.close()
            elif winornot == 'г2':
                if lp2[13] != 'empty':
                    temporaryvalue = int(lp2[13])
                else:
                    temporaryvalue = 0
                yea = hasdevineshield(lp1[17], rating(lp1[0]), 2)
                if lp2[16] != 'empty':
                    lp2[1] = int(lp2[1])
                    lp2[1] += -rating(lp1[0])[2] - yea
                lp1n = lp1[0] + rating(lp1[0])[2] + yea
                lp2n = lp2[0] + rating(lp2[0])[0] + winstreak2 // 5 + temporaryvalue
                lp1n = str(lp1n)
                lp2n = str(lp2n)
                fi1 = open(pl1, 'w')
                fi2 = open(pl2, 'w')
                print(
                    step + '_______________________________________________________________________________________________________________________________________________________________________')
                print(player2, 'won', ' \n \n')
                print(bigspace, player2 + ':',
                      str(lp2[0]) + '(' + str(rating(lp2[0])[0] + winstreak2 // 5 + temporaryvalue) + ')', '>>>', lp2n,
                      'rank:', rating(int(lp2n))[4])
                if lp2[13] != 'empty':
                    print(bigspace, '>>> extra rating" worked out ' + str(temporaryvalue) + 'level (' + str(
                        rating(lp2[0])[0] + winstreak2 // 5) + '+' + str(temporaryvalue) + ')')
                print(' ')
                print(bigspace, player1 + ':', str(lp1[0]) + '(' + str(rating(lp1[0])[2] + yea) + ')', '>>>', lp1n,
                      'rank:', rating(int(lp1n))[4])
                if yea != 0:
                    print(bigspace, '>>> "royal shield" worked out and saved you', int(yea), 'rating')
                print(' ')
                print(
                    '_______________________________________________________________________________________________________________________________________________________________________\n \n \n')
                winstreak2 += 1
                if rating(lp2[0])[4] != rating(int(lp2n))[4]:
                    print('for', player2 + ':', 'congrats, you are upgrated to', rating(int(lp2n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp2n))[0]) + '(' + str(rating(int(lp2n))[1]) + '), for loss:',
                          str(rating(int(lp2n))[2]) + '(' + str(rating(int(lp2n))[3]) + ')')
                    if lp2[rating(int(lp2n))[7]] == '0':
                        lp2[rating(int(lp2n))[7]] = '1'
                        lp2[1] = int(lp2[1])
                        lp2[1] += rating(int(lp2n))[6]
                        print('current balance:', lp2[1])
                if winstreak2 % 5 == 0 and winstreak2 != 0:
                    print('for', player2 + ':', 'you won', winstreak2,
                          "times in a row and it's impressive, so you'll get an extra rating in size '" + str(
                              winstreak2 // 5) + "'")
                if rating(lp1[0])[4] != rating(int(lp1n))[4]:
                    print('for', player1 + ':', 'unfortunately, you are demoted to', rating(int(lp1n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp1n))[0]) + '(' + str(rating(int(lp1n))[1]) + '), for loss:',
                          str(rating(int(lp1n))[2]) + '(' + str(rating(int(lp1n))[3]) + ')')
                if winstreak1 > 3:
                    print('for', player1 + ':', 'unfortunately, you lost series of', winstreak1, "wins")
                winstreak1 = 0
                print(step)
                fi1.write(newbar(lp1, lp1n))
                fi2.write(newbar(lp2, lp2n))
                fi1.close()
                fi2.close()
            elif winornot == 'г121':
                if lp1[13] != 'empty':
                    temporaryvalue = int(lp1[13])
                else:
                    temporaryvalue = 0
                yea = hasdevineshield(lp2[17], rating(lp2[0]), 3)
                if lp1[16] != 'empty':
                    lp1[1] = int(lp1[1])
                    lp1[1] += -rating(lp2[0])[3] - yea
                lp1n = lp1[0] + rating(lp1[0])[1] + winstreak1 // 5 + temporaryvalue
                lp2n = lp2[0] + rating(lp2[0])[3] + yea
                lp1n = str(lp1n)
                lp2n = str(lp2n)
                fi1 = open(pl1, 'w')
                fi2 = open(pl2, 'w')
                print(
                    step + '_______________________________________________________________________________________________________________________________________________________________________')
                print('took 21', player1, ' \n \n')
                print(bigspace, player1 + ':',
                      str(lp1[0]) + '(' + str(rating(lp1[0])[1] + winstreak1 // 5 + temporaryvalue) + ')', '>>>', lp1n,
                      'rank:', rating(int(lp1n))[4])
                if lp1[13] != 'empty':
                    print(bigspace, '>>> extra rating" worked out ' + str(temporaryvalue) + 'level (' + str(
                        rating(lp1[0])[1] + winstreak1 // 5) + '+' + str(temporaryvalue) + ')')
                print(' ')
                print(bigspace, player2 + ':', str(lp2[0]) + '(' + str(rating(lp2[0])[3] + yea) + ')', '>>>', lp2n,
                      'rank:', rating(int(lp2n))[4])
                if yea != 0:
                    print(bigspace, '>>> "royal shield" worked out and saved you', int(yea), 'rating')
                print(' ')
                print(
                    '_______________________________________________________________________________________________________________________________________________________________________\n \n \n')
                winstreak1 += 1
                if rating(lp1[0])[4] != rating(int(lp1n))[4]:
                    print('for', player1 + ':', 'congrats, you are upgrated to', rating(int(lp1n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp1n))[0]) + '(' + str(rating(int(lp1n))[1]) + '), for loss:',
                          str(rating(int(lp1n))[2]) + '(' + str(rating(int(lp1n))[3]) + ')')
                    if lp1[rating(int(lp1n))[7]] == '0':
                        lp1[rating(int(lp1n))[7]] = '1'
                        lp1[1] = int(lp1[1])
                        lp1[1] += rating(int(lp1n))[6]
                        print('current balance:', lp1[1])
                if winstreak1 % 5 == 0 and winstreak1 != 0:
                    print('for', player1 + ':', 'you won', winstreak1,
                          "times in a row and it's impressive, so you'll get an extra rating in size '" + str(
                              winstreak1 // 5) + "'")
                if rating(lp2[0])[4] != rating(int(lp2n))[4]:
                    print('for', player2 + ':', 'unfortunately, you are demoted to', rating(int(lp2n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp2n))[0]) + '(' + str(rating(int(lp2n))[1]) + '), for loss:',
                          str(rating(int(lp2n))[2]) + '(' + str(rating(int(lp2n))[3]) + ')')
                if winstreak2 > 3:
                    print('for', player2 + ':', 'unfortunately, you lost series of', winstreak2, "wins")
                winstreak2 = 0
                print(step)
                fi1.write(newbar(lp1, lp1n))
                fi2.write(newbar(lp2, lp2n))
                fi1.close()
                fi2.close()
            elif winornot == 'г221':
                if lp2[13] != 'empty':
                    temporaryvalue = int(lp2[13])
                else:
                    temporaryvalue = 0
                yea = hasdevineshield(lp1[17], rating(lp1[0]), 3)
                if lp2[16] != 'empty':
                    lp2[1] = int(lp2[1])
                    lp2[1] += -rating(lp1[0])[3] - yea
                lp1n = lp1[0] + rating(lp1[0])[3] + yea
                lp2n = lp2[0] + rating(lp2[0])[1] + winstreak2 // 5 + temporaryvalue
                lp1n = str(lp1n)
                lp2n = str(lp2n)
                fi1 = open(pl1, 'w')
                fi2 = open(pl2, 'w')
                print(
                    step + '_______________________________________________________________________________________________________________________________________________________________________')
                print('took 21', player2, ' \n \n')
                print(bigspace, player2 + ':',
                      str(lp2[0]) + '(' + str(rating(lp2[0])[1] + winstreak2 // 5 + temporaryvalue) + ')', '>>>', lp2n,
                      'rank:', rating(int(lp2n))[4])
                if lp2[13] != 'empty':
                    print(bigspace, '>>> extra rating" worked out ' + str(temporaryvalue) + 'level (' + str(
                        rating(lp2[0])[1] + winstreak2 // 5) + '+' + str(temporaryvalue) + ')')
                print(' ')
                print(bigspace, player1 + ':', str(lp1[0]) + '(' + str(rating(lp1[0])[3] + yea) + ')', '>>>', lp1n,
                      'rank:', rating(int(lp1n))[4])
                if yea != 0:
                    print(bigspace, '>>> "royal shield" worked out and saved you', int(yea), 'rating')
                print(' ')
                print(
                    '_______________________________________________________________________________________________________________________________________________________________________\n \n \n')
                winstreak2 += 1
                if rating(lp2[0])[4] != rating(int(lp2n))[4]:
                    print('for', player2 + ':', 'congrats, you are upgrated to', rating(int(lp2n))[5] + '.',
                          "for win you get:",
                          str(rating(int(lp2n))[0]) + '(' + str(rating(int(lp2n))[1]) + '), for loss:',
                          str(rating(int(lp2n))[2]) + '(' + str(rating(int(lp2n))[3]) + ')')
                    if lp2[rating(int(lp2n))[7]] == '0':
                        lp2[rating(int(lp2n))[7]] = '1'
                        lp2[1] = int(lp2[1])
                        lp2[1] += rating(int(lp2n))[6]
                        print('current balance:', lp2[1])
                if winstreak2 % 5 == 0 and winstreak2 != 0:
                    print('for', player2 + ':', 'you won', winstreak2,
                          "times in a row and it's impressive, so you'll get an extra rating in size '" + str(
                              winstreak2 // 5) + "'")
                if rating(lp1[0])[4] != rating(int(lp1n))[4]:
                    print('for', player1 + ':', 'unfortunately, you are demoted to', rating(int(lp1n))[5] + '.',
                          "for your win you get:",
                          str(rating(int(lp1n))[0]) + '(' + str(rating(int(lp1n))[1]) + '), for loss:',
                          str(rating(int(lp1n))[2]) + '(' + str(rating(int(lp1n))[3]) + ')')
                if winstreak1 > 3:
                    print('for', player1 + ':', 'unfortunately, you lost series of', winstreak1, "wins")
                winstreak1 = 0
                print(step)
                fi1.write(newbar(lp1, lp1n))
                fi2.write(newbar(lp2, lp2n))
                fi1.close()
                fi2.close()
            else:
                fi1 = open(pl1, 'w')
                fi2 = open(pl2, 'w')
                fi1.write(newbar(lp1, lp1[0]))
                fi2.write(newbar(lp2, lp2[0]))
                fi1.close()
                fi2.close()
                print(
                    step + '_______________________________________________________________________________________________________________________________________________________________________')
                print('your current rating:\n \n ')
                print(bigspace, player1 + ':', lp1[0], 'rank:', rating(lp1[0])[4], ' \n ')
                print(bigspace, player2 + ':', lp2[0], 'rank:', rating(lp2[0])[4], ' \n ')
                print(
                    '_______________________________________________________________________________________________________________________________________________________________________\n \n \n')
                print(step)
                if winornot != 'u':
                    gamerow -= 1
            gamerow += 1
            print(step, step, step)
