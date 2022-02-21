Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

def add_prefix_un(word):
    '''
 
    :param word: str of a root word
    :return:  str of root word with un prefix
 
    This function takes `word` as a parameter and
    returns a new word with an 'un' prefix.
    '''
    return 'un'+word
def make_word_groups(vocab_words):
    '''
 
    :param vocab_words: list of vocabulary words with a prefix.
    :return: str of prefix followed by vocabulary words with
             prefix applied, separated by ' :: '.
 
    This function takes a `vocab_words` list and returns a string
    with the prefix  and the words with prefix applied, separated
     by ' :: '.
    '''
    prefix = vocab_words[0]
    return prefix+' :: '+' :: '.join(prefix+word for word in vocab_words[1:])
def remove_suffix_ness(word):
    '''
 
    :param word: str of word to remove suffix from.
    :return: str of word with suffix removed & spelling adjusted.
 
    This function takes in a word and returns the base word with `ness` removed.
    '''
    root = word[:-4]
    return root if root[-1] != 'i' else root[:-1]+'y'
def adjective_to_verb(sentence, index):
    '''
 
    :param sentence: str that uses the word in sentence
    :param index:  index of the word to remove and transform
    :return:  str word that changes the extracted adjective to a verb.
 
    A function takes a `sentence` using the
    vocabulary word, and the `index` of the word once that sentence
    is split apart.  The function should return the extracted
    adjective as a verb.
    '''
    return sentence[:-1].split()[index]+'en'
