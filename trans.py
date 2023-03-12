import sys
from googletrans import Translator
from gtts import gTTS
import os
from playsound import playsound

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
    
    # convert the text to speech
    tts = gTTS(text=string, lang='en')
    
    # create a temporary file to store the speech
    temp_file = "temp.mp3"
    tts.save(temp_file)
    
    # play the speech
    playsound(temp_file)

    # delete the temporary file
    os.remove(temp_file)
    

    
    







