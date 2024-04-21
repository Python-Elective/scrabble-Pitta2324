import random
import string
 
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
 
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
 
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
 
WORDLIST_FILENAME = "words.txt"
 
 
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
 
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list
 
 
def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
 
    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq
 
 
# (end of helper code)
# -----------------------------------
 
#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
 
    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.
 
    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)
 
    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    assert isinstance(word,str), "word must be a string"
   
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
        assert isinstance(n, int), "n must be an int"
    assert n >= 0, "hand length n must not be 0"
       
    def get_word_score(word, n):
        word = word.lower()
    total_score = sum(SCRABBLE_LETTER_VALUES.get(letter, 0) for letter in word) * len(word)
    if len(word) == n:
        total_score += 50
    return total_score
 
#testcases for logic
print(get_word_score("waybill", 7)) #155
 
#testcases for assertion
#Legal
# print(get_word_score("haPPy", 7))
# #Illegal
# print(get_word_score(1000, 7))
# print(get_word_score("", 7))
# print(get_word_score("blabla", 0))
 
#
# Problem #2: Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.
 
    For example:
    >>> display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.
 
    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for _ in range(hand[letter]):
            print(letter, end=" ")       # print all on the same line
    print()                             # print an empty line
display_hand({'a':1, 'x':2, 'l':3, 'e':1})
#
# Problem #2: Make sure you understand how this function works and what it does!
#
 
 
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
 
    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.
 
    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3
 
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
 
    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
 
    return hand
 
print(deal_hand(HAND_SIZE))
 
#
# Problem #2: Update a hand by removing letters
#
 
 
def update_hand(hand: dict, word: str) -> dict:
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
 
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.
 
    Has no side effects: does not modify hand.
 
    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
 
    assert isinstance(word,str), "word must be a string"
   
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
 
    output = hand.copy()
    for letter in word:
        if letter in output.keys() and output[letter] > 0:
            output[letter] -= 1
    return output
 
#testcase
print(update_hand({'a': 1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, "quail"))
print(update_hand({'a': 0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}, "quail"))
 
#
# Problem #3: Test word validity
#
def is_valid_word(word: str, hand: dict, word_list: list) -> bool:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
 
    Does not mutate hand or word_list.
 
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
   
    assert isinstance(word,str), "word must be a string"
   
    if len(word) > 0:
        word = word.lower()
        assert word.islower(), "lower() conversion failed"
   
    new_hand = hand.copy()
 
    for letter in word:
        if letter not in new_hand or new_hand[letter] == 0:
            return False
        else:
            new_hand[letter] -= 1
   
    if word not in word_list:
        return False
   
    return True
 
#testcases
print(is_valid_word("hello", {'h': 1, 'e':1, 'l':2, 'o':1, 'u':1, 'i':1}, ["hello", "pitta"]))
print(is_valid_word("hello", {'h': 1, 'e':1, 'l':1, 'o':2, 'u':1, 'i':1}, ["hello", "pitta"]))
print(is_valid_word("pitta", {'p': 1, 'i':1, 't':2, 'a':2, 'u':1, 'i':1}, ["hello", "pitta"]))
 
#
# Problem #4: Playing a hand
#
 
def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.
 
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    sum = 0
    for value in hand.values():
        sum += value
    return sum
 
 
def play_hand(hand, word_list, n):
    """
    Allows the user to play the given hand, as follows:
 
    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."
 
      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
 
    """
    score = 0  # Initialize score
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    while calculate_hand_len(hand) > 0:
        # Display the hand
        print('Current Hand:', end=' '); display_hand(hand)    
        # Ask user for input
        guess = str(input('Enter word, or a "." to indicate that you are finished: '))        
        # If the input is a single period:
        if guess == '.':        
            # End the game (break out of the loop)
            break            
        # Otherwise (the input is not a single period):
        else:        
            # If the word is not valid:
            if is_valid_word(guess, hand, word_list) == False:            
                # Reject invalid word (print a message followed by a blank line)
                print('Invalid word, please try again.', '\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                score += get_word_score(guess, n)
                print('"'+guess+'"', "earned", get_word_score(guess, n), "points. Total:", score, "points", '\n')
                # Update the hand
                hand = update_hand(hand, guess)              
 
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if guess == '.':
        print('Goodbye! Total score:', score, 'points.')
    else:
        print('Run out of letters. Total score:', score, 'points.')  
 
 
#testcase
word_list = load_words()
hand = {'h':1, 'i':1, 'c':1, 'n':1, 'm':2, 'a':1}
n = 5
play_hand(hand, word_list, n)
 
#
# Problem #5: Playing a game
#
 
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    # TO DO ... <-- Remove this comment when you code this function
    # <-- Remove this line when you code the function
    print("play_game not yet implemented.")
 
 
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)