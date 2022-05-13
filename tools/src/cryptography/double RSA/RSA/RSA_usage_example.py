import hashlib
from random import randint, random
import binascii
import binary_search

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

##########################################

m = 34360524800; #key to be encrypted

#Generate RSA public key
keyPair = RSA.generate(2048);
pubKey = keyPair.publickey()
n = pubKey.n;
e = pubKey.e;

print("Public key is:");
print("n = "+hex(n));
print("e = "+hex(e));

#Encrypt m as m^e mod n
c = pow(m, e ,n); #compute power and reduce mod n

print("Ciphertext is c = "+hex(c));