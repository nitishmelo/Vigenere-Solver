# Vigenere-Solver
A Vigenere Cipher Decoder. Uses IOC (Index of Coincidence) to approximate the key length, N, which is used to divide the ciphertext into N chunks. It then uses frequency analysis to determine the letter that decrypts each chunk, combining them all to form the plaintext.

Includes unit tests; specifically, parameterized tests for various inputs using PyTest. 
# Instructions On How to Run The Program
1. run ```python3 main.py```
# How to run the tests
1. ```pip install pytest```, if you do not have it installed.
2. run ```python -m pytest```
