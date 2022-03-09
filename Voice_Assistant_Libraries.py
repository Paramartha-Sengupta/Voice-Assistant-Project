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
