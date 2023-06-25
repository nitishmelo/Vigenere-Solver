import pytest
import VignereBreakWithKeyLength as VP
import KeyLengthCalc as KLC
import VigenereCompleteBreak as VCB

multipletextsdata = []
bigtextdata = []

def callAndAssert(cipherText, capsys, plainText, key, keyLen):
    assert KLC.KeyLength(cipherText) == keyLen
    expected = f"\nKey: {key}\n" + f"Plaintext: {plainText}\n"
    VP.breaker(cipherText, keyLen)
    captured = capsys.readouterr()
    assert captured.out == expected

def test_no_letters(capsys):
    VCB.decode(":)")
    captured = capsys.readouterr()
    assert captured.err == "Text cannot be decrypted; there are no letters."

@pytest.mark.parametrize('cipherText, plainText, key, keylen, testID', multipletextsdata)
def test_multiple_cipher_texts(cipherText, plainText, key, keylen, testID, capsys):
    callAndAssert(cipherText, capsys, plainText, key, keylen)

@pytest.mark.parametrize('cipherText, plainText, key, keylen, testID', bigtextdata)
def test_with_big_text(cipherText, plainText, key, keylen, testID, capsys):
    callAndAssert(cipherText, capsys, plainText, key, keylen)