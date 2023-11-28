# Fixed XOR
# Write a function that takes two equal-length buffers and produces their XOR combination.
# Input 1:          1c0111001f010100061a024b53535009181c
# Input 2:          686974207468652062756c6c277320657965
# Wanted output:    746865206b696420646f6e277420706c6179

def xor_on_hex(h1, h2):
    if len(h1) != len(h2):
        print("Unequal lengths!")
        return ""
    bin1 = int(format(int(h1), 'b'))
    print(f'{bin1=}')
    #print(bin1.__sizeof__())
    bin2 = int(format(int(h2), 'b'))
    #print(bin2.__sizeof__())
    print(f'{bin2=}')
    # return bin1 ^ bin2
    return hex(h1 ^ h2)


def xor_on_strings(s1, s2):
    return {int(hex(int(s1) ^ int(s2))): 'x'}


if __name__ == "__main__":
    n1 = 0x1c0111001f010100061a024b53535009181c
    # n1 = r'1c0111001f010100061a024b53535009181c'
    print(f'{n1=}')

    n2 = 0x686974207468652062756c6c277320657965
    # n2 = r'686974207468652062756c6c277320657965'
    print(f'{n2=}')

    expected_xor = r'746865206b696420646f6e277420706c6179'
    print(f"{expected_xor=}")
    if False:
        actual_xor = xor_on_hex(n1, n2)
        # actual_xor = xor_on_strings(n1, n2)
        # actual_xor = f"{int(hex(int(n1) ^ int(n2))): 'x'}"
        print(f"{actual_xor=}")

        # print(f'{0xABC123EFFF:b}')
        if expected_xor == actual_xor:
            print("Success!")
        else:
            print("Failure!")
