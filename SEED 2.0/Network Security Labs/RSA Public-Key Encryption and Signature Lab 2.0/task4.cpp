#include <iostream>
#include <openssl/bn.h>
using namespace std;

void signMessage() {
    BIGNUM *d = BN_new();

    // Hexadecimal value of d (private key)
    BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");

    // Original message
    string M_original_hex = "49206f776520796f752024323030302e";  // Hexadecimal of "I owe you $2000."
    BIGNUM *M_original_hash = BN_new();
    BN_hex2bn(&M_original_hash, M_original_hex.c_str());

    // Sign the original message (S_original = M^d mod n)
    BIGNUM *S_original = BN_new();
    BN_mod_exp(S_original, M_original_hash, d, NULL, NULL);

    // Print the original signature
    char *S_original_hex = BN_bn2hex(S_original);
    cout << "Signature for the original message: " << S_original_hex << endl;

    // Clean up
    OPENSSL_free(S_original_hex);
    BN_free(d);
    BN_free(M_original_hash);
    BN_free(S_original);
}

int main() {
    signMessage();
    return 0;
}
