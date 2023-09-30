from Crypto.PublicKey import RSA

def calculate_private_key():
    p = int("F7E75FDC469067FFDC4E847C51F452DF", 16)
    q = int("E85CED54AF57E53E092113E62F436F4F", 16)
    e = int("0D88C3", 16)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Calculate private key (d)
    d = pow(e, -1, phi_n)

    print("Private key (d):", hex(d))

if __name__ == "__main__":
    calculate_private_key()
