# -*- coding: utf-8 -*

import urlparse
import requests
import urllib
import re
from difflib import Differ
import sys


from settings import NETWORK


def get_sender(url,bypass=None,cookie=None,useproxy=None,get_full_request=False,request_param_for_atack=None,post=None):
    SplitResult=urlparse.urlsplit(url)
    if type(request_param_for_atack)==str:
        request_param_for_atack=re.split('[|;,]',request_param_for_atack)
    if post:
        meanings_array=[]
        param_array=[]
        for el in post.split('&'):
            param_array.append((re.search(r'\S*(?=\=)',el)).group())
            meanings_array.append((re.search(r'(?<==)\S*',el)).group())
        
    else:
        param_array=re.findall(r'(?<=^)\S*?(?=\=)',SplitResult.query)
        param_array=param_array+(re.findall(r'(?<=&)\S*?(?=\=)',SplitResult.query))
        if len(request_param_for_atack)==0 and len(param_array)>1:
            print("I dont know param for inject. Pls use -p name_of_param")
        if re.findall(r'&',SplitResult.query) is not None:
            meanings_array=re.findall(r'(?<==)\S*?(?=&)',SplitResult.query)
            last_param=re.escape(param_array[-1])
            meanings_array=meanings_array+re.findall(r'(?<='+last_param+'=)\S*?(?=$)',SplitResult.query)
        else:
            meanings_array=re.findall(r'(?<=\=)\w*',SplitResult.query)
    if bypass:       
        # как красиво обрабатывать наличие порта?
        bypass=urllib.quote(bypass, safe='')
        my_url=SplitResult.scheme+'://'+SplitResult.hostname+'/'+SplitResult.path+'?'
        postdata=''
        for param in param_array:
            i=0
            for prm_to_atack in request_param_for_atack:
                if param==prm_to_atack:
                    meanings_array[i]=bypass
                i+=1
        for param in param_array:
            i=0
            my_url=url+'&'+str(param)+'='+str(meanings_array[i])
            postdata=postdata+'&'+str(param)+'='+str(meanings_array[i])
            i+=1
        postdata=postdata[1:]
        

    #sys.exit()
    http_proxy  = NETWORK.http_proxy
    https_proxy = NETWORK.https_proxy

    proxyDict = { 
                "http"  : http_proxy, 
                "https" : https_proxy,
            }
    host='\'Host\':\''+SplitResult.netloc+'\''
    user_agent=NETWORK.user_agent

    # mb some thig different in accept?
    accept='\'Accept\':\'application/json, text/javascript, */*; q=0.01\''
    accept_language=NETWORK.accept_language
    accept_encoding=NETWORK.accept_encoding
    referer='\'Referer\':\''+url+'\''

    # Need get cookie from user
    if cookie:
        a=cookie.split(':')
        cookie={a[0]:a[1]}

    headers={host,user_agent,accept,accept_language,accept_encoding,referer}
    
    if useproxy:
        try:
            if post:
                response=requests.post(url,cookies=cookie,proxies=proxyDict,data=postdata)
            else: 
                response=requests.get(my_url,cookies=cookie,proxies=proxyDict)
        except:
            print("Can not connect to "+url)
            print("We use proxy:"+http_proxy)
            sys.exit()
    else:
        try:
            if post:
                response=requests.post(url,data=postdata,cookies=cookie)            
            else:
                response=requests.get(my_url,cookies=cookie)
        except:
            print("Can not connect "+url) 
            sys.exit()

    #print("stage_3 url: "+url)
    if (get_full_request==True):
        return(response.content)
    return(response.status_code)


def response_dif(response1,response2):
    d=Differ()
    diff = d.compare(response1, response2)
    i=0
    for el in diff:
        if re.match(r'\+|-',el):
            i+=1
    return i

def bypass_tester(my_url,bypass,cookie,proxy,response,request_param_for_atack,post):
    #get_sender(url,bypass=None,cookie=None,useproxy=None,get_full_request=False,request_param_for_atack=[],post):
    result=get_sender(my_url,bypass,cookie,proxy,response,request_param_for_atack,post)
    if response==False:
        if str(result)[0]=='4':

            return 0
        elif  str(result)[0]=='5':

            return 2
        elif  str(result)[0]=='2':

            return 1
        elif  str(result)[0]=='3':
 
            return 1
        else:
            print 'Nothing ' +str(result)[0]
            return 0


if __name__ == "__main__": 
    my_url='http://challenge01.root-me.org/web-serveur/ch9/'
    post='login=123&password=456'

    response1=bypass_tester(my_url,'$20==!','cOOka:test',True,False,'password',post)

