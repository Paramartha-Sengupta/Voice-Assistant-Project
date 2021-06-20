# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 00:26:50 2021

@author: Paramartha
"""
import requests
key='5fb3d5ec05a14630bd1608fe136a9f28'

api_address='https://newsapi.org/v2/top-headlines?country=in&apiKey='+key
json_data=requests.get(api_address).json()

#News
news_arr=[]
def news():
    for i in range(1):
        news_arr.append("number"+str(i+1)+":- "+json_data["articles"][i]['title']+'.')
    return news_arr








