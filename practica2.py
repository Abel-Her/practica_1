
# Ahorcado
# -----------------------------------
# Código Auxiliar
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Fin del código Auxiliar

# -----------------------------------

# Se cargan palabras del archivo de texto y se define un abecedario en ingles:
wordlist = load_words()
abc='abcdefghijklmnopqrstuvwxyz'
labc = list(abc)

#Función que comprueba si la palabra ha sido adivinada.
def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    a = set(secret_word)
    b = set(letters_guessed)
    c = bool(a.issubset(b))

    return c

#Función que devuelve el progreso del juego:
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    b = set(letters_guessed)
    a = list(secret_word)
    wrd = []
    for i in a:
        if i in b:
            wrd.append(i)
        else:
            wrd.append(' _')

    c = ''.join(wrd)
    return c


#Regresa las letras que aún no han sido adivinadas.
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    b = []
    for i in labc:
        if i in letters_guessed:
            pass
        else:
            b.append(i)

    c = ''.join(b)
    return c
#Función que cuenta los elementos de un conjunto:
def cardinality(set):
    s = list(set)
    n = 0
    for k in s:
        n+=1
    return n
#Función para iniciar el Ahorcado
def hangman(secret_word):
    print('I am thinking of a word that is',len(secret_word),'letters long')
    print('________________________________________________________________')
    letters_guessed = []
    #Intentos
    tries = 6
    #Advertencias
    w = 3
    wb =  w
    wc =  w
    while tries > 0:
        print('You have',tries,'guesses left')
        print('Available letters:', get_available_letters(letters_guessed))
        print('Please guess a letter:')
        try:
            l = input()
            l = l.lower()
            if l not in labc:
                 wb-=1
                 print('Only Alphabet letters please :/', get_guessed_word(secret_word, letters_guessed))
                 if wb > 0:
                     print('WARNING #',w-wb,'If you repeat this error three times in a row, you will lost a try')
                 else:
                     print('You lost a try, please follow the rules.')
            if l in labc:
                if l in letters_guessed:
                    wc-=1
                    print('This letter is guessed :/', get_guessed_word(secret_word, letters_guessed))
                    if wc > 0:
                        print('WARNING #',w-wc,'If you repeat this error three times in a row, you will lost a try')
                    else:
                        print('You lost a try, please follow the rules.')
                if l in list(secret_word) and l not in letters_guessed:
                    wc = w
                    wb = w
                    letters_guessed.append(l)
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                if l not in list(secret_word) and l not in letters_guessed:
                    wc = w
                    wb = w
                    print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
                    letters_guessed.append(l)
                    if l in list('aeiou'):
                        tries-=2
                    if l in list('bcdfghjklmnpqrstvwxyz'):
                        tries-=1
        except AttributeError:
            wb-=1
            print('Only Alphabet letters please :/', get_guessed_word(secret_word, letters_guessed))
            if wb > 0:
                print('WARNING #',w-wb,'If you repeat this error three times in a row, you will lost a try')
            else:
                print('You lost a try, please follow the rules.')
        if wc <= 0 or wb <= 0:
            tries -= 1
            wc = w
            wb = w
        if is_word_guessed(secret_word, letters_guessed):
            print('You won! :D')
            print('You have',tries*cardinality(set(secret_word)), 'points')
            print('________________________________________________________________')
            tries = 0
        if tries <= 0 and not is_word_guessed(secret_word, letters_guessed):
            print('Sorry, you lose, the word is:',secret_word)
            print('________________________________________________________________')
            tries = 0
        print('________________________________________________________________')

hangman(choose_word(wordlist))
#Para forzar a que una palabra es sea la que se quiere:
# hangman('vacuna')
