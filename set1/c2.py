# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# Input 1:          1c0111001f010100061a024b53535009181c
# Input 2:          686974207468652062756c6c277320657965
# Wanted output:    746865206b696420646f6e277420706c6179

def xor_on_int(h1, h2):
    if h1.__sizeof__() != h2.__sizeof__():
        print("Unequal lengths!")
        return ""
    bin1 = int(format(h1, 'b'))
    print(f'{bin1=}')
    #print(bin1.__sizeof__())
    print(f"{type(bin1)=}")
    bin2 = int(format(h2, 'b'))
    #print(bin2.__sizeof__())
    print(f'{bin2=}')
    print(f"{type(bin2)=}")
    xor = format(bin1 ^ bin2, 'x')
    print(f"{xor=}")
    return xor


def xor_on_strings(s1, s2):
    return s1 ^ s2


if __name__ == "__main__":
    n1 = 0x1c0111001f010100061a024b53535009181c
    # n1 = r'1c0111001f010100061a024b53535009181c'
    print(f'{n1=}')
    print(f"{type(n1)=}")

    n2 = 0x686974207468652062756c6c277320657965
    # n2 = r'686974207468652062756c6c277320657965'
    print(f'{n2=}')
    print(f"{type(n2)=}")

    expected_xor = 0x746865206b696420646f6e277420706c6179
    # expected_xor = r'746865206b696420646f6e277420706c6179'
    print(f"{expected_xor=}")
    print(f"{type(expected_xor)=}")
    if True:
        # actual_xor = xor_on_int(n1, n2)
        actual_xor = n1 ^ n2
        # actual_xor = f"{int(hex(int(n1) ^ int(n2))): 'x'}"
        print(f"{actual_xor=:x}")
        print(f"{expected_xor=:x}")

        if expected_xor == actual_xor:
            print("Success!")
        else:
            print("Failure!")
