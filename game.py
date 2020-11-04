# This game a simple game you can play it easally that name is rock , paper , sissions
# this whrote by python 3.9

import os
os.system('cls'or'clear')
class color:
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHTIE = '\033[0m'
    YELLOW = '\033[93m'
    sed = '\033[96m'
print(color.RED+r'                                                /M/M\M\                          ')
print(color.RED+r'                                               /M/|M|\M\  ')
print(color.RED+r'       /G/G/G/G/G/G/G                         /M/ |M| \M\                              ')
print(color.RED+r'      /G/                                    /M/|M|M|M|\M\                           ')
print(color.RED+r'     /G/                                    /M/  |M| |M \M\                           ')                         
print(color.RED+r'    /G/                                    /M/   |M| |M  \M\                         ')
print(color.sed+r'   /G/                                     |M|   |M| |M  |M|      /E/E/E/|E|                      ')
print(color.sed+r'  |G|   \G\G\G\G\G/|G|   |A|\A\A\A\        |M/M/M|M|M|M|M|M|     /E      |E|                                     ')
print(color.sed+r'   \G\             |G|   \A\      |A|      |M|   |M| |M  |M|    /E/      |E|                       ')
print(color.sed+r'    \G\            |G|   \A\      |A|      |M|   |M| |M  |M|   /E/E/E\\E\|E|                      ')
print(color.sed+r'     \G\           |G|   \A\      |A|      |M|   |M| |M  |M|   \E\                             ')
print(color.sed+r'      \G\/G/G/G/G/G|G|    \A\A\A\A\A\A\    |M|           |M|    \E\E\E\E\E\E                          ')
print(color.GREEN+'----------------------------------------------------')                                                                              
print(color.sed+'sissiors , rock or paper')
print(color.GREEN+'----------------------------------------------------')



player1 = str(input('player1 enter your move : '))
player2 = str(input('player2 enter your move :'))

if player1 == 'rock':
    if player2 == 'sissiors':
        print('player 1 wins')
    elif player2 == 'paper':
        print('player 2 wins')

if player1 == 'paper':
    if player2 == 'rock':
        print('player 1 wins')
    elif player2 == 'sissiors':
        print('player 2 wins')
if player1 == 'sissors':
    if player2 == 'paper':
        print('player 1 wins')
    elif player2 == 'rock':
        print('player 2 wins')
    else :
        print('Cannot find sorry :( ):')



print(color.GREEN+'----------------------------------------------------')
print(color.sed+'THANKS CHOISE THIS APP .')
print(color.GREEN+'----------------------------------------------------')
