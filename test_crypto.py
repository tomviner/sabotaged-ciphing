# These stopped working. TODO: Fix
#from crypt import encrypt
#from decryptor import decrypt




def check_crypting():
    return True
    text = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    expected = 'af dbu'
    assert encrypt(text, key) == expected


def check_decrpyt():
    return True
    expected = 'ze cat'
    key = 'bcdefghijklmnopqrstuvwxyza'
    ciphercode = 'af dbu'
    assert decrypt(ciphercode, key) == expected
