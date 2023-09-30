#include <iostream>
#include <openssl/bn.h>
using namespace std;

void decryptMessage() {
    BIGNUM *n = BN_new();
    BIGNUM *d = BN_new();
    BIGNUM *C = BN_new();
    BIGNUM *decrypted_M = BN_new();

    // Hexadecimal values
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
    BN_hex2bn(&C, "8C0F971DF2F3672B28811407E2DABBE1DA0FEBBBDFC7DCB67396567EA1E2493F");

    // Decrypt the message (decrypted_M = C^d mod n)
    BN_mod_exp(decrypted_M, C, d, n, NULL);

    // Convert decrypted message to plain ASCII string
    char *decrypted_M_hex = BN_bn2hex(decrypted_M);
    string decrypted_M_str(decrypted_M_hex);
    string decrypted_M_ascii;
    for (size_t i = 0; i < decrypted_M_str.length(); i += 2) {
        string byte = decrypted_M_str.substr(i, 2);
        char chr = (char)stoi(byte, nullptr, 16);
        decrypted_M_ascii += chr;
    }

    // Print the decrypted message
    cout << "Decrypted message: " << decrypted_M_ascii << endl;

    // Clean up
    OPENSSL_free(decrypted_M_hex);
    BN_free(n);
    BN_free(d);
    BN_free(C);
    BN_free(decrypted_M);
}

int main() {
    decryptMessage();
    return 0;
}
