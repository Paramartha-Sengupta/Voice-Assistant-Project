# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:22:39 2021

@author: PARAMARTHA SENGUPTA
"""

import pyttsx3 as p
import speech_recognition as sr
#from YT_auto import *
from selenium import webdriver
from key_file import * 
from key_file_2 import * 
import requests
import randfacts

#Search in Wikipedia
class Infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users/Paramartha/Desktop/chromedriver_win32/chromedriver.exe')
    
    def get_info(self,query):
        self.query=query
        self.driver.get(url='https://www.wikipedia.org')
        search=self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()
        

#Youtube
class music():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users/Paramartha/Desktop/chromedriver_win32/chromedriver.exe')
    
    def play(self,query):
        self.query=query
        self.driver.get(url='https://www.youtube.com/results?search_query='+query)
        video=self.driver.find_element_by_xpath('//*[@id="title-wrapper"]')
        video.click()
        

#Jokes
url='https://official-joke-api.appspot.com/random_joke'
json_data=requests.get(url).json()

arr=['','']
arr[0]=json_data['setup']
arr[1]=json_data['punchline']

def joke():
    return arr



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
               
        
