import os
import pytest
from test_complete_break import data  

@pytest.hookimpl()
def pytest_sessionstart():
    for file in os.listdir("./files"):
        with open(f"./files/{file}") as fp:
            cipherText = fp.readline().strip('\n')
            plainText = fp.readline().strip('\n')
            key = fp.readline().strip('\n')
            keylen = int(fp.readline())
            data.append((cipherText, plainText, key, keylen))