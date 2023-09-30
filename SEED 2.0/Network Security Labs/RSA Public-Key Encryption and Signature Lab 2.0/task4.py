# Original message
M_original = "I owe you $2000."

# Provided private key (d) and public key (n)
d_hex = "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D"
n_hex = "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5"

d = int(d_hex, 16)
n = int(n_hex, 16)

# Sign the original message
M_original_hash = int(M_original.encode('utf-8').hex(), 16)
S_original = pow(M_original_hash, d, n)

# Print the original signature
print("Signature for the original message:", hex(S_original)[2:])

# Modify the message
M_modified = "I owe you $3000."

# Sign the modified message
M_modified_hash = int(M_modified.encode('utf-8').hex(), 16)
S_modified = pow(M_modified_hash, d, n)

# Print the modified signature
print("Signature for the modified message:", hex(S_modified)[2:])
