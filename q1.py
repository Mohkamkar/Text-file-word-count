
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

