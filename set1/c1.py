# Convert hex to base64
# input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# wanted output: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
import base64


def hex_to_b64(hex_str):
    return base64.b64encode(bytes.fromhex(hex_str)).decode('ascii')


if __name__ == "__main__":
    hex_string = r'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected_b64 = r'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    actual_b64 = hex_to_b64(hex_string)

    print(f"{expected_b64=}")
    print(f"{actual_b64=}")
    if expected_b64 == actual_b64:
        print("Success!")
