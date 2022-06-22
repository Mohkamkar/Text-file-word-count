# Write code in your favorite programming language to output count of each word found in ‘sample.txt’ file.
# The count should represent the number of times a word appears in the text. 
# Your code can implement a brute force approach to count the words
# -	Input: String or file path to ‘sample.txt’
# -	Output: words and their count

# Read file.txt
with open('sample.txt', 'r') as file:
    text = file.read()

# Cleaning the text from given characters
text = text.replace('"','')
text = text.replace("'",'')
text = text.replace('/t','')
text = text.replace('/n','')
text = text.replace('?','')
text = text.replace(';','')


# lower case

words = text.split()
for i in range(len(words)):
   words[i] = words[i].lower()
    
print('Total Words:', len(words))
# print the number of words
for w in words:
    w_count = words.count(w)
    print('%s : '%w ,w_count)

