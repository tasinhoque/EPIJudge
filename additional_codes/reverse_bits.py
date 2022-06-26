precomputed_reverse = [0b00, 0b10, 0b01, 0b11]


def reverse_bits(x):
    mask_size = 16
    bitmask = 0xFFFF

    return (
        precomputed_reverse[x & bitmask] << (3 * mask_size)
        | precomputed_reverse[(x >> mask_size) & bitmask] << (2 * mask_size)
        | precomputed_reverse[(x >> (2 * mask_size)) & bitmask] << mask_size
        | precomputed_reverse[(x >> (3 * mask_size)) & bitmask]
    )
