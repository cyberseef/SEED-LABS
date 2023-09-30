#include <iostream>
#include <openssl/bn.h>
using namespace std;

void encryptMessage() {
    BIGNUM *n = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *M = BN_new();
    BIGNUM *C = BN_new();

    // Hexadecimal values
    BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
    BN_hex2bn(&e, "010001");
    BN_hex2bn(&M, "4120746f702073656372657421");

    // Encrypt the message (C = M^e mod n)
    BN_mod_exp(C, M, e, n, NULL);

    // Print the encrypted message (C)
    char *C_hex = BN_bn2hex(C);
    cout << "Encrypted message (C): " << C_hex << endl;

    // Clean up
    OPENSSL_free(C_hex);
    BN_free(n);
    BN_free(e);
    BN_free(M);
    BN_free(C);
}

int main() {
    encryptMessage();
    return 0;
}
