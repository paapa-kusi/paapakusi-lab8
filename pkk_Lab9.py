def encode(password):
    encoded_password = ''
    for i in password:
        i = int(i)
        i += 3
        i = str(i)
        encoded_password += i
    return encoded_password

