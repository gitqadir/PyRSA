# PyRSA
This Python project demonstrates the implementation of the RSA (Rivest–Shamir–Adleman) algorithm for encrypting and decrypting messages. RSA is a widely used public-key cryptosystem that is based on the difficulty of factoring large integers. This project provides a simple yet effective example of how RSA encryption and decryption works.

# RSA Encryption and Decryption in Python

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Working](#working)
- [License](#license)

## Introduction
RSA encryption is a public-key cryptosystem that uses two keys: a public key for encryption and a private key for decryption. This project showcases a Python implementation of RSA encryption and decryption, allowing users to securely encrypt messages using a public key and decrypt them using the corresponding private key.

## Installation
To use this project, you'll need Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/gitqadir/PyRSA.git
```
Once cloned, navigate to the project directory:
```bash
cd PyRSA
```
## Usage
To encrypt and decrypt messages using RSA, follow these steps:

Run PyRSA.py script.
Enter prime numbers in the terminal when prompted.
View all the RSA alogirthm parameters printed in terminal.

## Working
Python code explanation:
1.	Import math and sys libraries, define global variables as I use them to change font colours, define a few functions.
2.	Create a dictionary, with key value pairs defining A: 1, B: 2, C: 3 for encryption and a reverse dictionary 1: A, 2: B, 3: C for decryption.
3.	Ask the user to input a prime number ‘p’ and ‘q’ in the range of 500-1000 and validate the input if it is a prime number within range and p ≠ q.
4.	Calculate RSA algorithm parameters n, z, e, d, public key, private key and print them.
(_Calculation of n, z is easy. For values e and z, we use a while loop that checks if gcd(e, z) == 1, if not then increments e to get the correct value. Similarly for d using the formula ed = ((x*z) + 1) gives d as a float value, so we use a loop to increment x till we have an int value for d. [This can be understood more clearly by seeing the code]_)
6.	Once we have all the parameters, we encrypt our message character by character by using the formula c =  me mod n. This is done by creating a for loop that iterates over the characters in message and computing c. The encrypted characters are then stored in a list. We print the plain text characters, its numerical representation, me, and the cipher text.
7.	Similar to encryption, we decrypt our message stored as cipher text in a list, and use the reverse dictionary to find what the plain text character is using its numerical representation.

![Image](/images/gitRSA.png)
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
