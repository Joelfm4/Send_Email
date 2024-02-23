# Email Sending Script

This Python script facilitates sending emails using a recipient list from a CSV file. It utilizes various modules including `email.message`, `ssl`, `smtplib`, `os`, `csv`, `sys`, and `re`.

## Prerequisites

Ensure Python is installed on your system. Additionally, you need to install the `email-validator` module to validate email addresses. You can install the requirements using the following command:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, set up your Gmail email credentials. Create a file named `SETTINGS.py` in the same directory as the script and define the `EMAIL` and `PASSWORD` variables with your Gmail email address and password, respectively.

Example `SETTINGS.py`:

```python
EMAIL = 'your_email@gmail.com'
PASSWORD = 'your_password'
```

## Usage

1. Place the CSV file with the recipients in the same directory as the script.

2. Run the `main.py` script.

3. Follow the instructions provided by the script to input the name of the CSV file with the recipients.

4. The script will check if the file exists and if it has the `.csv` extension.

5. If the file is valid, the script will verify if the email addresses in the file are valid.

6. If all email addresses are valid, the script will send emails to the recipients listed in the CSV file.

## Notes

- **This script is designed to work specifically with Gmail accounts.**
- The content, subject, and body of the email are configured within the script itself.

- Make sure to allow access for less secure apps in your Gmail account settings if you're using a Google account to send emails. You can enable this option in the security settings of your account.

- This script is designed for educational and demonstration purposes. Use it responsibly and respect the acceptable use policies of email services.


[What will the recipient receive](test.png)
