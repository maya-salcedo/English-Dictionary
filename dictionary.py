import json

data = json.load(open('data.json'))

def definition(word):
    if word in data:
        return(data[word])
    else:
        return('That does not exist in my dictionary. Sorry.')

while True:
        word_to_check = input('Enter a word:').strip().lower()
        print(definition(word_to_check))