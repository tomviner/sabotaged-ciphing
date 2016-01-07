from crypt import encrypt
from decryptor import decrypt


def test_crypting():
    text = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    expected = 'af dbu'
    assert encrypt(text, key) == expected


def test_decrpyt():
    expected = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    ciphercode = 'af dbu'
    assert decrypt(ciphercode, key) == expected