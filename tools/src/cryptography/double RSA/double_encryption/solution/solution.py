import hashlib
from random import randint, random
import binascii

import binary_search


def int_to_bin(test_key):
    test_k = format(test_key, "b").zfill(key_length);
    print(test_k)
    test_k_as_list = [];
    for i in range(key_length):
        if test_k[i] == "0":
            test_k_as_list.append(0);
        else:
            test_k_as_list.append(1);

    return list_reverse(test_k_as_list);


##convert hex to bin
def hex_to_bin(hex_string, bin_length):
    bin_string = bin(int(hex_string, 16))[2:];
    return bin_string.zfill(bin_length)


# Generate 16 pseudo-random bits from the input x
# x must be in list format
def gen_key_stream(x):
    digest = hashlib.sha256(str(x).encode('utf-8')).hexdigest();
    binary_digest = hex_to_bin(digest, 256);
    return binary_digest[0:5];


# m is the plaintext, sk is the secret key
# both m and sk must be in list format
def encrypt(m, sk):
    c = [];
    x = sk.copy();
    d = gen_key_stream(x);
    for i in range(4):
        for j in range(5):
            y = m[i * 5 + j] ^ (ord(d[j]) - 48);
            c.append(y);
            x[(i * 5 + j) % key_length] = x[(i * 5 + j) % key_length] ^ m[i * 5 + j];
        d = gen_key_stream(x);

    return c;


def decrypt(c, sk):
    m = [];
    x = sk.copy();
    d = gen_key_stream(x);
    for i in range(4):
        for j in range(5):
            y = c[i * 5 + j] ^ (ord(d[j]) - 48);
            m.append(y);
            x[(i * 5 + j) % key_length] = x[(i * 5 + j) % key_length] ^ y;
        d = gen_key_stream(x);

    return m;


########################

def double_encryption(plaintext, sk1, sk2):
    ciphertext_1 = encrypt(plaintext, sk1);
    #   print(ciphertext_1);
    #  print(sk1)
    ciphertext_2 = encrypt(ciphertext_1, sk2);

    return ciphertext_2;


def double_decryption(ciphertext, sk1, sk2):
    decrypted_1 = decrypt(ciphertext, sk2);
    #    print(decrypted_1);
    #  print(sk2)
    decrypted_2 = decrypt(decrypted_1, sk1);

    return decrypted_2;


##########################################################

def list_reverse(a):
    b = [a[len(a) - i - 1] for i in range(len(a))];

    return b;


############################################################


if __name__ == '__main__':

    message = [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1];

    c = [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0];

    list_left = [];
    key_length = 12;

    for test_key_1 in range(2 ** key_length):
        test_key = int_to_bin(test_key_1);
        test_ciphertext = encrypt(message, test_key);
        list_left.append(test_ciphertext);

    indexes, binary_list, int_list = binary_search.efficient_binary_sorting(list_left);

    num = 0;

    valid_keys_1 = [];
    valid_keys_2 = [];

    for test_key_2 in range(2 ** key_length):

        test_key = int_to_bin(test_key_2);
        middle_value = decrypt(c, test_key);

        # convert binary to int
        int_val = binary_search.binary_to_int(middle_value);
        pos = binary_search.dicotomic_search(int_list, 0, len(int_list) - 1, int_val);
        if pos > 0:
            num += 1;
            print("We found a valid key pair");
            key_1 = int_to_bin(indexes[pos]);
            print("sk1 = " + str(key_1) + ", sk2 = " + str(test_key));
            print("-----------------------------------------");

            valid_keys_1.append(key_1);
            valid_keys_2.append(test_key);

    print("num of valid key pairs = " + str(num));

    ######################################
    # SECOND ATTEMPT

    message = [1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1]
    c = [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0]

    list_left = [];

    for test_key in valid_keys_1:
        test_ciphertext = encrypt(message, test_key);
        list_left.append(test_ciphertext);

    indexes, binary_list, int_list = binary_search.efficient_binary_sorting(list_left);

    num = 0;

    for test_key_2 in valid_keys_2:

        middle_value = decrypt(c, test_key_2);

        # convert binary to int
        int_val = binary_search.binary_to_int(middle_value);
        pos = binary_search.dicotomic_search(int_list, 0, len(int_list) - 1, int_val);
        if pos > 0:
            num += 1;
            print("We found a valid key pair");
            key_1 = valid_keys_1[indexes[pos]];
            print("sk1 = " + str(key_1) + ", sk2 = " + str(test_key_2));
            print("-----------------------------------------");

            valid_keys_1.append(key_1);
            valid_keys_2.append(test_key);

    print("num of valid key pairs = " + str(num));
