import json
import difflib

data = json.load(open('data.json'))

def definition(word):
    while True:
        if word in data:
            return(str(data[word]))
        elif word.title() in data:
            return data[word.title()]
        elif word.upper() in data:
            return data[word.upper()]
        else:
            try:
                alternative_word = difflib.get_close_matches(word, data, n=1)
                word = alternative_word[0]
                return("Do you mean " + word + "?\n" + str(data[word]))
            except IndexError:
                return('that is not in my dictionary. sorry')
                break

while True:
        word_to_check = input('Enter a word:').lower()
        output = definition(word_to_check)
        print(output)
