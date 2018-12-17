from django.http import HttpResponse
from django.shortcuts import render

import os
import sys
import urllib.request
import json, pprint
# Create your views here.

def link(request):
   
    client_id = ""    # 자신이 제공 받은 KEY ID 
    client_secret = ""   # 자신이 제공 받은 KEY 암호


    text = request.POST.get('text')
    encText = urllib.parse.quote(text)
    srcLang = 'ko'
    tarLang = 'en'
    data = "source={}&target={}&text=" .format(srcLang,tarLang) + encText
    
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))

    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        data = response_body.decode('utf-8')
        data = json.loads(data)
        trans_text = data['message']['result']['translatedText']
    else:
        print("Error Code:" + rescode)
    
    return HttpResponse(trans_text)

def trans(request):
    return render(request,'base/input.html')

