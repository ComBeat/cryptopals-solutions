#  Here is the opening stanza of an important work of the English language:
#
# Burning 'em, if you ain't quick and nimble
# I go crazy when I hear a cymbal
#
# Encrypt it, under the key "ICE", using repeating-key XOR.
#
# In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.
#
# It should come out to:
#
# 0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
# a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f
#
# Encrypt a bunch of stuff using your repeating-key XOR function. Encrypt your mail. Encrypt your password file. Your .sig file. Get a feel for it. I promise, we aren't wasting your time with this.
import binascii


def repeating_key_xor(s):
    print(f"{s=}")
    print(f"{type(s)=}")
    key = "ICE"
    hex_key = binascii.hexlify(bytes(key, 'utf-8'))
    print(f"{hex_key=}")
    print(f"{type(hex_key)=}")

    #print(s ^ hex_key)

    return "TODO"


if __name__ == "__main__":
    to_encrypt = str.split("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", '\n')
    expected_out = ["0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272",
                    "a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"]
    actual_out = []
    #print(f"{expected_out[0]}")
    #print(f"{type(expected_out[0])}")

    for i in to_encrypt:
        actual_out.append(repeating_key_xor(i))

    if False:
        print(f"{expected_out=}")
        print(f"{len(expected_out)=}")
        print(f"{actual_out=}")
        print(f"{len(actual_out)=}")
        if expected_out == actual_out:
            print("Yay")
        else:
            print("Unequal length!")
