# email_content.py

password_reset_subject = "Password Reset Request for Your [AppName] Account"

password_reset_body = """
Hello,

We received a request to reset the password for your [AppName] account associated with this email address. If you didn't request a password reset, you can ignore this email.

To reset your password, please use the following One-Time Password (OTP) to confirm your identity:

OTP: {otp}

This OTP is valid for 15 minutes. If you need a new OTP, please request a password reset again.

Once you've entered the OTP, you will be prompted to set a new password for your account.

If you have any questions or need assistance, please contact our support team at support@[AppName].com.

Thank you,
The [AppName] Team
"""
