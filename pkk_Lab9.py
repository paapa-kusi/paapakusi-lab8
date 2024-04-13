def encode(password):
    encoded_password = '' # Empty string for new password
    for i in password:
        i = int(i)
        i += 3 # Shifts each digit by 3
        i = str(i)
        encoded_password += i
    return encoded_password


