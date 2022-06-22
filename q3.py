# code that takes the output from Q1 or Q2 as input and outputs the word with the highest count.

#import q2.py

import q2       
#q2.counting_words(q2.words)

def highest_frequency_word(words):
    highest_frequency = 0
    highest_frequency_word = ''
    for w in words:
        w_count = words.count(w)
        if w_count > highest_frequency:
            highest_frequency = w_count
            highest_frequency_word = w
    return highest_frequency_word, highest_frequency


highest_frequency_word(q2.words)
print("Highest_frequency_word:", highest_frequency_word(q2.words))
