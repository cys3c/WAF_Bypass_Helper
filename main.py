# -*- coding: utf-8 -*
# for python 2.7

# как передавать спец символы, в команной троке пример: '> javascript:alert(1) <img \"  \" > <'"    --- приходитя экранировать кавычки в теге Img
# сделать нормальный хелп - чтобы автоматически добавлял возможные виды атак
# удлять одинаковые строки
# 3й python - не всё попадает в файл



import os
import sys
import re
import inspect
import argparse
from main_modules.settings import PRIORITY

#
mycwd=os.getcwd()




def use_bypass(technik,string):
    try:
        files = open(str(directory)+'/'+str(technik)+'/__init__.py')
    except Exception:
        print(u'Dir '+mycwd+'/'+str(directory)+'/'+str(technik)+' or __init__.py not found')
        sys.exit()
    else:
        files.close
        files = os.listdir(str(directory)+'/'+str(technik))
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
                    result=obj.tamper(string)
                    if type(result)==list:
                        print ('----------- more than 1 result --------------')
                        for el in result:
                            if el!=string:
                                print ("Method:"+module_name+ ' Priority '+str(priority)+' '+el)
                                write_to_file(el,outputfile)
                            else:
                                print("Method: "+module_name+" nothing to do")

                    elif type(result)==str:
                        if result!=string:
                            print ("Method:"+module_name+  ' Priority '+str(priority)+' '+result)
                            write_to_file(result,outputfile)
                        else:
                            print("Method: "+module_name+" nothing to do")
                    else:
                        print ("Ahtung "+str(type(result))+"Method:"+module_name )
                        print (str(result))

        
def main():
    global directory, outputfile
    directory='Tampers'
    parser=createParser()
    atack_params=parser.parse_args()
    injection_element  = atack_params.injstring
    type_atack = atack_params.typeofatack
    outputfile = atack_params.outputfile
    dbname = atack_params.dbname
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
 
    return parser

def write_to_file(string,filename):
    if filename:
        f = open(filename, 'a')
        f.write(string+'\n')
        f.close()
    else:
        pass

if __name__ == "__main__":      
    main()
