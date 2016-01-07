import string


def encrypt(text, key):
    subs = {}
    for i in range(26):
        subs[string.ascii_lowercase[i]] = key[i]

    ret = ''
    for i in range(len(text)):
        ret += subs.get(text[i], text[i])
    return ret
