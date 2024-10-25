import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentialss
class EmailCredentials:
    def __init__(self, smtp_server, smtp_port, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.sender_password = sender_password

# Email notifications
class EmailNotifier:
    def __init__(self, credentials, recipient_emails):
        self.credentials = credentials
        self.recipient_emails = recipient_emails  # List of recipient emails

    def send_email(self, subject, message):
        try:
            # Setup the SMTP server
            with smtplib.SMTP(self.credentials.smtp_server, self.credentials.smtp_port) as server:
                server.starttls()
                server.login(self.credentials.sender_email, self.credentials.sender_password)

                # Send email to each recipient in the list
                for recipient_email in self.recipient_emails:
                    # Create a MIMEText object for the message
                    msg = MIMEMultipart()
                    msg['From'] = self.credentials.sender_email
                    msg['To'] = recipient_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    # Send the email
                    server.sendmail(self.credentials.sender_email, recipient_email, msg.as_string())
                    print(f"Email sent to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email: {e}")

# Class to check URLs and return status
class UrlChecker:
    def __init__(self, urls):
        self.urls = urls

    def check_urls(self):
        failed_urls = []
        for url in self.urls:
            try:
                response = requests.get(url)
                if response.status_code != 200:
                    failed_urls.append((url, response.status_code))
            except Exception as e:
                failed_urls.append((url, str(e)))
        return failed_urls

# Function to orchestrate the process
def main():
    # Email credentials
    email_credentials = EmailCredentials(
        smtp_server='smtp.gmail.com',  # Example: Gmail SMTP server
        smtp_port=587,
        sender_email='wije2582@gmail.com',
        sender_password='uadd ghll rcjd nyco'  # App password
    )
    
    # Receiver emails
    recipient_emails = ['ravinda.esol@gmail.com', 'wijethilakesavindu@gmail.com']  # Add emails
    
    # Email notifier
    email_notifier = EmailNotifier(email_credentials, recipient_emails)

    # List of URLs to check
    urls = [
        'https://backend.hcmsmiles.lk/login',
        'https://hcmsmiles.lk/login',
        'https://backend.mysoftlogic.lk/backend/login',
        'https://baaackend.hcmsmiles.lk/login',
        'https://mysoftlogic.lk/',
        'https://glomark.lk/',
        'https://odel.lk/home',
        'https://backend.kandos.lk/backend/login',
        'https://kandos.lk/',
        'https://tyreshoponline.lk/backend/login',
        'https://tyreshoponline.lk/',
        'https://burgerking.lk/',
        'https://crystaljade.lk/',
        'https://popeyes.com.lk/',
        'https://fleetmgt.slt.lk/',
        'https://routeradar.trackfleet.online/',
    ]
    
    # URL checker
    url_checker = UrlChecker(urls)
    
    # Check URLs
    failed_urls = url_checker.check_urls()
    
    # If any URLs failed, send an email
    if failed_urls:
        message = "\n".join([f"URL: {url} returned status: {status}" for url, status in failed_urls])
        email_notifier.send_email("Website Check Failed", message)
    else:
        print("All URLs returned 200.")

# Run the main function
if __name__ == "__main__":
    main()
    
    
