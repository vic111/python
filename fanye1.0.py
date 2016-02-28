#在一个网页进行二级下载图片#
#添加翻页功能#
import os,re,codecs,urllib
from urllib import request
from bs4 import BeautifulSoup

Url='http://www.ivsky.com/tupian/index_'
for t in range(0,10):
	pageUrl=Url+str(t)+'.html'
	req=request.Request(pageUrl)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
	htmlDoc = urllib.request.urlopen(pageUrl).read()
	soup = BeautifulSoup(htmlDoc)
	print ('正在下载')
	divHtml = soup.find_all("div",class_="il_img")
	for link in divHtml:
		inurl='http://www.ivsky.com'+link.a.attrs['href']
		htmlDoc1 = urllib.request.urlopen(inurl).read()
		souptwo = BeautifulSoup(htmlDoc1)
		imgHtml = souptwo.find_all("div",class_="il_img")
		print ('正在保存')
		i=1	
		#创建目录
		path='/home/vic111/python/tu/'+souptwo.title.string
		#dirname = os.path.dirname(path.strip())
		#if not os.path.exists(dirname):
		#	os.makedirs(dirname)
		if not os.path.exists(path):
			os.makedirs(path)
		for imglink in imgHtml:
			print (imglink.img.attrs['alt']+str(i))				
			data = urllib.request.urlopen(imglink.img.attrs['src']).read()
			fileName = imglink.img.attrs['alt'] + str(i) + '.jpg'
			i=i+1
			filePath = os.path.join(path,fileName)
			image = open(filePath,'wb')
			image.write(data)
			image.close()
