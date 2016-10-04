import string, sys
from collections import Counter

def word_count(file_name):
    """ Create function to count occurances of each words in file_name"""

    #Created a function called word_tally pointing to file_name that is undefined atm
    
    text = open(file_name)

    #word_tally = {} # Empty dictionary
    word_tally = Counter() # Empty Counter

    for line in text:
        words = line.rstrip().split(' ') # Split each line into separate words

        for word in words:
            # Make word all lowercase, and remove punctuation
            word = word.lower().rstrip(string.punctuation) 
            # Store word in dictionary, along with corresponding count
            #word_tally[word] = word_tally.get(word, 0) + 1
            # Store word with in Counter, increase count by 1
            word_tally.update({word:+1})

    # for entry in word_tally.iteritems(): # Each 'entry' is a tuple in a new list
    #     print '%s %d' %  (entry[0], entry[1]) # Print information in each tuple
    for entry in word_tally:
        print '%s %d' % (entry, word_tally[entry]) # Print word and corresponding tally in Counter

    return word_tally # Return dictionary so you can use it in other functions

# Use sys.argv, so in the Python shell you can call whichever textfile you want
# For example, in terminal call: python wordcount.py test.txt
file_name = sys.argv[1]
word_count(file_name)