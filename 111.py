#encoding:UTF-8
import urllib.request
import os
from bs4 import BeautifulSoup
 
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
soup = BeautifulSoup(data)
print(soup.get_text())
filepath = os.path.join('page_'+soup.get_text())

