import keyboard
from time import sleep
import win32clipboard as cb

def copy(code):

    cb.OpenClipboard()
    cb.EmptyClipboard()
    cb.SetClipboardData(cb.CF_UNICODETEXT, code) #puede que puedas cambiarlo a SetClipboardText
    cb.CloseClipboard()

def paste():

    keyboard.press_and_release('ctrl+v')

def write(code):

    copy(code)
    paste()

letters = 'aeioukstnhmyrwgzdbp'

pressed = {}
for letter in letters: pressed[letter] = False

was_pressed = ''

hiragana_codes = {
                    'ka':u'\u304b',
                    'ki':u'\u304d',
                    'ku':u'\u304f',
                    'ke':u'\u3051',
                    'ko':u'\u3053',
                    'a':u'\u3042',
                    'i':u'\u3044',
                    'u':u'\u3046',
                    'e':u'\u3048',
                    'o':u'\u304a',

                 }

detect = False
run = False

while True:

    sleep(0.01)

    if keyboard.is_pressed('ctrl+shift'): detect = True

    if detect == True and not keyboard.is_pressed('ctrl+shift'):
        detect = False
        run = not run

    if run:

        for letter in letters:

            if keyboard.is_pressed(letter):
                pressed[letter] = True

            if pressed[letter] and not keyboard.is_pressed(letter):
                was_pressed = was_pressed + letter
                pressed[letter] = False

        for syllable in hiragana_codes:

            if syllable in was_pressed:

                for letter in syllable: keyboard.press_and_release('backspace')
                write(hiragana_codes[syllable])
                was_pressed = ''
