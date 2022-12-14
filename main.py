# ----------------------------Automated Birthday Wisher---------------------------------------------------- #
import pandas
import datetime as dt
import random
import smtplib

EMAIL = "@gmail.com"
PASSWORD = ""

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)


data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randrange(1,3)}.txt") as letter_templates:
        contents = letter_templates.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject: Happy Birthday\n\n{contents}."
                            )