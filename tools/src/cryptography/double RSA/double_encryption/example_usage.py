
import hashlib
from random import randint, random
import binascii

#DOUBLE ENCRYPTION WITH CIPHER USING KEYS OF LENGTH key_length
key_length = 12;

##convert hex to bin
def hex_to_bin(hex_string, bin_length):
    bin_string = bin(int(hex_string,16))[2:];
    return bin_string.zfill(bin_length)

#Generate 5 pseudo-random bits from the input x
#x must be in list format
def gen_key_stream(x):

    digest = hashlib.sha256(str(x).encode('utf-8')).hexdigest();
    binary_digest = hex_to_bin(digest, 256);
    return binary_digest[0:5];

#m is the plaintext, sk is the secret key
#both m and sk must be in list format
def encrypt(m,sk):

    c = [];
    x = sk.copy();
    d = gen_key_stream(x);
    for i in range(4):
        for j in range(5):
            y = m[i*5+j]^(ord(d[j])-48);
            c.append(y);
            x[(i*5+j)%key_length] = x[(i*5+j)%key_length]^m[i*5+j];
        d = gen_key_stream(x);

    return c;

def decrypt(c, sk):

    m = [];
    x = sk.copy();
    d = gen_key_stream(x);
    for i in range(4):
        for j in range(5):
            y = c[i*5+j]^(ord(d[j])-48);
            m.append(y);
            x[(i*5+j)%key_length] = x[(i*5+j)%key_length]^y;
        d = gen_key_stream(x);

    return m;

########################

##TRUE ENCRYPTION AND DECRYPTION FUNCTIONS
##IT'S A DOUBLE ENCRYPTION AND DECRYPTION ROUTINE: TWO KEYS ARE NEEDED!
def double_encryption(plaintext,sk1,sk2):
    
    ciphertext_1 = encrypt(plaintext, sk1);
    ciphertext_2 = encrypt(ciphertext_1, sk2);

    return ciphertext_2;

def double_decryption(ciphertext,sk1,sk2):
    
    decrypted_1 = decrypt(ciphertext, sk2);
    decrypted_2 = decrypt(decrypted_1, sk1);

    return decrypted_2;


##########################################################
###EXAMPLE OF USAGE


secret_key_1 = [1,1,0,0,1,0,0,1,1,0,1,1];
secret_key_2 = [0,1,0,1,0,1,0,1,0,1,0,0];

message = [1,0,0,1,0,1,0,1,1,1,0,0,1,0,1,1,0,1,0,1];
print("m = "+str(message));

c = double_encryption(message,secret_key_1, secret_key_2);
m = double_decryption(c, secret_key_1, secret_key_2);
print("c = "+str(c));

sec = input('Press something to quit\n')
