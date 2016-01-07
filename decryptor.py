import string

def dec_gen(encoded, subs):
    for i, letter in enumerate(encoded):
        yield subs.get(letter, letter)


def decrypt(ciphercode, key):
    mapping = dict()
    for i in range(26):
        mapping[key[i]] = string.ascii_lowercase[i]

    return ''.join([letter for letter in dec_gen(ciphercode, mapping)])
