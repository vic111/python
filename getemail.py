#发送一个网页#
import smtplib  
from email.mime.text import MIMEText  
_user = "ysxswh@126.com"  
_pwd  = "yaosen1238"  
_to   = "675317972@qq.com"  
_host = "smtp.126.com"
content = "<a href='http://miyamo-ura.ml'>嘿嘿嘿</a>"



#使用MIMEText构造符合smtp协议的header及body
#def star:
msg = MIMEText(content,_subtype='html',_charset='gb2312') #内容 
msg["Subject"] = "don't panic"  	#标题
msg["From"]    = _user  
msg["To"]      = _to
try:
	s = smtplib.SMTP(_host, timeout=25)#连接smtp邮件服务器,端口默认是25  
	s.login(_user, _pwd)#登陆服务器  
	s.sendmail(_user, _to, msg.as_string())#发送邮件  
	s.close()
	print ('发送成功')
	#return True  
except:
	print ('发送失败')
	#return False
'''		
if __name__ == '__main__':
	if star:
		print ("发送成功")
	else :
		print ('发送失败')
'''
