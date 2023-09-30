# Public key values
n = int("DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5", 16)
e = int("010001", 16)

# Message to encrypt
message = "A top secret!"

# Convert the message to hex and then to an integer
message_hex = int(message.encode("utf-8").hex(), 16)

# Encrypt the message
encrypted_message = pow(message_hex, e, n)

print("Encrypted message (C):", hex(encrypted_message))
