#!/usr/bin/python3
'''Determines if a given data set represents a valid UTF-8 encoding
'''


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: A list of integers, where each integer represents 1 byte of data.
    :return: True if data is a valid UTF-8 encoding, else return False.
    """

    # Define a mask to check the most significant bits of each byte
    mask = 0b10000000
    # Initialize a variable to keep track of the number of bytes remaining in a character
    remaining_bytes = 0

    for byte in data:
        # Apply the mask to the byte to check the most significant bit
        masked_byte = byte & mask
        if remaining_bytes == 0:
            if masked_byte == 0:
                # This is a single-byte character, no need to check further
                continue
            elif (masked_byte & 0b11100000) == 0b11000000:
                # This is a two-byte character
                remaining_bytes = 1
            elif (masked_byte & 0b11110000) == 0b11100000:
                # This is a three-byte character
                remaining_bytes = 2
            elif (masked_byte & 0b11111000) == 0b11110000:
                # This is a four-byte character
                remaining_bytes = 3
            else:
                # Invalid starting byte
                return False
        else:
            if (masked_byte & 0b11000000) != 0b10000000:
                # Invalid continuation byte
                return False
            remaining_bytes -= 1

    # All characters have been processed, and if there are any remaining bytes, it's invalid
    return remaining_bytes == 0
