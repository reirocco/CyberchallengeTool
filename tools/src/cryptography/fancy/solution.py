import copy

#plaintext m: binary string of length 16

#key k: binary string of length 10
def my_fancy_cipher(m,k):
    
    c = copy.copy(m);

    #Encryption process
    for i in range(7):
        for j in range(0,len(k)):

            if k[j]==1:
                pos_0 = ((i+j)+2)%16;
                pos_1 = (j+i)%16;
                tmp = c[pos_0];
                c[pos_0] = (c[j]+k[pos_1%len(k)])%2
                c[pos_1] = (tmp+k[pos_0%len(k)])%2;
            

    return c;

#####################################

k = [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0]

m = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0]


test_c = my_fancy_cipher(m,k);
print("Challenge m1 = "+str(m));
print("Challenge c1 = "+str(test_c))

list_of_keys = [];

print("Using first pair of plaintext-ciphertext");

#m = [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0];
#test_c = [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0];

for dec_key in range(2**16):

    test_k = format(dec_key,"b").zfill(16);
    test_k_as_list = [];
    for i in range(16):
        if test_k[i]=="0":
            test_k_as_list.append(0);
        else:
            test_k_as_list.append(1);
    new_c = my_fancy_cipher(m,test_k_as_list);

    if new_c == test_c:
        print("Found a valid key : k = ["+str(test_k)+"]")
        list_of_keys.append(test_k_as_list);
#    print(test_k_as_list)


print("Refining keys, using second pair of plaintext ciphertext")

m = [1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1];

test_c = my_fancy_cipher(m,k);
print("Challenge m2 = "+str(m));
print("Challenge c2 = "+str(test_c))

true_secret_key = [];

for i in range(len(list_of_keys)):

    test_k_as_list = list_of_keys[i];

    new_c = my_fancy_cipher(m,test_k_as_list);

    if new_c == test_c:
        print("Found a valid key : k = ["+str(test_k_as_list)+"]")
        true_secret_key = test_k_as_list;
        list_of_keys.append(test_k);

print("The found secret key is ");
print(true_secret_key);