# 在 Django 的官方文档中，有以下例子：

from django.core.mail import send_mail

send_mail('Subject here', 'Here is the message.', 'from@example.com', ['to@example.com'], fail_silently=False)
# 由此代码中我们可以知道，在每次 send_mail 的时候都会建立一个链接，如果发送多封邮件则会建立多个邮件。所以一次性发送多封邮件时 send_mass_mail 要优于 send_mail。

# 为了使用以上功能，我们需要在 settings.py 中对其功能进行配置：

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = False
EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = '1111111@qq.com'
EMAIL_HOST_PASSWORD = 'xxxx'
DEFAULT_FROM_EMAIL = '1111111@qq.com'



# 使用 smtplib 进行邮件发送的示例代码：
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

receiver = '11111@qq.com'    # 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="11111@qq.com"#用户名
mail_pass=""   #口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格
sender = mail_user
receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header(mail_user, 'utf-8')
message['To'] =  Header(str(receivers), 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')

try:
   smtpObj = smtplib.SMTP_SSL(mail_host, 465)
   smtpObj.login(mail_user,mail_pass)
   smtpObj.sendmail(sender, receivers, message.as_string())
   smtpObj.quit()
   print ("邮件发送成功")
except smtplib.SMTPException as e:
   print (e)