
import string
import numpy as np
import math as m
# Variables Declaration
gcd = 0
det = 0
msg_encoded = []
cipher_encoded = []
encrypt_data = []
encrypt_data_alph = []
final_encryption = ''

# Creation of List containing all symbols, numbers and alphabets (big and small)
letter = list(string.ascii_letters)
num = list(string.digits)
char = list(string.punctuation)
space = [' ']
Ascii_List = letter + num + char + space

""" Creation of list containing numbers from 0 to 95, to create a dictionary
with key-value pair being symbol and following number """

Numbers = list(range(0, len(Ascii_List)))
Ascii = dict(zip(Ascii_List, Numbers))

# Encryption of data
msg = input("Enter the message ")
for i in msg:  # Replacing symbols of message with corresponding numbers
    msg_encoded.append(Ascii[i])
if len(msg_encoded) % 2 != 0:
    msg_encoded.append(Ascii[' '])  # Adding space if message elements is odd
print('Encoded message is: ' + str(msg_encoded))
# Entering cipher, and checking if cipher is valid, that is GCD = 1 and det(cipher) is not = 0
while det == 0 or gcd == 0:
    cipher = input("Enter a 4 worded cipher ")
    for i in cipher:
        cipher_encoded.append(Ascii[i])
    print('Encoded cipher is: ' + str(cipher_encoded))
    Key = np.array([cipher_encoded[0:2], cipher_encoded[2:4]])
    if np.linalg.det(Key) == 0 or m.gcd((round(np.linalg.det(Key))) % len(Ascii_List), len(Ascii_List)) != 1:
        print("Invalid Cipher")
        det = 0
        gcd = 0
        cipher_encoded = []
    else:
        det = 1
        gcd = 1
print('Final Cipher is:\n' + str(cipher_encoded))
# Multiply the Key (generated from cipher) with the symbols in message (taken 2 at a time)
N1 = int(len(msg_encoded)/2)
for n in range(0, N1):
    t = list(msg_encoded[2*n:2*(n+1)])
    t = np.array([[t[0]], [t[1]]])
    encryption = np.dot(Key,t).tolist()  # Matrix multiplication using numpy
    encrypt_data.append(encryption[0][0])
    encrypt_data.append(encryption[1][0])
for i in range(0,len(encrypt_data)):
    encrypt_data[i] = encrypt_data[i] % len(Ascii_List)
    for key,value in Ascii.items():  # Encrypted data (in terms of number) is substituted with corresponding key
        # value from dictionary
        if encrypt_data[i] == value:
            encrypt_data_alph.append(key)

for i in range(0,len(encrypt_data_alph)):
    final_encryption = final_encryption + str(encrypt_data_alph[i])
print('Encrypted Data is: ' + final_encryption)

# Decryption


def mod_Inv(x,y):   # Function to calculate modular inverse
    for k in range(y):
        if (x*k) % y == 1:
            break
    return k


# Printing the encrypted received message
print("The received data is: " + final_encryption)
received_data = list(final_encryption)
received_data_num = []
cipher_decode = []
Decrypted_data = []
Decrypted_data_alph = []
Decrypted_msg = ''
# Converting symbols of received data to their corresponding numbers based on key value from dictionary
for i in range(0, len(received_data)):
    received_data_num.append(Ascii[received_data[i]])
# Converting cipher symbols into corresponding numbers to create Key Matrix
for i in cipher:
    cipher_decode.append(Ascii[i])
# To find Decryption Key to decrypt the encrypted message
# ...

# To find Decryption Key to decrypt the encrypted message
Decryption_Key = np.array([cipher_decode[0:2], cipher_decode[2:4]])  # Creates a numpy array (2x2)
Decryption_Key_det = round(np.linalg.det(Decryption_Key))  # Determinant of Key Matrix
Decryption_Key_det_mod = round(np.linalg.det(Decryption_Key) % len(Ascii_List))
Decryption_Key_det_inv = mod_Inv(Decryption_Key_det_mod, len(Ascii_List))  # Find modular inverse of determinant
# (det)^(-1)
Decryption_Key = np.linalg.inv(Decryption_Key)

for i in range(2):
    for j in range(2):
        Decryption_Key[i][j] = round(Decryption_Key[i][j] * Decryption_Key_det)
        # Multiply Adjoint of Key Matrix with inverse determinant mod with 95 to give the corresponding decryption key
        Decryption_Key[i][j] = (Decryption_Key_det_inv * Decryption_Key[i][j]) % (len(Ascii_List))

# Multiply Decryption key with encrypted data (2 symbols at a time) to get the decrypted data
N2 = int(len(received_data) / 2)
for n in range(0, N2):
    z = list(received_data_num[2 * n:2 * (n + 1)])
    z = np.array([[z[0]], [z[1]]])
    decryption = np.dot(Decryption_Key, z).tolist()
    Decrypted_data.append(round(decryption[0][0]))
    Decrypted_data.append(round(decryption[1][0]))

# Mod each element of decrypted data with 95, and substitute the numbers with the corresponding key value
for i in range(0, len(Decrypted_data)):
    Decrypted_data[i] = Decrypted_data[i] % len(Ascii_List)
    for key, value in Ascii.items():
        if Decrypted_data[i] == value:

            Decrypted_data_alph.append(key)

# Decrypted Data
Decrypted_msg = ''.join(Decrypted_data_alph)
print("The Decrypted Message is: " + Decrypted_msg)
