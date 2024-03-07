# Automatic Email Sender Script
This Python script is designed to send emails to multiple recipients using Gmail SMTP. It reads email addresses and names from a CSV file, composes an email for each recipient, and sends it.

## Prerequisites
Before using this script, ensure you have the following:

Python installed on your system.


Required Python libraries installed:


pandas
smtplib
email

## You can install the necessary libraries using pip:
pip install pandas


## Configuration
CSV File: Prepare a CSV file containing the email addresses and names of recipients. Make sure to specify the path to this file in the script (data=pd.read_csv("abc.csv")).

Sender's Email: Enter your email address in the from_addr variable.

Sender's Email Password: Enter your email password in the password variable.

Email Content: Customize the email content inside the loop where the body variable is defined.

## Usage
Clone or download this repository to your local machine.
Navigate to the directory containing the script.
Ensure your CSV file is correctly formatted with email addresses and names.
Open the script and configure the variables mentioned in the Configuration section.

## Run the script using the following command:

python mail.py


## Note
This script uses Gmail SMTP to send emails. Make sure to allow less secure apps to access your Gmail account. You can do this in your Gmail account settings.
