# 내가 좋아하는 노래에서 어떤 말이 가장 많은지 확인

import requests
from bs4 import BeautifulSoup
import bs4
import collections

url = "https://music.naver.com/lyric/index.nhn?trackId=3022119"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

section_result = soup.find('div', class_='show_lyrics')

lyrics1 = [str(line) for line in section_result if not isinstance(line, bs4.element.Tag)]

lyrics1 = ' '.join(lyrics1).split()

url = "https://music.naver.com/lyric/index.nhn?trackId=2319164"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

section_result = soup.find('div', class_='show_lyrics')

lyrics2 = [str(line) for line in section_result if not isinstance(line, bs4.element.Tag)]

lyrics2 = ' '.join(lyrics2).split()

url = "https://music.naver.com/lyric/index.nhn?trackId=22205276"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

section_result = soup.find('div', class_='show_lyrics')

lyrics3 = [str(line) for line in section_result if not isinstance(line, bs4.element.Tag)]

lyrics3 = ' '.join(lyrics3).split()

url = "https://music.naver.com/lyric/index.nhn?trackId=16676937"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

section_result = soup.find('div', class_='show_lyrics')

lyrics4 = [str(line) for line in section_result if not isinstance(line, bs4.element.Tag)]

lyrics4 = ' '.join(lyrics4).split()

url = "https://music.naver.com/lyric/index.nhn?trackId=4044278"
result = requests.get(url)
soup = BeautifulSoup(result.text, 'html.parser')

section_result = soup.find('div', class_='show_lyrics')

lyrics5 = [str(line) for line in section_result if not isinstance(line, bs4.element.Tag)]

lyrics5 = ' '.join(lyrics5).split()
# 각 노래를 가져와서 단어로 분류

lyrics = []
lyrics += lyrics1
lyrics += lyrics2
lyrics += lyrics3
lyrics += lyrics4
lyrics += lyrics5
print(lyrics)

word_count = collections.Counter(lyrics)
word_count = sorted(word_count.items(), key=lambda x:x[1], reverse=True)
print(word_count)

# 들어가 있는 내용을 많은 순으로 분류







"""
import csv
import string

list = []
list += [line for line in section_result]

print(list)


# ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

for aaa in list
    if aaa !== <br/>
    list.append(aaa)

list[1] = '1'

items = []
for i in range(0, 2):
    for items in list
        items = list[i].split()
    print(items)



import re
import nltk
chat_words = sorted(set(w for w in items)



[w for w in chat_words if re.search ("[a-zA-Z]+",w)]

print(w)

aa = [line for line in list if not re.search('^r', list)]
print(aa)
"""

