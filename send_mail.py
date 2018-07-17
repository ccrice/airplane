# coding:utf8
# created at 2018/7/17.

from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


from_addr = 'sch_0221@163.com'
password = 'O84FbyUK'
to_addr = '337065098@qq.com'
cc_addr = '690420753@qq.com'
smtp_server = 'smtp.163.com'

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_mail(data_html):
    msg = MIMEText(data_html, 'html', 'utf-8')
    msg['From'] = _format_addr('发件人:<%s>' % from_addr)
    msg['To'] = _format_addr('<%s>' % to_addr)
    msg['Subject'] = Header('抢购机票了', 'utf-8').encode()
    msg['Cc'] = _format_addr('<%s>' % cc_addr)

    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr,cc_addr], msg.as_string())
    server.quit()