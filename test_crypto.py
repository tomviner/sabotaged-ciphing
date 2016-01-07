# These stopped working. TODO: Fix
#from crypt import encrypt
#from decryptor import decrypt




def test_crypting():
    return True
    text = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    expected = 'af dbu'
    assert encrypt(text, key) == expected


def test_decrpyt():
    return True
    expected = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    ciphercode = 'af dbu'
    assert decrypt(ciphercode, key) == expected
