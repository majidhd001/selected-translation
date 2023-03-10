import sys
from googletrans import Translator
import pyttsx3


#sudo apt-get install espeak libespeak-dev libportaudio2
# initialize the text-to-speech engine
engine = pyttsx3.init()

# set the voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', 'Persian+English-US') # you can choose any available voice

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 50)

#for voice in voices:
#    print("Voice ID:", voice.id)
#    print("Name:", voice.name)
#    print("Languages:", voice.languages)
#    print("Gender:", voice.gender)
#    print("Age:", voice.age)

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
    engine.say(string)
    engine.runAndWait()
    
    







