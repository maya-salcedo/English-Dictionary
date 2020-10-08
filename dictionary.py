import json
import difflib

data = json.load(open('data.json'))

def definition(word):
    while True:
        if word in data:
            return(data[word])
        else:
            try:
                alternative_word = difflib.get_close_matches(word, data, n=1)
                word = alternative_word[0]
                return("Do you mean " + word + "?\n" + str(data[word]))
            except IndexError:
                return('that is not in my dictionary. sorry')
                break

while True:
        word_to_check = input('Enter a word:').strip().lower()
        print(definition(word_to_check))
