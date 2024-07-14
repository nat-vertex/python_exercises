from bs4 import BeautifulSoup
import codecs
import os
import re


def create_soup(filename):
    f = codecs.open(filename, 'r', 'utf-8') 
    html = f.read()
    return BeautifulSoup(html, 'xml')

  
    
    
dict_desc_data = dict()

directory = 'C://Users//user//Downloads//Telegram Desktop//DataExport_2024-07-13//chats'
files = os.listdir(directory)

directories_files = []
for i in files:
    files_down = os.listdir(directory + str('//') + str(i))
    for file in files_down: 
        if 'messages' in file: 
            directories_files.append(directory + str('//') + str(i) + str('//')  + str(file))

for directory in directories_files:
    
    filename = directory
    soup = create_soup(filename)
 
    
    #название группы
    parent = soup.find('a', attrs = {'class':re.compile("content block_link")}) #определить элемент, в который вложен искомый
    desctext = parent.find('div', attrs = {'class':re.compile("text bold")}) #по родителю найти потомка с нужным классом
    desctext = desctext.text.strip()
    #дата создания
    parent = soup.find('div', attrs = {'id':re.compile("message-1")}) #определить элемент, в который вложен искомый
    datetext = parent.find('div', attrs = {'class':re.compile("body details")})
    datetext = datetext.text.strip()
    datetext_list = datetext.split()
    
    
    datetext_list[0] = datetext_list[0] if len(datetext_list[0]) == 2 else str(0) + datetext_list[0]
    
    #в 3.10 заменить на match case
    if datetext_list[1] == "January":
        output = '01'
    if datetext_list[1] == "February":
        output = '02'
    if datetext_list[1] == "March":
        output = '03'
    if datetext_list[1] == "April":
        output = '04'
    if datetext_list[1] == "May":
        output = '05'
    if datetext_list[1] == "June":
        output = '06'
    if datetext_list[1] == "July":
        output = '07'
    if datetext_list[1] == "August":
        output = '08'
    if datetext_list[1] == "September":
        output = '09'
    if datetext_list[1] == "October":
        output = '10'
    if datetext_list[1] == "November":
        output = '11'
    if datetext_list[1] == "December":
        output = '12'
            
    datetext_list[1] = output
    datetext = '.'.join(datetext_list)

    dict_desc_data [desctext] = datetext

    
    
for i in dict_desc_data:
    print(i,  dict_desc_data[i])    
