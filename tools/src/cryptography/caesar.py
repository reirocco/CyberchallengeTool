#receive as input a ciphertext c and a key k
#the ciphertext musr be written as capital letters
#k is a number between 0 and 25
def caesar_decrypt(c,k):
    
    #convert characters into numbers in [0 ; 25]
    num_c = [];
    for i in range(len(c)):
        num_c.append(ord(c[i])-65);
    
    #decrypting
    m = "";
    for i in range(len(c)):

        c_minus_k = (num_c[i]-k)%26;
        m+=chr(c_minus_k+65);

    return m;




c = "DHRFGNCNFFJBEQRQVSSVPVYVFFVZN"
for k in range(26):
    m = caesar_decrypt(c,k);
    print("For k = "+str(k)+", m = "+str(m));