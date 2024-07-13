import smtplib
import datetime as dt
import random

my_email = 'pyemailtest2024@gmail.com'
password = 'hleqwicuhbqublcx'#You get this from app passwords in gmail. Hard to find, helps to have error code to take you to page.

now = dt.datetime.now()
# date_of_birth = dt.datetime(year= 1999, month=1 , day=15)
day_of_week = now.weekday()
if day_of_week == 3:
    with open('quotes.text', mode='r') as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)
    with smtplib.SMTP(
            'smtp.gmail.com') as connection:  # different for every email provider. This closes it every time
        connection.starttls()  # encrypts the email and makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, to_addrs='hflinders101@gmail.com',
            msg=f'Subject:Motivation Sunday\n\n '
                f'{quote}')
