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

if __name__ == '__main__':
    while True:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = input("Please enter an option: ")
        if option == "1":
            num = input("Please enter your password to encode: ")
            num = encode(num)
            num2 = num
            print("Your password has been encoded and stored!")
        if option == "2":
            num2 = decode(num2)
            print(f"The encoded password is {num}, and the original password is {num2}")
        if option == "3":
            break

