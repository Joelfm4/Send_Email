from email.message import EmailMessage
import ssl  # to encrypt the email
import smtplib  # to send our email
import os
import csv
import sys
import re
from SETTINGS import EMAIL, PASSWORD


def main():

    path = os.path.dirname(__file__)

    files = os.listdir(path)

    print("-"*30)
    print("Files: ")

    for file in files:
        print(f"-> {file}")

    try:
        print("-"*30)
        data_file_name = input("File Name with Data: ")
        print("-"*30)

        if verify_file(data_file_name):

            with open(data_file_name, "r") as file:

                reader = csv.reader(file)
                next(reader)

                if verify_emails(data_file_name):
                    send_email(data_file_name)
    except EOFError:
        print("Have a nice day :)")


def verify_file(data_file_name):
    """
    This function checks if the given CSV file exists and if its extension is .csv.

    Args:
        data_file_name (str): The name of the CSV file to be verified.

    Returns:
        bool: A boolean value indicating whether the file exists and has the correct extension or not.

    Raises:
        Exception: If an error occurs while checking for the file.
    """
    try:
        if os.path.exists(data_file_name) and data_file_name.endswith(".csv"):
            return True

        else:
            print("File not found. Please check again.")
            print("Please ensure the file name ends with .csv")

            main()

    except Exception as error:
        print(f"Something went wrong in 'unction verify_file' -> {error}")


def verify_emails(data_file_name):
    """
    This function verifies the emails in the given CSV file.

    Args:
        data_file_name (str): The name of the CSV file containing the data.

    Returns:
        bool: A boolean value indicating whether the emails are valid or not.

    Raises:
        Exception: If an error occurs while reading the CSV file or validating the emails.
    """
    try:

        with open(data_file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                email = row[2].strip()

                if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email): # basic pattern for email validation
                    print(f"Invalid email address: {email}")
                    return False

    except Exception as error:
        print(f"Something went wrong in 'verify_emails' -> {error}")
        return False

    return True


def send_email(data_file_name):
    """
    This function sends an email to the recipients listed in the given CSV file.

    Args:
        data_file_name (str): The name of the CSV file containing the data.

    Raises:
        Exception: If an error occurs while reading the CSV file or sending the email.
    """
    try:
        with open(data_file_name, "r") as file:
            reader = csv.reader(file)
            next(reader)


            data = [row.strip().split(",") for row in file]

            first_name = [row[0] for row in data]
            last_name = [row[1] for row in data]
            email_address = [row[2] for row in data]


        for i in range(len(first_name)):
            email_sender = EMAIL
            email_password = PASSWORD
            email_receiver = email_address[i]
            subject = "TEST"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject

            body = f"""
            Subject: SUBJECT

            Dear {first_name[i]} {last_name[i]},

            Work!!!!

            Sincerely,
            YOUR NAME
            """

            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())

    except Exception as error:
        print(f"Something went wrong in 'send_email' -> {error}")


if __name__ == "__main__":

    main()



