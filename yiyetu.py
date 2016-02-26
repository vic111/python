#下载一个网页的图
import os,re,codecs,urllib
from urllib import request
from bs4 import BeautifulSoup


#path='0.jpg'
#url="http://www.qiushibaike.com/"
#req=request.Request(url)
#req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
#with request.urlopen(req) as response:
#	a=BeautifulSoup(response.read().decode())
#for link in a.find_all('img'):#寻找soup中a的标签然后进行遍历
#	request.urlopen(link.get('src')).read()
#	#path=path+1
#	dirname=os.path.dirname(path.strip())
#	if not os.path.exists(dirname):
#		os.makedirs(dirname)
#	with open (i,'wb') as f:
#		f.write(data)



pageUrl = 'http://www.qiushibaike.com/'
req=request.Request(pageUrl)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
with request.urlopen(req) as response:
	soup=BeautifulSoup(response.read().decode())
print ("正在下载")
divHtml = soup.find_all("img")
for link in divHtml:
	data=request.urlopen(link.get('src')).read()
	fileName = link.get('alt') + '.jpg'
	filePath = os.path.join('./tu',fileName)
	image = open(filePath,'wb')
	image.write(data)
	image.close()


#htmlDoc = urllib.request.urlopen(pageUrl).read()
#soup = BeautifulSoup(htmlDoc)
#print (soup.prettify())
#print ("正在下载第(%d)"%(i))

'''


imgUrl = divHtml[0].img.attrs['src']
data = urllib.request.urlopen(imgUrl).read()
fileName = soup.title.contents[0] + '.jpg'
filePath = os.path.join('./tu',fileName)
image = open(filePath,'wb')
image.write(data)
image.close()
'''



