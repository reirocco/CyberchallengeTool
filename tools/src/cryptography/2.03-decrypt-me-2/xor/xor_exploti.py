import base64

challenge_ciphertext = base64.b64decode("AQYABXAmRTpZCxZSRTMABAEJFw8LRA==").decode("ascii")
known_ciphertext = base64.b64decode("AAAAAAACFllUARYAFRwJDAMRFxkYAA==").decode("ascii")
known_plaintext = base64.b64decode("VGhpcyBpcyB0aGUgcGxhaW50ZXh0IQ==").decode("ascii")

def encrypt(x,y):
   return ''.join([chr(ord(x[i]) ^ ord(y[i])) for i in range(len(x))])

key = encrypt(known_ciphertext,known_plaintext)
print("key --> " + key)
print("decripted --> " + encrypt(key,challenge_ciphertext))
