# -*- coding: cp1252 -*-
import speech_recognition as sr
import serial as ser
from random import randint

arduino_serial = ser.Serial('com3',9600)

r = sr.Recognizer()

while True:
    
    with sr.Microphone() as source:

        r.energy_threshold = 400

        print('habla ahora')
        audio = r.listen(source)
        
    try:
        
        print('procesando')
        message = r.recognize_google(audio,language='es-CL')
        
        print('- dijiste: '+message)
        
        if message == 'cerrar': exit()

        if 'aleatorio' in message:
            i_rand = message.find('aleatorio')
            numb = message[i_rand+10:]
            i_spacebar = numb.find(' ')
            i_end = numb.find(' fin')
            lower_limit = int(numb[0:i_spacebar])
            upper_limit = int(numb[i_spacebar+1:i_end])
            rand_numb = randint(min(lower_limit,upper_limit),max(lower_limit,upper_limit))
            i_extra = i_rand+i_end+14
            if i_extra == len(message):
                message = message[0:i_rand]+str(rand_numb)
            else:
                message = message[0:i_rand]+str(rand_numb)+message[i_extra:]
            print('- mensaje actualizado: '+message)
        
        if 'mover' in message:
            arduino_serial.write(chr(int(message[6:])))
        
        else:
            print('enter a command')
            
    except Exception as e:

        print('-------------')
        print(e)
        print('-------------')
