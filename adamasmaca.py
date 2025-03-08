import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words=('karınca babun porsuk yarasa ayı kunduz deve kedi istiridye kobra puma çakal '
       'karga geyik köpek eşek ördek kartal gelincik tilki kurbağa keçi kaz şahin'
       'aslan kertenkele lama köstebek maymun kuş geyik fare katır baykuş panda').split()

def getrandomword(wordlist):
    i=random.randint(0,len(wordlist)-1)
    return wordlist[i]

def displayBoard(missedL,correctL,secretWord):
    print(HANGMANPICS[len(missedL)])
    print()

    print('Yanlış harfler:', end=' ')
    for letter in missedL:
        print(letter, end=' ')
    print()

    print('Doğru harfler:', end=' ')
    for letter in correctL:
        print(letter, end=' ')
    print()



    blanks='_'*len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctL:
            blanks= blanks[:i]+secretWord[i]+blanks[i+1:]


    for letter in blanks:

         print(letter, end=' ')

    print()

def getGuess(alreadyguess):
      while True:
          print('Bir harf söyle.')
          guess = input()
          guess = guess.lower()

          if len(guess) !=1:
              print('Lütfen sadece 1 harf söyle.')

          elif guess in alreadyguess:
              print('Bu harfi zaten söyledin.')

          elif guess not in 'abcçdefgğhıijklmnoöprsştuüvyz':
              print('Lütfen Türkçe alfabeden bir harf söyle.')

          else:
              return guess

def playAgain():

    print("Yeniden oynamak istiyor musun?")
    return input().lower().startswith('e')


print('A D A M  A S M A C A')
missedL= ''
correctL= ''
secretWord=getrandomword(words)
gameisdone= False


while True:
    displayBoard(missedL,correctL,secretWord)
    guess= getGuess(missedL + correctL)
    if guess in secretWord:
        correctL=correctL + guess

        allfound=True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctL:
                allfound = False


        if allfound:
            print('Tebrikler! Gizli kelime:' +secretWord)
            print('Kazandınız!')
            gameisdone = True

    else:
        missedL=missedL + guess

    if len(missedL)==len(HANGMANPICS)-1:
        displayBoard(missedL, correctL, secretWord)
        print('Tahmin hakkın bitti. ' +
              str(len(missedL)) + ' yanlış tahmin ' +
              str(len(correctL)) + ' doğru tahmin yaptın. '+ 'Gizli kelime:' + secretWord)
        gameisdone = True






    if gameisdone:
        if playAgain():
            missedL = ''
            correctL = ''
            gameisdone = False
            secretWord = getrandomword(words)
        else:                                  
            break                              
