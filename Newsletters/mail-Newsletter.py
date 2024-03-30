import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import time

EMAIL_ADDRESS = "monashactuary.president@gmail.com"
EMAIL_PASSWORD = ""
CSV_FILE_PATH = "/Users/zachbushby/Documents/edu/MASS/Data/Newsletter/Data/Week 5.csv"
NEWSLETTER_PATH = "/Users/zachbushby/Documents/edu/MASS/Data/Newsletter/week_5_new_members_newsletter.html"

# Read recipient names, email addresses, and tickets from the CSV file
NAMES = []
RECIPIENT_ADDRESSES = []
TICKETS = []

with open(CSV_FILE_PATH, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        NAMES.append(f"{row['First.name']}")
        RECIPIENT_ADDRESSES.append(row['Email.address'])
        TICKETS.append(row['Tickets'])

# Load the HTML template once, outside the loop
with open(NEWSLETTER_PATH, "r") as template_file:
    html_template = template_file.read()

# Compose and send emails
#for name, recipient_address, tickets in zip(NAMES, RECIPIENT_ADDRESSES, TICKETS):
for name, recipient_address, tickets in zip(NAMES, RECIPIENT_ADDRESSES, TICKETS):

    msg = MIMEMultipart()

    time.sleep(3)
    # Replace the {{Tickets}} placeholder with the actual tickets
    html_content = html_template.replace("{{tickets}}", str(tickets))

    # Attach HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Set the email subject, sender, and recipient
    msg['Subject'] = f"Yo {name}! We've been cooking... "
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient_address

    # Send the message via SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, recipient_address, msg.as_string())
        #print(f"Email sent to {name} ({recipient_address}) with {tickets} tickets.")
        print(f"Email sent to {name} ({recipient_address})")

