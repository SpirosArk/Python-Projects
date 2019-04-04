#Code written by Spiros Ark

from random import randint
import os 


def foo(x):
    if x is 'r' or x is 'R':
        return False
    else:
        try:
            i=int(x)
            if i>3 and i<20:
                return False
        except Exception:
            return True
    return True


def printhanger(tries,maxtries):                                                                                             #Function so the programm will be able to appear the hanger.
  
    if tries == 5:
        print('+-----+')
        print('|')
        print('|')
        print('|') 
        print(tries,'tries left')
    elif tries == 4:
        print('+-----+')
        print('|',''*10,'o')
        print('|')
        print('|') 
        print(tries,'tries left')   
    elif tries == 3:
        print('+-----+')
        print('|',''*10,'o')
        print('|',''*3,'--+')
        print('|') 
        print(tries,'tries left')
    elif tries == 2:
        print('+-----+')
        print('|',''*10,'o')
        print('|',''*3,'--+--')
        print('|') 
        print(tries,'tries left')
    elif tries == 1:
        print('+-----+')
        print('|',''*10,'o')
        print('|',''*3,'--+--')
        print('|',''*5,'/') 
        print(tries,'tries left')
    elif tries == 0:
        print('+-----+')
        print('|',''*10,'o')
        print('|',''*3,'--+--')
        print('|',''*5,'/\\')


s=0                                                                                                                          #Variable to win the game(must reach len(theWord))
playagain=True
while playagain is True: 
        tries=5
        maxtries=5
        f=[open('words.txt','r')]
        Choice=input('Type g or G if word will be given by another player: ') 
        cL=[]
        wRl=[]
        

        if Choice is 'G' or Choice is 'g':                                                                                   #Selecion between game type(versus cpu/2nd player).
            theWord=input('Player do not look! 2nd player, type in word, must be in English and at least 3 letters long: ')  #(Game vs 2nd player).
            theWord=theWord.lower()
            while theWord not in f:
                theWord=input('Please enter a valid english word between 3 and 20 letters:')	       
            os.system('clear')           
        else:
            wl=input('Type r or R for word of random length,else give length of random word(between 3 and 20):')             #(Game vs cpu)Code for random word selection.

            while foo(wl):
                wl=input('Type r or R for word of random length,else give length of random word(between 3 and 20):')

            if wl is 'r' or wl is 'R':                                                                                       #Code for random word selection
                listIntex=randint(0,66617)
                theWord=y[listIntex]
            else: 
                theWord=y[int(wl)]
                theWord=list(theWord)
        w=['_' * len(theWord)]
        while (tries != 0) or (s != len(theWord)):
            print(w)
            printhanger(tries,maxtries)                                                                                      #Game winning and losing conditions
            print('Chosen letters are:',cL)
            print('Wrong letters are:',wRl)
            letter=input('Give me a letter:')
            letter=letter.upper()
            while letter in cL:                                                                                              #What happens if the letter has already been selected
                letter=input('You already gave that letter')
                letter=letter.upper()
            cL.append(letter)
            s = s + theWord.count(letter)
            if letter in theWord:                                                                               
            	for i in range(len(theWord)):
            		if letter==theWord[i]:
               			w[i]=letter

            else:                                                                                               #Section where the tries are going down by 1 if a wrondg lette has been chosen
            	tries=tries-1
            	printhanger(tries,maxtries)
            print(''.join(w))
        if tries is 0: 
            print('Sorry! You lost! The word was',theWord)
        if s is len(theWord):
            print('Congrats you found the word')
        playagain=input('If you want to play again press True')
