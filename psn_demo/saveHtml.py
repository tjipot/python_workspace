import urllib2
import cookielib
import pdfkit

cj = cookielib.LWPCookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
url = "https://www.taobao.com/"
req = urllib2.Request(url)
''' 保存html到本地'''
operate = opener.open(req)
msg = operate.read()
document = '/users/haoranye/desktop/1.html'  
file_ = open(document,'w')   
file_.write(msg)
file_.close()

path_wk = r'C:\Python27\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf = path_wk)

'''保存pdf到本地'''
pdfkit.from_url(url, r'D:\are you coding\pdf\taobao.pdf', configuration=config)
