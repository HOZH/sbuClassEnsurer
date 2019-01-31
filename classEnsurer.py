from bs4 import BeautifulSoup as bs
import urllib.request
import email.mime.text
import smtplib
import time

smtplib.SMTP_SSL(host='smtp.gmail.com').connect(host='smtp.gmail.com', port=465)

# hard code your gmail address here (not your school email due to the complexity of cracking their netId system)
mail_username = 'putyourgmailhere'
mail_password = 'passwordhere'  # hard code you passwd here
from_addr = mail_username
to_addrs = ['somethingemailshere']  # could be send to multiple targets

smtp = smtplib.SMTP()

# show the debug log
smtp.set_debuglevel(1)

try:
    smtp = smtplib.SMTP('smtp.gmail.com')
    smtp.connect('smtp.gmail.com', '587')

except:
    print('CONNECT ERROR ****')

# gmail uses ssl
smtp.starttls()

try:
    print('loginning ...')
    smtp.login(mail_username, mail_password)
except:
    print('LOGIN ERROR ****')

while True:

    with open(
            'classes.txt') as data:  # leave this io procedure inside the loop so users can update their classes.txt file while this script is running
        classNums = (data.read())

    classNums = classNums.split('\n')

    result = ''
    key = 0  # key to determine whether the email should to send
    for clazz in classNums:
        currentUrl = "http://classfind.stonybrook.edu/vufind/Search/Results?lookfor=" + \
            clazz + "&type=AllFields&submit=Find&limit=10&sort=callnumber"
        req = urllib.request.Request(currentUrl)

        response = urllib.request.urlopen(req)

        soup = bs(response, features='html.parser')

        for sth in (soup.find_all(class_='span-2')):
            something = str(sth.select_one('b')).replace("<b>", '').replace("</b>", '')
            result = result + something + ' ' + clazz

        if len(soup.find_all(class_="itemLine1" + clazz + " status_waitlist")) == 1:
            key = 1

            result = result + ' is available\n'

        else:

            result = result + ' is closed\n'

    print(result)
    if key == 1:
        msg = email.mime.text.MIMEText(result)
        msg['From'] = from_addr
        msg['To'] = ';'.join(to_addrs)
        msg['Subject'] = 'from Hong\'s class ensurer'
        print(msg.as_string())
        smtp.sendmail(from_addr, to_addrs, msg.as_string())
        break

    time.sleep(300)
