#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Version 2: 文本邮件, 有主题, 有发件人和收件人;
# 一定要在命令行中运行才不会报错, 奇怪, @20170925;
#  而且, 要自己邮箱发给自己, 要不然, 会被网易当做垃圾邮件.., 绝了, 大千世界;
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText    # email是内置模块;
# from email.utils import parseaddr, formataddr
# import smtplib
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr   = input('From: ')
# password    = input("Password: ")
# to_addr     = input("To: ")
# smtp_server = input("SMTP Server: ")    # smtp.163.com
#
# msg = MIMEText('Hello, send by Python...', 'plain', 'utf-8')
# msg['From']     = _format_addr('Python Lover <%s>' % from_addr)
# msg['To']       = _format_addr('管理员 <%s>' % to_addr)
# msg['Subject']  = Header('来自SMTP的问候...', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25;
# server.set_debuglevel(1)                # 这个debug level可以打印出程序和SMTP服务器交互的所有信息;
# server.login(from_addr, password)       # 登录邮箱账号;
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()

# Version 3: HTML邮件;
# from email import encoders
# from email.header import Header
# from email.mime.text import MIMEText    # email是内置模块, 负责包装email;
# from email.utils import parseaddr, formataddr
# import smtplib                          # smtplib模块负责发送email;
#
# def _format_addr(s):
#     name, addr = parseaddr(s)
#     return formataddr((Header(name, 'utf-8').encode(), addr))
#
# from_addr   = input('From: ')
# password    = input("Password: ")
# to_addr     = input("To: ")
# smtp_server = input("SMTP Server: ")    # smtp.163.com
#
# # 此处设置MIMEText的类型为'html';
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#                '<p>send by <a href="https://www.python.org">Python</a>...</p>' +
#                '</body></html>', 'html', 'utf-8')    # From, To, Subject等都得包装到此类型的对象中;
# msg['From']     = _format_addr('Python Lover HY <%s>' % from_addr)
# msg['To']       = _format_addr('Administrator HY <%s>' % to_addr)
# msg['Subject']  = Header('来自SMTP的问候...', 'utf-8').encode()
#
# server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25;
# server.set_debuglevel(1)                # 这个debug level可以打印出程序和SMTP服务器交互的所有信息;
# server.login(from_addr, password)       # 登录邮箱账号;
# server.sendmail(from_addr, [to_addr], msg.as_string())
# server.quit()


# Version 4: 带附件的邮件;
from email import encoders
from email.mime.multipart import MIMEMultipart  # 卧槽, 这原来是这样的导入:
# [https://stackoverflow.com/questions/5821755/importerror-no-module-named-mime-multipart];
from email.mime.base import MIMEBase            # 卧槽, 这也是这样导入, PyCharm的导入提示有问题!;
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import smtplib                          # smtplib模块负责发送email;

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr   = input('From: ')
password    = input("Password: ")
to_addr     = input("To: ")
smtp_server = input("SMTP Server: ")    # smtp.163.com

# 告诉解释器这个邮件对象为"MIMEMultipart()"的, 可带附件;
msg             = MIMEMultipart()
msg['From']     = _format_addr('Python Lover HY <%s>' % from_addr)
msg['To']       = _format_addr('Administrator HY <%s>' % to_addr)
msg['Subject']  = Header('来自SMTP的问候...', 'utf-8').encode()

# 邮件正文是MIMEText:
msg.attach(MIMEText('Send with file...', 'plain', 'utf-8'))

# 添加附件, 就是加上一个'MIMEBase'对象, 此处从本地读取一个图片:
with open('/Users/univesre/desktop/dock_pic.png', 'rb') as f:
    # 设置附件的MIME和文件名, 这里是png类型;
    mime = MIMEBase('image', 'png', filename='dock_pic.png')
    # 加上一些必要的头信息;
    mime.add_header('Content-Disposition', 'attachment', filename='dock_pic.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件内容读进来;
    mime.set_payload(f.read())
    # 用Base64编码;
    encoders.encode_base64(mime)
    # mime添加到msg(MIMEMultipart)中;
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25;
server.set_debuglevel(1)                # 这个debug level可以打印出程序和SMTP服务器交互的所有信息;
server.login(from_addr, password)       # 登录邮箱账号;
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()






