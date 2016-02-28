#在一个网页进行二级下载图片#
#添加翻页功能#
import os,re,codecs,urllib
from urllib import request
from bs4 import BeautifulSoup

Url='https://www.zhihu.com/collection/61913303?page='
for t in range(1,2):#抓取的页数范围
	pageUrl=Url+str(t)
	req=request.Request(pageUrl)
	req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/44.0.2403.157 UBrowser/5.5.9703.2 Safari/537.36')
	htmlDoc = urllib.request.urlopen(pageUrl).read()#访问收藏
	soup = BeautifulSoup(htmlDoc)
	print ('正在下载')
	divHtml = soup.find_all("h2",class_="zm-item-title")#收藏中抓取问题的网址
	for link in divHtml:
		print (link)
		try:
			print ('开始下载')
			inurl='https://www.zhihu.com'+link.a['href']
		except:
			print ('报错')
		else:
			htmlDoc1 = urllib.request.urlopen(inurl).read()#访问问题
			souptwo = BeautifulSoup(htmlDoc1)
			imgHtml = souptwo.find_all("img")#抓取图片的网址
			print ('正在保存')
			i=1	
			#创建目录
			path='/home/vic111/python/zhihu/'+souptwo.title.string
			#dirname = os.path.dirname(path.strip())
			#if not os.path.exists(dirname):
			#	os.makedirs(dirname)
			if not os.path.exists(path):
				os.makedirs(path)
			for imglink in imgHtml:
				#print (imglink.img.attrs['alt']+str(i))
				print ('一个图片')
				print (imglink.attrs['src'])
				try:				
					data = urllib.request.urlopen(imglink.attrs['src']).read()#访问图片
				except:
					print ('报错')
				else:
					fileName = str(i) + '.jpg'
					i=i+1
					filePath = os.path.join(path,fileName)
					image = open(filePath,'wb')
					image.write(data)
					image.close()
			


