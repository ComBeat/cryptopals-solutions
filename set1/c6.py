#  There's a file here. It's been base64'd after being encrypted with repeating-key XOR.
#
# Decrypt it.
#
# Here's how:
#
#     1) Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
#     2) Write a function to compute the edit distance/Hamming distance between two strings. The Hamming distance is just the number of differing bits. The distance between:
#     this is a test
#     and
#     wokka wokka!!!
#     is 37. Make sure your code agrees before you proceed.
#     3) For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, and find the edit distance between them. Normalize this result by dividing by KEYSIZE.
#     4) The KEYSIZE with the smallest normalized edit distance is probably the key. You could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE blocks instead of 2 and average the distances.
#     5) Now that you probably know the KEYSIZE: break the ciphertext into blocks of KEYSIZE length.
#     6) Now transpose the blocks: make a block that is the first byte of every block, and a block that is the second byte of every block, and so on.
#     7) Solve each block as if it was single-character XOR. You already have code to do this.
#     8) For each block, the single-byte XOR key that produces the best looking histogram is the repeating-key XOR key byte for that block. Put them together and you have the key.
#
# This code is going to turn out to be surprisingly useful later on. Breaking repeating-key XOR ("Vigenere") statistically is obviously an academic exercise, a "Crypto 101" thing. But more people "know how" to break it than can actually break it, and a similar technique breaks something much more important.
import base64


def hamming_distance(s1, s2):
    distance = 0

    if len(s1) != len(s2):
        distance = -1
        return distance

    s1_decoded = base64.b64decode(s1)
    s2_decoded = base64.b64decode(s2)

    for byte1, byte2 in zip(s1_decoded, s2_decoded):
        # XOR the bytes and count the differing bits
        xor_result = byte1 ^ byte2
        distance += bin(xor_result).count('1')

    return distance


if __name__ == '__main__':
    keysize = range(2, 41)
    test1 = "this is a test"
    test2 = "wokka wokka!!!"
    expected_difference = 37
    actual_difference = hamming_distance(base64.b64encode(bytes(test1, 'utf-8')), base64.b64encode(bytes(test2, 'utf-8')))

    with open('c6.txt') as f:
        fcontent = f.readlines()

    print(f"{expected_difference=}", f"{actual_difference=}")
    if expected_difference == actual_difference:
        print("Test Yay")
    else:
        print("Test Nooo")
