"""
Implement run-length encoding and decoding.

Run-length encoding (RLE) is a simple form of data compression, where runs
(consecutive data elements) are replaced by just one data value and count.

For example we can represent the original 53 characters with only 13.

```
"WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"  ->  "12WB12W3B24WB"
```

RLE allows the original data to be perfectly reconstructed from
the compressed data, which makes it a lossless data compression.

```
"AABCCCDEEEE"  ->  "2AB3CD4E"  ->  "AABCCCDEEEE"
```

For simplicity, you can assume that the unencoded string will only contain
the letters A through Z (either lower or upper case) and whitespace. This way
data to be encoded will never contain any numbers and numbers inside data to
be decoded always represent the count for the following character.
"""

import re


def decode(data):
    num = ''
    decoded = ''
    for i in range(len(data)):
        if data[i].isdigit() and data[i] not in num:
            num += data[i]
        else:
            if num != '':
                decoded += data[i]*int(num)
                num = ''
            else:
                decoded += data[i]
    return decoded


def encode(data):
    string = ('').join(re.findall('[a-zA-z\s]+', data))
    encoded = ''
    count = 1
    previous = ''

    for i in range(len(string)):
        if i == 0:
            previous = string[i]
        elif string[i] == previous:
            count += 1
        else:
            if count == 1:
                encoded += previous
            else:
                encoded += str(count) + previous
            count = 1
            previous = string[i]
    if count == 1:
        encoded += previous
    else:
        encoded += str(count)+previous
    return encoded
