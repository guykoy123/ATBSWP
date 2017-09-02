#python 2.7
#lucky.py - Opens several Google search results

import requests,sys,webbrowser, bs4

print('Googling...')  #display text while downloading the google page
res=requests.get('http://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status() #check for correct page download

soup=bs4.BeautifulSoup(res.text) #parse HTML

linkElems=soup.select('.r a')
numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com'+linkElems[i].get('href'))
    
