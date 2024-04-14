def encode(password):
    encoded_password = '' # Empty string for new password
    for i in password:
        i = int(i)
        i += 3 # Shifts each digit by 3
        i = str(i)
        encoded_password += i
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for char in encoded_password:
        decoded_char = chr(ord(char)-3)
        decoded_password += decoded_char
    return decoded_password


