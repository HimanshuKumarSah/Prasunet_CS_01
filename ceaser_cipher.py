# Encryption Function
# Iterate through each character in the message and encrypt it using its ASCII value and the shift value.
def encryption():
    print("Encrypted Message is: \n")
    for a in message.lower():
        if a == ' ':
            print(' ', end='')
        else:
            x = ord(a) #converting the letter to ASCII Value
            y = x + shift #adding the key value to the letter
            z = chr(y) #converting the new ASCII value to a letter
            print(z, end='') #printing the Encrypted Message
    print()

# Decryption Function
# Iterate through each character in the message and decrypt it using its ASCII value and the shift value.
def decryption():
    print("Decrypted Message is: \n")
    for a in message.lower():
        if a == ' ':
            print(' ', end='')
        else:
            x = ord(a) #converting the letter to ASCII Value
            y = x - shift #subtracting the key value from the letter
            z = chr(y) #converting the new ASCII value to a letter
            print(z, end='') #printing the Decrypted Message
    print()


#Taking the message as input
message = input("Enter your text to be encrypted/decrpyted: ")
#Taking the key value as input
shift = input("Enter your key value here: ")
#Converting the key value to integer
shift = int(shift)

#Asking user for encryption or decryption of the message.
func = input("Enter 'e' to Encrypt or 'd' to Decrypt: ")
if func == 'e':
    encryption()
elif func == 'd':
    decryption()
