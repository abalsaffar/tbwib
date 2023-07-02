def password_reset(email):
    """
    Sends a password reset link to the user with the given email address.

    Args:
      email: The email address of the user to send the password reset link to.

    Returns:
      True if the password reset email was sent successfully, or False if the email does not exist or there's an error.
    """

    # Check if the email exists in the database.
    user = User.query.filter_by(email=email).first()
    if user is None:
        # Email does not exist, return False
        return False

    # Import the email content file.
    from email_content import password_reset_subject, password_reset_body

    # Generate a new OTP.
    otp = generate_otp()

    # Format the email body with the generated OTP.
    formatted_body = password_reset_body.format(otp=otp)

    # Send the OTP to the user's email.
    email_sent = send_email(email, otp, password_reset_subject, formatted_body)
    if not email_sent:
        # Email could not be sent, return False
        return False

    # Save the OTP in the database.
    user.password_reset_otp = otp
    try:
        db.session.commit()
        return True
    except Exception as e:
        # Handle any exceptions that might occur during the database operation.
        print(f"Error updating password reset OTP: {e}")
        db.session.rollback()
        return False
