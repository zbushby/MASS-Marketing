import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage

import csv
import time

EMAIL_ADDRESS = "monashactuary.president@gmail.com"
EMAIL_PASSWORD = ""
CSV_FILE_PATH = "//Users//zachbushby//Documents//edu//MASS//Data//Welcome New Members//Data//Week 4.csv"

# Read recipient names and email addresses from the CSV file
NAMES = []
RECIPIENT_ADDRESSES = []

with open(CSV_FILE_PATH, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Assuming 'First name' and 'Last name' are the headers for recipient names
        name = f"{row['First name']}"
        email = row['Email address']
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

<p>I'm Zach, and I'm thrilled to extend a warm welcome to you as a new member of our community. I hope you are as excited as I am about your journey ahead with the Monash Actuarial Student Society in 2024!</p>

<p>As a member, you can expect to receive our weekly newsletter, packed with graduate & internship opportunities, updates of amazing upcoming events, and opportunities for friendship with your fellow actuarial peers in a non-academic setting. Be sure to keep an eye on your inbox for the latest edition!</p>

<p>To stay connected and up-to-date with all things Monash Actuary, please follow us on our social media:</p>

<ul>
  <li><a href="https://www.instagram.com/monashactuary/" style="color: #00008B;">Instagram</a></li>
  <li><a href="https://www.facebook.com/monashactuary" style="color: #00008B;">Facebook</a></li>
  <li><a href="https://www.linkedin.com/company/monashactuary/" style="color: #00008B;">Linkedin</a></li>
  <li><a href="http://monashactuary.com.au" style="color: #00008B;">Website</a></li>
  <li><a href="https://linktr.ee/monashactuary" style="color: #00008B;">MASS Linktree</a></li>
</ul>

<p>Additionally, here are some useful resources to help you navigate our events and activities:</p>

<ul>
  <li><a href="https://www.monashactuary.com.au/event-timeline" style="color: #00008B;">Event Timeline</a></li>
</ul>

<p>Please don't hesitate to reach out if you have any questions or need assistance. We're here to support you every step of the way!</p>

<p>Once again, welcome to the Monash Actuarial Student Society! We're thrilled to have you as part of our community and look forward to seeing you at our events!</p>

<div style="font-family: Arial, sans-serif; color: #00008B; font-style: italic; font-weight: bold;">
    <p style="color: navy;">Zach Bushby</p>
    <p style="color: black; font-style: italic;">President</p>
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
    msg['Subject'] = f"Hey {name}! Welcome to MASS!"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_address

    # Send the message via SMTP server.
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, recipient_address, msg.as_string())
        print(f"Email sent for {name} with {recipient_address}")
