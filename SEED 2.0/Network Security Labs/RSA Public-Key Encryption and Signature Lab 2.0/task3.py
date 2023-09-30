from Crypto.PublicKey import RSA

def decrypt_message():
    n = int("DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5", 16)
    d = int("74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D", 16)

    # Encrypted message (C)
    cipher = int("8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F", 16)

    # Decrypt the message
    decrypted_message = pow(cipher, d, n)
    decrypted_message_bytes = decrypted_message.to_bytes((decrypted_message.bit_length() + 7) // 8, byteorder='big')

    print("Decrypted message:", decrypted_message_bytes.decode('utf-8'))

if __name__ == "__main__":
    decrypt_message()
