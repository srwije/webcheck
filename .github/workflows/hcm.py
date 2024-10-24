import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_website_status(url):
    try:
        response = requests.get(url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def send_email(to_email, subject, body):
    # Your email credentials
    from_email = "wije2582@gmail.com"
    from_password = "uadd ghll rcjd nyco"  # Use an app password from your Google account
    
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Set up the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        
        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

if __name__ == "__main__":
    url = "https://backend.hcmsmiles.lk/login"
    status = check_website_status(url)

    if status == 200:
        subject = "Website Status: Success"
        body = f"The site {url} is up and returned status code 200."
    else:
        subject = "Website Status: Failure"
        body = f"The site {url} returned a status code: {status}."

    # Send email to notify the result
    send_email("ravinda.esol@gmail.com", subject, body)



