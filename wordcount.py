def word_count(file_name):
    """ Create function to count occurances of each words in file_name"""


    #Created a function called word_tally pointing to file_name that is undefined atm

    text = open(file_name)

    word_tally = {}

    for line in text:
        words = line.strip().split(' ')

        for word in words:
            word_tally[word] = word_tally.get(word, 0) + 1

    for entry in word_tally.iteritems():
        print '%s %d' %  (entry[0], entry[1])

    return word_tally

word_count("twain.txt")