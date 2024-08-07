# python liabrary for human speech recognition
import speech_recognition as aa
#python liabrary for  text to speech
import pyttsx3
#python liabrary for automation of youytube and whatsapp
import pywhatkit
#python liabrary for date and time
import datetime

listener = aa.Recognizer()
#iniatializing pywhATKIT
machine = pyttsx3.init()

#Def. Func to hear 
def talk(text):
    #SAY-pass parameter and give the output
    machine.say(text)
    machine.runAndWait()

#giving input
def input_instruction():
    #ensure that insrtuction is global variable
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening..")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis','')
                print(instruction)
    
    except:
        pass
    return instruction

#func to include all the functionalities in jarvis
def play_jarvis():

    instruction = input_instruction()
    print(instruction)
    #use conditional statement for jarvis response
    if "play" in instruction:
        #allowing jarvis to respond to our input
        #replace fun will replace the  "play" 
        song = instruction.replace
        talk( "playing " +  song)
        pywhatkit.playsonyt(song)
        
    #adding date and time function     
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M%P')#format of date and time is written 
        #adding time
        talk('current time' + time)
    #adding date
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m')#format pf date
        talk("Today's date" + date) 
    
    elif 'How are you' in instruction:
        talk('I am Jhakas, how about you?')
    
    elif 'What is your name ' in instruction:
        talk('I am one and only Jarvis, What can i do for you?')
    
    elif:
        talk('Please repeat')
play_jarvis()