#requestsExm.py 2.7
#demonstrates the requests module
#downloads a text file and than saves it to the computer
import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt') #download the file at this URL
try:
    res.raise_for_status() #raise am exception if status code is not 200 OK
    playFile=open('RomeoAndJuliet.txt','wb') #importent to open in wb mode to keep unicode characters
    for chunk in res.iter_content(100000): #divides the content into chunks the size of 100000 bytes
        playFile.write(chunk) #save each chunk

except Excption as exc:
    print 'An Error has occured',exc
    
