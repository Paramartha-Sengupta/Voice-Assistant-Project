# Voice Assistant

Have you ever felt that some of your daily tasks could be done by your computer- without your involvement? 
Like playing a soothing song for your relaxation or helping you with the meaning of "reconnaissance"? You may think I have Alexa/Siri for that- But how cool is it to make your own Virtual Assistant? Like instead of being just a consumer, what if you could be the creator? 

Seems interesting???  
![image](https://user-images.githubusercontent.com/68769656/157397575-58da95ab-942b-474f-96f7-008644f6258c.png)

In this Repository I have created a Virtual Assiatnt of my own. Well, being a huge fan of the Office US, I named him Dwight!
![image](https://user-images.githubusercontent.com/68769656/157396476-316e1de8-b191-44ff-a366-7385cf6ff6f0.png)

So the question arises, what can Dwight do for me?  
![image](https://user-images.githubusercontent.com/68769656/157404136-1a24b7a1-9903-4907-8bfd-e3bbcf5dd520.png)


1. Hey Dwight, can you search for an information from Wikipedia for me?  
![image](https://user-images.githubusercontent.com/68769656/157400158-b6d62e09-4723-4e26-b836-688b97ea10fb.png)

2. What about any song I wish? Is that too possible?  
![image](https://user-images.githubusercontent.com/68769656/157400238-23be56c4-b738-4186-bb94-4bff691f453d.png)

3. Can you read out the latest news Headlines? I didn't have time to go through the newspaper today morning.  
![image](https://user-images.githubusercontent.com/68769656/157403959-c0180d6e-9672-46c4-8ef4-27e324e10bfc.png)

4. Impressive! What about a quick joke?  
![image](https://user-images.githubusercontent.com/68769656/157404610-332e5d2c-688f-4d8c-9ed6-767154d82541.png)

5. Can you tell me the exact weather outside? Not just my place... anywhere I want?  
![image](https://user-images.githubusercontent.com/68769656/157404751-9e2c406c-6422-4b59-a298-4bbc50eb503c.png)

6. Damn! Lets give you some really tough work. Can you send a Whatsapp message to any of my contacts?   
![image](https://user-images.githubusercontent.com/68769656/157405894-519be5a5-9e30-4346-a134-b54f061663a8.png)

OMG! That's amazing... Are you still interested to learn more tricks and perform even more difficul tasks??  
![image](https://user-images.githubusercontent.com/68769656/157406177-e18912b7-6088-4a4a-ac7e-5add2c311cad.png)

Well, We see Dwight is an awesome assistant! Now let us deep-dive a bit on the Technical End

# Vitual Assistant- Technical Aspect

Let us deep-dive to understand what are the action items we need to keep in mind for creating an awesome virtual assistant?
1. Speaking out the commands for the user
2. Receiving, Recording and Storing the voice command from the user
3. Connecting the request to the required application API and displaying the action initaiated as the output

Let us understand each of the items in the above list in details:

#### 1.  Speaking out the commands for the user

We have implemented the python library- "pyttsx" for the same. pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3. There are multiple advantages associates with this library:
  i. The Speaking style is completely controlled by the Programmer and is simple to use
  ii. The Speaking Voice, Rate and Volume can be easily modified to suit the requirement
  iii. The Documentation is clear and complete.

You can read more about this library from this link: https://pypi.org/project/pyttsx3/

#### 2. Receiving, Recording and Storing the voice command from the user

Have used the "speechrecognition" library for this action. This library is used for performing speech recognition, with support for several engines and APIs, online and offline. Once the command is recieved it is stored into the variable as a string. The instruction (which is now present in the string variable), can now be parsed to find the keywords that the assistant shall be acting upon. For example, If the user requests something like- "Can you play a video for me?". With the help of the speech recognition library this instruction will be captured. The parser will be focussing on the word "video", and identify the action that it needs to play a video in Youtube.

You can read more about the library here: https://pypi.org/project/SpeechRecognition/

### 3. Connecting the request to the required application API and displaying the action initaiated as the output

In this application, we have used "Chromedriver.exe", and will be providing the X-Path link for it to execute. For Example, I am interested to know about Elon Musk, and I request Dwight as "Can you give me some information on Elom Musk?". The text processing action would be focussing on the "information" part, and knows that it will be reaching out to the Wikipedia page for this information. Now in the search bar of Wikipedia (which will be fetched by the X-Path information provided, the key word "Elon Musk" will be placed. The click button for searching will be automatically initiated- and voila! The Wikipedia Page for viewing information about Elon Musk will be available.

# Next targets for Development:

## Short-Term targets

1. Enable Dwight to Share a mail to the desired recipient.  
2. Implementing the voice assiatnce to find help on more specific domains:
    i. Like suggesting the best platform for buying a Wishlist item- (Store/Platform that is having the best reviewed item at the cheapest prices)  
    ii. Recommendation System Enablement  
    iii. Give insights on investment etc.  
3. Calling Features  

## Long-Term Targets

1. Creating a Draft E-mail writeup for the topic as mentioned by the user
2. Home Appliances control through Voice Assitant (Need to check on the Feasibility- Hardware Requirements)
