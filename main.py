##################### Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "birthdayman32@outlook.com"
MY_PASSWORD = "!@#QWE123"
PLACEHOLDER = "[NAME]"

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
now = dt.datetime.now()
today_month = now.month
today_day = now.day

birthday = pandas.read_csv("birthdays.csv")
# print(birthday)
birthday_dict = {(row.month, row.day): index for (index, row) in birthday.iterrows()}
# print(birthday_dict)


#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
if (today_month, today_day) in birthday_dict:
    birthday_person_row = birthday_dict[(today_month, today_day)]
    rand_num = random.randint(1, 3)
    letter_content = []

    with open(f"letter_templates/letter_{rand_num}.txt") as text:
        wish_letter = text.readlines()
    birthday_letter = wish_letter
    birthday_letter[0] = birthday_letter[0].replace(PLACEHOLDER, f"{birthday['name'][birthday_person_row]}")
    birthday_letter = ''.join(birthday_letter)
    # print(birthday_letter)


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    birthday_person_email = birthday['email'][birthday_person_row]
    # print(birthday_person_email)
    with smtplib.SMTP("smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person_email,
                            msg=f"Subject:Happy Birthday!!!\n\n{birthday_letter}")



