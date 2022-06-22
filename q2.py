
#------------------------------------------------------#
# Read file.txt
#------------------------------------------------------#

with open('sample.txt', 'r') as file:
    text = file.read()


# Cleaning the text from given characters
# Iterate over all key-value pairs in dictionary

#------------------------------------------------------#
# CLEAN function
#------------------------------------------------------#

def clean_text(text):
    #replacement characters

    replacements = {
                   
                   '"',
                   "'",
                   '/t',
                   '/n',
                   '?',
                   ';'}
    for char in replacements:
        text = text.replace(char, '')
    return text



# Cleaning the text
clean_text(text)


# lower case function
def lower_case(text):
    words = text.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    return words
words = lower_case(text)
    
#print('Total Words:', len(words))

#------------------------------------------------------#
# print the number of words
#------------------------------------------------------#

def counting_words(words):
    for w in words:
        w_count = words.count(w)
        print('%s : '%w ,w_count)
        
counting_words(words)



#Closing the fiel
file.close()


   

