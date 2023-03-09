import sys
from googletrans import Translator

def translate_word(word):
    # Instantiates a translator
    translator = Translator()

    # Translates the input word to Farsi
    translation = translator.translate(word, dest='fa')

    print(f'{translation.text}')

if __name__ == '__main__':
    args = [arg for arg in sys.argv[1:]]
    string = ' '.join(args)
    translate_word(string)

