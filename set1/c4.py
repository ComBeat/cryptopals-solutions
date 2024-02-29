# One of the 60-character strings in file c4.txt has been encrypted by single-character XOR.
# Find it.
import binascii

import c3

if __name__ == "__main__":
    result_list = []

    with open('c4.txt') as f:
        lines = f.readlines()
    lines = list(map(str.strip, lines))

    for i in lines:
        ascii_string = binascii.unhexlify(i)
        result_list.append(c3.find_xor_char(ascii_string))

    print(max(result_list))
