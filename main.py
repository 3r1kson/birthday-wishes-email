##################### Extra Hard Starting Project ######################
import random
import smtplib
import pandas as pd
import datetime as dt

my_email = ""
password = ""
smtp_data = []
birthdays = []
smtp_data = []

# 1. Update the birthdays.csv
births = pd.read_csv('birthdays.csv').to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
def check_birth():
    for i in births:
        date = dt.datetime.now()
        if i['month'] == date.month and i['day'] == date.day:
            birthdays.append(i)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def choose_letter():
    select = random.randint(1, 3)
    with open(f"letter_templates/letter_{select}.txt", "r") as letter:
        return letter.read()

# 4. Send the letter generated in step 3 to that person's email address.
def send_wishes():
    if get_config():
        check_birth()
        for birthday in birthdays:
            letter = choose_letter()
            letter = letter.replace("[NAME]", birthday['name'])

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="eriksonribeiro@hotmail.com",
                    msg=f"Subject: Happy Birthday \n\n{letter}"
                )

def get_config():
    global my_email, password, smtp_data
    validation = False
    try:
        with open('../pythonEmail.txt') as python_file:
            smtp_data = [line.strip().split(' = ') for line in python_file]

        my_email = smtp_data[0][1].strip('"')
        password = smtp_data[1][1].strip('"')
        validation = True
    except FileNotFoundError:
        print("Error to load smtp data")

    return validation

send_wishes()


