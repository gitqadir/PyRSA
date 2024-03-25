'''
This python program implements the RSA key generation algorithm to encrypt and decrypt messages.
The script, prints all the important parameters of the RSA algorithm.

Steps to run the program:
1. Run the python code, The program asks user to input Prime numbers in the range of 500-1000.
2. Enter prime numbers and the rest of the code runs automatically, printing all the important parameters of RSA, cipher text and decrypted text.
3. The program has logic to validate your input, to check if it is prime and in the range 500-1000.
4. I used prime numbers 503 and 997, The smallest and largest in the range as values ofr p and q to test the algorithm.
'''


import math
from sys import exit

# Message to encrypt
message = 'QADIRSPYTHONPROGRAMTOIMPLEMENTRSAALGORITHM'

# Font colours
redf = '\033[31m'
resetf = '\033[0m'
bluef = '\033[34m'

print(bluef + " \n Algorithm Starts \n" + resetf)
# Cipher text and Decrypted text
cipher_text = {}
decrpyt_text = {}
cipher_list = []
decrypt_list = []


# Function for checking prime numbers
def is_prime(x):
    for i in range(2, x):
        if (x % i) == 0:
            return False
    return True


# Plaintext characters and their numerical representation
characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_char = {}
for x in range(len(characters)):
    num_char[characters[x]] = x+1
print('*-' * 50)
print(num_char)
print('*-' * 50 + "\n")

# Reverse Lookup for Decryption
char_decrypt = {val: key for (key, val) in num_char.items()}

# Step 1:
# Take input from user for value of P
p = int(input(redf + "Enter a prime number for the value of p in the range 500 to 1000 \n" + resetf))
if p < 500 or p > 1000:
    print("Error: Enter a value in the range 500 to 1000")
    exit()
else:
    if is_prime(p):
        pass
    else:
        print("Error: p is not a prime number")
        exit()

# Take input from user for value of Q
q = int(input(redf + "Enter a prime number for the value of q in the range 500 to 1000 \n" + resetf))
if q == p:
    print("Error: Enter a value of q different than p")
    exit()
else:
    if q < 500 or q > 1000:
        print("Error: Enter a value in the range 500 to 1000")
        exit()
    else:
        if is_prime(q):
            print('*-' * 50 + "\n")
            print("The value of p is ", p)
            print("The value of q is ", q)
        else:
            print("Error: q is not a prime number")
            exit()

# Step 2: Calculate n
n = p * q
print("The value of n is ", n)

# Step 3: Calculate z
z = (p - 1) * (q - 1)
print("The value of z is ", z)

# Step 4: Calculate e, so that greatest common divisor is 1 and less than z
e = 2
while e < z:
    if math.gcd(e, z) == 1:
        break
    else:
        e += 1

print("The value of e is ", e)

# Step 5: Calculate d, such that ed - 1 is exactly divisible by z
x = 2
while x < z:
    d = ((x * z) + 1) / e
    if d.is_integer():
        d = int(d)
#        print("The value of x is ", x) #------------DEBUG STATEMENT------------#
        print("The value of d is ", d)
        print(f'Public key: {e, n}')
        print(f'Private key: {d, n}')
        print('*-' * 50 + "\n")
        break
    else:
        x += 1

# Step 6: Encryption and Getting value of m^e
for i in message:
    me = pow(num_char[i], e)
    c = int(math.fmod(me, n))
    print(f'Plaintext Character: {i} \t Numerical representation: {num_char[i]}\t m^e: {me}\t \t Ciphertext: {c}')
    cipher_text[i] = c
    cipher_list.append((i, c))
print('*-' * 50 + "\n")
print("List of characters and its cipher text: \n")
print(cipher_list)
print('*-' * 50 + "\n")

# Step 7: Decryption to verify the algorithm works
for i in cipher_list:
    # cd = pow(cipher_text[i], d)
    # print(cd)
    m = int(pow(i[1], d, n))
    print(f'Decrypted numerical representation: {m} \t Decrypted character: {char_decrypt[m]}')
    decrypt_list.append(char_decrypt[m])
print('*-' * 50 + "\n")
print(decrypt_list)
print('*-' * 50 + "\n")

# Step 8: Join list items to create string

decrypted_message = ''.join(decrypt_list)
print("Decrypted message is " + bluef + decrypted_message + resetf)
print('*-' * 50 + "\n")