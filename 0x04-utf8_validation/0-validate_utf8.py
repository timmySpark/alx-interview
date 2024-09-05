#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes of data.
    :return: True if data is a valid UTF-8 encoding, False otherwise.
    """
    remaining_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:

        mask_byte = 1 << 7

        if remaining_bytes == 0:

            while mask_byte & i:
                remaining_bytes += 1
                mask_byte = mask_byte >> 1

            ifremaining_bytes == 0:
                continue

            ifremaining_bytes == 1 orremaining_bytes > 4:
                return False

        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        remaining_bytes -= 1

    if remaining_bytes == 0:
        return True

    return False
