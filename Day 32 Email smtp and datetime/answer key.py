from datetime import datetime
import pandas as pd
import random
import smtplib


my_email = 'pyemailtest2024@gmail.com'
password = #You get this from app passwords in gmail. Hard to find, helps to have error code to take you to page.

today = datetime.now()
today_tuple = (today.month,today.day)
data = pd.read_csv('birthdays.csv')

# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])

    to_send_to = birthday_person['email']
    with smtplib.SMTP('smtp.gmail.com') as connection:  # different for every email provider. This closes it every time
        connection.starttls()  # encrypts the email and makes connection secure
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_send_to,
            msg=f'Subject:Happy Birthday\n\n{contents}')




