# Import necessary library
import random

# Function to generate a random OTP
def generate_otp():
    otp_length = 6  # Length of the OTP
    otp = ''.join([str(random.randint(0, 9)) for _ in range(otp_length)])  # Generate a random OTP with the specified length
    return otp