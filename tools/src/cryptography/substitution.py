import numpy as np
import copy

def substitution_encrypt(m,k):

    c = list(copy.copy(m));
    for i in range(len(m)):
        val_m = ord(m[i])-97;
        new_letter = k[val_m];
        new_chr = chr(new_letter+65);
        c[i] = new_chr;

    return "".join(c);

def decrypt(c,decryption_map):
    
    m = [];

    for i in range(len(c)):
        this_chr = c[i];
        pos = 0;
        for j in range(26):
            if decryption_map[j]==this_chr:
                pos = j;

        decrypted_chr = chr(pos+97);
        m.append(decrypted_chr)
   
    return "".join(m);


decryption_map = "UCIBMNEDXLQOHAKFSZWPVGTJRY";

c = "SVMWPKMVAIXNZUZXKUWKWPXPVYXKAMNVAYXKAUIKHMIMWUZMHUOMIDXUGXWKAKHKOPKFXVAVHMZKWM"

m = decrypt(c,decryption_map);
print(m);