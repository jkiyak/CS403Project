"""
Preston Levert Mitchell
Scrapper

Summary: A script thats runs once every thirthy minites and grabes key information from news sites.


Main: Starts the Scraper; gets website request
    ;grabs the data by function calls
    ;prints data to output file

recv: Gets the content for src request
    ;puts into parsable html
    ;returns this

getit: seperates the html and grab whats needed
    ;parses headline text, hyperlink, image
    ;returns this in a list that contains a list within

pushit: pushes the data to a specific file as a txt
    ;file path then uses jsondump to drop text

Using schedule to run every hour;

"""
import os
import time
import schedule
import simplejson
import requests
from bs4 import BeautifulSoup

def main():
    print('Scraper Started...')
    website = input()
    web = requests.get(website)
    code = web.status_code
    print(code)
    print('\n')
    if code != 200:
        print('Error on requesting Page.')
        exit()

    source = recv(web)
    the_data = getit(source.find_all('div',{'class':'media'}))
    print('\n')
    print('Website Scrapped Information Obtained.'+'\n'+'Pushing information...')
    pushit(the_data)
    print('\n\n\nWaiting an hour till next info grab.')
    
    
        
def recv(call):
    soup = BeautifulSoup(call.content,'html.parser')
    return soup

def getit(zeta):
    the_data = []
    for i in zeta:
        print(i)
        print('\n')
        if i.img.get('alt') != "":
            hold = [i.img.get('alt'),i.a.get('href'),i.img.get('data-src-large')]
            the_data.append(hold)
    return the_data

def pushit(call):
    #path = easygui.fileopenbox()
    out_file = 'Data.txt'
    file = open(out_file,'w')
    simplejson.dump(call,file)
    file.close()
    
main()
##schedule.every().hour.do(main)
##while True:
##    schedule.run_pending()
##    time.sleep(1)
