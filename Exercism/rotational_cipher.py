"""
Create an implementation of the rotational cipher, also sometimes called the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on
transposing all the letters in the alphabet using an integer key
between `0` and `26`. Using a key of `0` or `26` will always yield
the same output due to modular arithmetic. The letter is shifted
for as many values as the value of the key.

The general notation for rotational ciphers is `ROT + <key>`.
The most commonly used rotational cipher is `ROT13`.

A `ROT13` on the Latin alphabet would be as follows:

```text
Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: nopqrstuvwxyzabcdefghijklm
```

It is stronger than the Atbash cipher because it has 27 possible keys, and 25 usable keys.

Ciphertext is written out in the same formatting as the input including spaces and punctuation.
"""

import string


def rotate(text, key):
    """Shifts letters a certain amount
    :text: string
    :key: int
    :returns: string"""

    alphabet = string.ascii_lowercase
    cipher = {}
    coded_text = ''
    for i in range(26):
        if key >= 26:
            key = 0
        cipher[alphabet[i]] = alphabet[key]
        cipher[alphabet[i].upper()] = alphabet[key].upper()
        key += 1

    for char in text:
        if char in cipher:
            coded_text += cipher[char]
        else:
            coded_text += char

    return coded_text
