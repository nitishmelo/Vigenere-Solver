import os
import pytest
from test_complete_break import multipletextsdata, bigtextdata

@pytest.hookimpl()
def pytest_sessionstart():
    for file in os.listdir("./files"):
        if file != "bigtextmultiplekeys.txt":
            with open(f"./files/{file}") as fp:
                cipherText = fp.readline().strip('\n')
                plainText = fp.readline().strip('\n')
                key = fp.readline().strip('\n')
                keylen = int(fp.readline())
                testID = f"Cipher with key of length {keylen}"
                multipletextsdata.append((cipherText, plainText, key, keylen, testID))
    with open("./files/bigtextmultiplekeys.txt", encoding='utf-8') as fp:
        plainText = fp.readline().strip('\n')
        for _ in range(9):
            cipherText = fp.readline().strip('\n')
            key = fp.readline().strip('\n')
            keylen = int(fp.readline().strip('\n'))
            testID = f"Cipher with key of length {keylen}"
            bigtextdata.append((cipherText, plainText, key, keylen, testID))