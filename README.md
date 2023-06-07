                **HELLO MY NAME IS ALLAYAR NIETBAEV**
<h1 align="center">there are no hints in this game</h1>

    from random import choice

    HANGMAN = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''','''

    +---+
    |   |
    O   |
        |
        |
        |
    =========''','''

        +---+
        |   |
        O   |
        |   |
            |
            |
     =========''','''

        +---+
        |   |
        O   |
       /|   |
            |
            |
     =========''','''

        +---+
        |   |
        O   |
       /|\  |
            |
            |
     =========''','''

        +---+
        |   |
        O   |
       /|\  |
        /   |
            |
     =========''','''

        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
     =========''']
    max_wrong = len(HANGMAN)

    words = ('programming','python','bread',    'youtube''human','door','house','minecraft','fire', 'car')
    

    word = choice(words)
    so_far = ' * ' * len(word)
    wrong = 0
    used = []

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])
        print('You used the following letters:'used)
        print('At the moment the word looks like this:',so_far)
    
    guess = input('Enter your letter:')
    
    while guess in  used:
        print('you already guessed the letter',guess)
        guess = input('Enter your letter:')
    used.append(guess)
    if guess in word:
        print('Yes!\'' +guess+'\'is in the word!')
        
        new = ''
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print('Sorry,letters\'' + guess + '\'not in the word.')
        wrong += 1
    if wrong == max_wrong:
        print(HANGMAN[wrong])
        print('you were hanged!')
    else:
        print('you guessed the word!')

    print('The hidden word was\''+ word +'')

<h1 align="center">In this game you have to find random numbers</h1>


          **And the game is called 'find a random number'**

    import random

    a = random.randint(1,10)

    chances = 7

    b = int(input('num='))

    start = 0

    stop = 7

***Function***

    while start<=stop:

    if b<a:
        print('ulkenrek san jaz')
    elif a>b:
        print('kishirek san jaz')
    else:
        print('ten')
        break
    b = int(input('num=')) 
    print(a)
    start+=1