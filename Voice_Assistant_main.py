
import pyttsx3 as p
import speech_recognition as sr
from Voice_Assistant_Config import *

engine=p.init()
#rate=engine.getProperty('rate')
#print(rate)

#voices=engine.getProperty('voices')
#print(voices)


engine.setProperty('rate',180)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Hello Sir! My name is Dwight, I am your assistant! How May I help You?')
print('Hello Sir! My name is Dwight, I am your assistant! How May I help You?')

r=sr.Recognizer()

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print('Listenting...')
    task=r.listen(source)
    text=r.recognize_google(task)
    print(text)
    
if "information" in text or 'detail' in text or 'Wikipedia' in text:
    speak('Please tell me the topic in which you need an Information')
    print('Please tell me the topic in which you need an Information')
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listenting...')
        task=r.listen(source)
        text2=r.recognize_google(task)
        
    speak('Searcing for {} in Wikipedia'.format(text2))  
    assist=Infow()
    assist.get_info(text2)
    
elif "video" in text or 'music' in text or 'song' in text:
    speak('Please tell me the video you want me to play!!!')
    print('Please tell me the video you want me to play!!!')
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listenting...')
        task=r.listen(source)
        vid=r.recognize_google(task)
    speak('Playing {} on Youtube'.format(vid))
    print('Playing {} on Youtube'.format(vid))
    assist=music()
    assist.play(vid)
    

elif "news" in text or 'update' in text:
    arr=news()
    print('Sure Sir! I will be reading out the Latest news for you')
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif 'fact' in text or 'facts' in text:
    x=randfacts.getFact()
    print('Did You Know That, {}'.format(x))
    speak('Did You Know That, {}'.format(x))
        
elif 'joke' in text or 'funny' in text:
    speak('Sure Sir! I have a joke for you')
    jokes=joke()
    print(arr[0])
    speak(arr[0])
    speak(' ')
    print(arr[1])
    speak(arr[1])   

elif 'weather' in text or 'condition outside' in text:
    print('Please tell me region whose weather you wish to know')
    speak('Please tell me region whose weather you wish to know')
    
    
    with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print('Listenting...')
        place=r.listen(source)
        region=r.recognize_google(place)
        print('You want to know about the weather of {}'.format(region))
        speak('You want to know about the weather of {}'.format(region))
        api_address='https://api.openweathermap.org/data/2.5/weather?q='+region+'&appid=7f5bdc88aa22bd90d58587a336eea2dd'
        json_data=requests.get(api_address).json()
        temp=round(json_data['main']['temp']-273,1)
        temp_feels=round(json_data['main']['feels_like']-273,1)
        description=json_data['weather'][0]['description']
        print('The Temparature in {} now is {}'.format(region,temp))
        print('The Temparature feels like ',temp_feels)
        print('The overall weather is: ',description)
        speak('The Temparature in {} is {}'.format(region,temp))
        speak('The Temparature feels like {}'.format(temp_feels))
        speak('The overall weather is: {}'.format(description))
               
