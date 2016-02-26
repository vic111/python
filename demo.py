from bs4 import BeautifulSoup
import os,urllib.request
pageUrl = 'http://www.76xh.com/tupian/1111.html'
htmlDoc = urllib.request.urlopen(pageUrl).read()
soup = BeautifulSoup(htmlDoc)
#print (soup.prettify())
#print ("正在下载第(%d)"%(i))
divHtml = soup.find_all("div",class_="pic_text")
imgUrl = 'http://www.76xh.com' + divHtml[0].img.attrs['src']
data = urllib.request.urlopen(imgUrl).read()
fileName = soup.title.contents[0] + '.jpg'
filePath = os.path.join('./tu',fileName)
image = open(filePath,'wb')
image.write(data)
image.close()
