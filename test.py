
import urllib.request, urllib.parse
import requests
import os

url_list = ['https://vietnamnet.vn']
url = url_list.pop(0)

response = urllib.request.urlopen(url)
data = response.read()



os.mkdir("thu")
os.chdir("thu")
file = 'baomoi' + '.html'
f = open(file, 'wb')

f.write(data)    #Nhập nội dung file
f.close()