import string
import numpy as np
import math as m
import random as r
import pywhatkit as whatsapp
# Variables Declaration


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
print(Ascii)


def function(value, choice):
    if choice == 0:
        if 0 <= value <= 20:
            return 94 - value
        if 21 <= value <= 40:
            return value + 33
        if 41 <= value <= 64:
            return 94 - value
        if 65 <= value <= 94:
            return value - 65
    elif choice == 1:
        if 0 <= value <= 20:
            return 94 - value
        if 21 <= value <= 40:
            return value + 33
        if 41 <= value <= 64:
            return value - 11
        if 65 <= value <= 94:
            return 94 - value
    elif choice == 2:
        if 0 <= value <= 20:
            return value
        if 21 <= value <= 40:
            return -value + 61
        if 41 <= value <= 64:
            return value
        if 65 <= value <= 94:
            return -value + 159
    else:
        if 0 <= value <= 20:
            return value
        if 21 <= value <= 40:
            return -value + 61
        if 41 <= value <= 64:
            return -value + 105
        if 65 <= value <= 94:
            return value

def function_inv(new_val, choice):
            if choice == 0:
                if 74 <= new_val <= 94:
                    return 94 - new_val
                if 54 <= new_val <= 73:
                    return new_val - 33
                if 30 <= new_val <= 53:
                    return 94 - new_val
                if 0 <= new_val <= 29:
                    return 65 + new_val
            elif choice == 1:
                if 74 <= new_val <= 94:
                    return 94 - new_val
                if 54 <= new_val <= 73:
                    return new_val - 33
                if 30 <= new_val <= 53:
                    return new_val + 11
                if 0 <= new_val <= 29:
                    return 94 - new_val
            elif choice == 2:
                if 0 <= new_val <= 20:
                    return new_val
                if 21 <= new_val <= 40:
                    return 61 - new_val
                if 41 <= new_val <= 64:
                    return new_val
                if 65 <= new_val <= 94:
                    return 159 - new_val
            else:
                if 0 <= new_val <= 20:
                    return new_val
                if 21 <= new_val <= 40:
                    return 61 - new_val
                if 41 <= new_val <= 64:
                    return 105 - new_val
                if 65 <= new_val <= 94:
                    return new_val

def Encryption(msg, N):
            msg_num = []
            encoded_msg_num = []
            encoded_msg = ""
            for i in msg:
                msg_num.append(Ascii[i])
                value = Ascii[i]
                choice_encrypt = r.randint(0, 3)
                new_value = function(value, choice_encrypt)
                encoded_msg_num.append(new_value)
                encoded_msg_num.append(choice_encrypt)
                for key, value in Ascii.items():
                    if new_value == value:
                        encoded_msg = encoded_msg + key
                for key, value in Ascii.items():
                    if value == choice_encrypt:
                        encoded_msg = encoded_msg + key
            for i in range(0, 2 * N):
                garbage = r.randint(0, len(Ascii) - 1)
                encoded_msg_num.append(garbage)
                for key, value in Ascii.items():
                    if garbage == value:
                        encoded_msg = encoded_msg + key
            encoded_msg_num.append(N)
            for key, value in Ascii.items():
                if value == N:
                    encoded_msg = encoded_msg + key

            return encoded_msg

def Decryption(encoded_msg):
            received_msg_num = []
            decrypt_msg_num = []
            decrypt_msg = ""
            for i in encoded_msg:
                received_msg_num.append(Ascii[i])
            last = len(encoded_msg) - 1
            received_msg_num.pop(last)
            last = last - 1
            N = received_msg_num[last]
            received_msg_num.pop(last)
            last = last - 1
            for i in range(0, 2 * N):
                received_msg_num.pop(last - i)
            L = len(received_msg_num)
            for i in range(0, int(L / 2)):
                new_value = received_msg_num[2 * i]
                choice_decrypt = received_msg_num[2 * i + 1]
                old_value = function_inv(new_value, choice_decrypt)
                decrypt_msg_num.append(old_value)
                for key, value in Ascii.items():
                    if old_value == value:
                        decrypt_msg = decrypt_msg + key
            return decrypt_msg

def hill_cipher_encryption(msg):
            gcd = 0
            det = 0
            msg_encoded = []
            cipher_encoded = []
            encrypt_data = []
            encrypt_data_alph = []
            final_encryption = ''
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
                if np.linalg.det(Key) == 0 or m.gcd((round(np.linalg.det(Key))) % len(Ascii_List),
                                                    len(Ascii_List)) != 1:
                    print("Invalid Cipher")
                    det = 0
                    gcd = 0
                    cipher_encoded = []
                else:
                    det = 1
                    gcd = 1
            print('Final Cipher is:\n' + str(cipher_encoded))
            # Multiply the Key (generated from cipher) with the symbols in message (taken 2 at a time)
            N1 = int(len(msg_encoded) / 2)
            for n in range(0, N1):
                t = list(msg_encoded[2 * n:2 * (n + 1)])
                t = np.array([[t[0]], [t[1]]])
                encryption = np.dot(Key, t).tolist()  # Matrix multiplication using numpy
                encrypt_data.append(encryption[0][0])
                encrypt_data.append(encryption[1][0])
            for i in range(0, len(encrypt_data)):
                encrypt_data[i] = encrypt_data[i] % len(Ascii_List)
                for key, value in Ascii.items():  # Encrypted data (in terms of number) is substituted with corresponding key
                    # value from dictionary
                    if encrypt_data[i] == value:
                        encrypt_data_alph.append(key)

            for i in range(0, len(encrypt_data_alph)):
                final_encryption = final_encryption + str(encrypt_data_alph[i])
            return final_encryption, cipher

        def mod_Inv(x, y):  # Function to calculate modular inverse
            for k in range(y):
                if (x * k) % y == 1:
                    break
            return k

def hill_cipher_decryption(final_encryption, cipher):
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
            Decryption_Key = np.array([cipher_decode[0:2], cipher_decode[2:4]])  # Creates a numpy array (2x2)
            Decryption_Key_det = round(np.linalg.det(Decryption_Key))  # Determinant of Key Matrix
            Decryption_Key_det_mod = round(np.linalg.det(Decryption_Key) % len(Ascii_List))
            Decryption_Key_det_inv = mod_Inv(Decryption_Key_det_mod,
                                             len(Ascii_List))  # Find modular inverse of determinant
            # (det)^(-1)
            Decryption_Key = np.linalg.inv(Decryption_Key)

            for i in range(0, 2):
                for j in range(0, 2):
                    Decryption_Key[i][j] = round(Decryption_Key[i][j] * Decryption_Key_det)
                    # Multiply Adjoint of Key Matrix with inverse determinant mod with 95 to give the corresponding
                    # decryption key
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
                        h = value

                        if h <= 0:
                            h = h % len(Ascii_List)
                        Decrypted_data[i] = h

                for key, value in Ascii.items():
                    if Decrypted_data[i] == value:
                        Decrypted_data_alph.append(key)

            # Decrypted Data
            for i in range(0, len(Decrypted_data_alph)):
                Decrypted_msg = Decrypted_msg + Decrypted_data_alph[i]
            return Decrypted_msg

    # Whatsapp part
num = "+91"
message = input("Enter a message")
Encryption_1 = Encryption(message, 94)
Encryption_2, cipher = hill_cipher_encryption(Encryption_1)
print("Encrypted data: " + Encryption_2)
whatsapp.sendwhatmsg_instantly(num, Encryption_2)
Decryption_1 = hill_cipher_decryption(Encryption_2, cipher)
Decryption_2 = Decryption(Decryption_1)
print("Decrypted Data is: " + Decryption_2)
whatsapp.sendwhatmsg_instantly(num, Decryption_2)