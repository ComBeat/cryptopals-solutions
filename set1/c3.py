# Input: 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# has been XOR'd against a single character. Find the key, decrypt the message.
# You can do this by hand. But don't: write code to do it for you.
#
# How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.
import binascii
import cryptography

freqs = {
    'a': 0.0651738,
    'b': 0.0124248,
    'c': 0.0217339,
    'd': 0.0349835,
    'e': 0.1041442,
    'f': 0.0197881,
    'g': 0.0158610,
    'h': 0.0492888,
    'i': 0.0558094,
    'j': 0.0009033,
    'k': 0.0050529,
    'l': 0.0331490,
    'm': 0.0202124,
    'n': 0.0564513,
    'o': 0.0596302,
    'p': 0.0137645,
    'q': 0.0008606,
    'r': 0.0497563,
    's': 0.0515760,
    't': 0.0729357,
    'u': 0.0225134,
    'v': 0.0082903,
    'w': 0.0171272,
    'x': 0.0013692,
    'y': 0.0145984,
    'z': 0.0007836,
    ' ': 0.1918182
}


def get_score(s2):
    score = 0
    for i in s2:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score


def find_xor_char(s1):
    # I know this is inefficient. Maybe I will improve it in the future lol
    result_list = []
    for u in range(256):
        result_string = ""
        for c in s1:
            result_char = chr(c ^ u)
            result_string += result_char
        result_list.append((get_score(bytearray(result_string, 'utf-8')), u, result_string))

    return max(result_list)


if __name__ == "__main__":
    hex_var = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ascii_string = binascii.unhexlify(hex_var)
    print(find_xor_char(ascii_string))
