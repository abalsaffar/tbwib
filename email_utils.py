# Import necessary library
import smtplib

# Function to send an email with the OTP
def send_email(email, otp):
    sender_email = "your_email@gmail.com"  # Replace with your Gmail email address
    sender_password = "your_password"  # Replace with your Gmail password

    # Set up the SMTP connection
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Start a TLS-encrypted connection
    server.login(sender_email, sender_password)  # Log in to the Gmail account

    # Compose the email message
    subject = "Your OTP for registration"  # Email subject
    body = f"Your OTP is: {otp}"  # Email body
    message = f"Subject: {subject}\n\n{body}"  # Combine the subject and body

    # Send the email
    try:
        server.sendmail(sender_email, email, message)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()  # Close the SMTP connection