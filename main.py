import random
import datetime as dt
import smtplib
import pandas

dates = pandas.read_csv("birthdays.csv")
list_of_data = dates.to_dict(orient="records")
print(list_of_data)

day = dt.datetime.now().day
month = dt.datetime.now().month

letters_path = ["./letter_templates/letter_1.txt", "./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt"]
send_this = ""
my_email = "merab1223t@gmail.com"
password = "xhygcsvzayclrrnw"

for x in list_of_data:
    if day == x["day"] and month == x["month"]:
        with open(f"{random.choice(letters_path)}", "r") as letter:
            send_this = letter.read().replace("[NAME]", f"{x["name"]}")

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=x["email"], msg=f"Subject: Happy birthday\n\n{send_this}")





