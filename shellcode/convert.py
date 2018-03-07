'''
Simple hex converter in little-endian representation
'''

from sys import argv
import binascii

def conv(input):
    reversed = input[::-1]
    rev_bytes = reversed.encode('utf-8')
    return binascii.b2a_hex(rev_bytes)


if __name__ == '__main__':
    if len(argv) > 1:
        print(conv(argv[1]))
