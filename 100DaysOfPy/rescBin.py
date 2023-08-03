def addTwo(x,y):return x+y
def addTwo(x,y):return x-y

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def hangmanAscii (input):
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
  return HANGMANPICS[input]