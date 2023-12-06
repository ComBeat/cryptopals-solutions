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


def score(c):
    score = 0
    return score


def find_xor_char(s):


if __name__ == "__main__":
    if False:
        hex_var = 0x1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
        # hex_var = '573908803ff9899a9889c00090f873784bcaff'
        ascii_string = binascii.unhexlify(hex_var).decode("utf-8")

        print(ascii_string)
        bin_var = format(hex_var, 'b')
        # bin_var = bin(hex_var)
        ascii_char_indexes = list(range(32, 127))

        # Fill String with necessary leading 0's
        if len(bin_var) % 8 != 0:
            print(len(bin_var))
            i = 8 - (len(bin_var) % 8)
            for x in range(i):
                bin_var = '0' + bin_var

            print(len(bin_var))

        # Slice binary string into bytes
        x = 8
        bin_var = [bin_var[y - x:y] for y in range(x, len(bin_var) + x, x)]
        print(len(bin_var))

        bla = ""
        for i in bin_var:
            bla += chr(int(i))

        print(len(bla))

        char_count = {}
        for i in bin_var:
            char_count[i] = bin_var.count(i)
            print(f"{i} = {bin_var.count(i)}")
        #for i in ascii_char_indexes:
         #   print(chr(int(i)))

        print(char_count)
        print(max(char_count.values()))
        max_keys = [key for key, value in char_count.items() if value == max(char_count.values())]
        print(max_keys)
        s = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
        print(s)

    hex_var = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ascii_string = binascii.unhexlify(hex_var)
    print(ascii_string)
