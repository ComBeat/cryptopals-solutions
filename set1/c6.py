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
import sys


def hamming_distance(s1, s2):
    if True:
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
    else:
        return sum([bin(s1[i] ^ s2[i]).count('1') for i in range(len(s1))])


if __name__ == '__main__':
    keysize = range(2, 41)
    test1 = b"this is a test"
    test2 = b"wokka wokka!!!"
    test_expected_difference = 37
    #test_actual_difference = hamming_distance(base64.b64encode(bytes(test1, 'utf-8')), base64.b64encode(bytes(test2, 'utf-8')))
    test_actual_difference = hamming_distance(base64.b64encode(test1), base64.b64encode(test2))
    #test_actual_difference = hamming_distance(test1, test2)

    with open('c6.txt', 'rb') as f:
        # fcontent = f.readlines()
        for ks in range(len(keysize) - 1):
            byte1 = f.read(keysize[ks])
            f.seek(-keysize[ks], 1)
            byte2 = f.read(keysize[ks] + 1)
            print(byte1, byte2)
            print(hamming_distance(byte1, byte2))


    # for s in fcontent:
    #    while byte := s[1]:
    #        print(byte)

    print(f"{test_expected_difference=}", f"{test_actual_difference=}")
    if test_expected_difference == test_actual_difference:
        print("Test Yay")
    else:
        print("Test Nooo")
        sys.exit()

    for ks in keysize:
        pass
