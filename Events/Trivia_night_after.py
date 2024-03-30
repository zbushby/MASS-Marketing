import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

import csv
import time

EMAIL_ADDRESS = "monashactuary.president@gmail.com"
EMAIL_PASSWORD = ""
CSV_FILE_PATH = "//Users//zachbushby//Documents//edu//MASS//Data//Trivia Night//eventbrite.csv"

# Read recipient names and email addresses from the CSV file
NAMES = []
RECIPIENT_ADDRESSES = []

with open(CSV_FILE_PATH, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Assuming 'First name' and 'Email address' are the headers for recipient names
        name = f"{row['First Name']}"
        email = row['Email']
        NAMES.append(name)
        RECIPIENT_ADDRESSES.append(email)

# Compose and send emails
for name, recipient_address in zip(NAMES, RECIPIENT_ADDRESSES):
    time.sleep(2)
    msg = MIMEMultipart()
    # Custom signature with HTML formatting


    # Email content
    html_content = f"""
<p>Hey {name},</p>

<p>Thank you so much for coming to Trivia Night! We hope you enjoyed it as much as we did!</p>

<p> If you're interested in more events we have <strong>Q&A Panel (FREE!) in Week 6 and our Corporate Cocktail in Week 7!!!</strong> Have a look at the details on our socials below:</p>

<ul>
  <li><a href="https://www.instagram.com/monashactuary/" style="color: #00008B;">Instagram</a></li>
  <li><a href="https://www.facebook.com/monashactuary" style="color: #00008B;">Facebook</a></li>
  <li><a href="https://linktr.ee/monashactuary" style="color: #00008B;">MASS Linktree</a></li>
</ul>


<p>In the mean time have a look at some of the photos we took during the night:</p>
<li><a href="https://drive.google.com/drive/folders/1YoEfkXo-PbFmBSQZGVgUJN_NUtB5pazA?usp=sharing" style="color: #00008B; font-size:20px;">Trivia Night Photos</a></li>

<p>Enjoy the mid-sem break, We look forward to seeing you at our upcoming events! :)</p>


<div style="font-family: Arial, sans-serif; color: #00008B; font-style: italic; font-weight: bold;">
    <p style="color: navy;">Zach</p>
    <p style="color: black;"><strong>Monash Actuarial Students Society</strong></p>
    <p style="color: black;">Campus Centre 21 Chancellors Walk<br>
    Monash University, VIC 3800</p>
    <p style="color: black;"><a href="http://monashactuary.com.au" style="color: #00008B;">monashactuary.com.au</a></p>
    <img src="cid:logo" alt="MASS Logo" style="width: 100px; height: auto;">
</div>
    """

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Attach logo image
    with open("//Users//zachbushby//Documents//edu//MASS//Data//Welcome New Members//Data//MASS.png", "rb") as logo_file:
        logo = logo_file.read()
    logo_part = MIMEImage(logo)
    logo_part.add_header('Content-ID', '<logo>')
    msg.attach(logo_part)

    # Set the email subject, sender, and recipient
    msg['Subject'] = f"Hey {name}! Trivia Night Photos are here!📷"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_address

    # Send the message via SMTP server.
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, recipient_address, msg.as_string())
        print(f"Email sent for {name} with {recipient_address}")
