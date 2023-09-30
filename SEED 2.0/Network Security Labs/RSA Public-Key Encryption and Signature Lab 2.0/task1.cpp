#include <iostream>
#include <openssl/bn.h>
using namespace std;

void calculatePrivateKey() {
    BIGNUM *p = BN_new();
    BIGNUM *q = BN_new();
    BIGNUM *e = BN_new();
    BIGNUM *phi_n = BN_new();
    BIGNUM *d = BN_new();

    // Hexadecimal values
    BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
    BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
    BN_hex2bn(&e, "0D88C3");

    // Calculate phi(n)
    BN_sub(phi_n, p, BN_value_one());
    BN_sub(phi_n, phi_n, q);
    BN_add(phi_n, phi_n, BN_value_one());

    // Calculate d (private key)
    BN_mod_inverse(d, e, phi_n, NULL);

    // Print the private key (d)
    char *d_hex = BN_bn2hex(d);
    cout << "Private key (d): " << d_hex << endl;

    // Clean up
    OPENSSL_free(d_hex);
    BN_free(p);
    BN_free(q);
    BN_free(e);
    BN_free(phi_n);
    BN_free(d);
}

int main() {
    calculatePrivateKey();
    return 0;
}
