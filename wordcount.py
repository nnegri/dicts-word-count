import string
import sys

def word_count(file_name):
    """ Create function to count occurances of each words in file_name"""


    #Created a function called word_tally pointing to file_name that is undefined atm
    
    text = open(file_name)

    word_tally = {}

    for line in text:
        words = line.rstrip().split(' ')

        for word in words:
            word = word.lower().rstrip(string.punctuation)
            word_tally[word] = word_tally.get(word, 0) + 1

    for entry in word_tally.iteritems():
        print '%s %d' %  (entry[0], entry[1])

    return word_tally


file_name = sys.argv[1]
word_count(file_name)