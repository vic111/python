#在一个网页进行二级下载图片#
import os,re,codecs,urllib
from urllib import request
from bs4 import BeautifulSoup
pageUrl='http://miyamo-ura.ml/'
req=request.Request(pageUrl)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
htmlDoc = urllib.request.urlopen(pageUrl).read()
soup = BeautifulSoup(htmlDoc)
print ('正在下载')
divHtml = soup.find_all("div",class_="show_room")
for link in divHtml:
	inurl='http://miyamo-ura.ml'+link.a.attrs['href']
	htmlDoc1 = urllib.request.urlopen(inurl).read()
	souptwo = BeautifulSoup(htmlDoc1)
	imgHtml = souptwo.find_all("div",class_="imageContainer")
	print ('正在保存')
	#i=1
	path='/home/vic111/python/benzi/'+souptwo.title.string	
	if not os.path.exists(path):
		os.makedirs(path)
	for imglink in imgHtml:
		print (imglink.img.attrs['alt'])				
		data = urllib.request.urlopen(pageUrl+imglink.img.attrs['src']).read()
		fileName = souptwo.title.string+imglink.img.attrs['alt']
		#i=i+1
		filePath = os.path.join('./benzi',fileName)
		image = open(filePath,'wb')
		image.write(data)
		image.close()
