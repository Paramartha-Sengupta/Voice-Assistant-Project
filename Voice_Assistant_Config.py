from selenium import webdriver
import requests

 
#Search in Wikipedia
class Infow():
    def __init__(self):
        self.driver=webdriver.Chrome(executable_path='C:/Users/USER/Desktop/chromedriver.exe')
    
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
        self.driver=webdriver.Chrome(executable_path='C:/Users/USER/Desktop/chromedriver.exe')
    
    def play(self,query):
        self.query=query
        self.driver.get(url='https://www.youtube.com/results?search_query='+query)
        video=self.driver.find_element_by_xpath('//*[@id="title-wrapper"]')
        video.click()
        
#Jokes
"""url='https://official-joke-api.appspot.com/random_joke'
json_data=requests.get(url).json()

arr=['','']
arr[0]=json_data['setup']
arr[1]=json_data['punchline']

def joke():
    return arr"""


key='5fb3d5ec05a14630bd1608fe136a9f28'

api_address='https://newsapi.org/v2/top-headlines?country=in&apiKey='+key
json_data=requests.get(api_address).json()

#News
news_arr=[]
def news():
    for i in range(1):
        news_arr.append("number"+str(i+1)+":- "+json_data["articles"][i]['title']+'.')
    return news_arr
