precomputed_parity = []


def parity(x):
    mask_size = 16
    bitmask = 0xFFFF

    return (
        precomputed_parity[x >> (3 * mask_size)]
        ^ precomputed_parity[(x >> (2 * mask_size)) & bitmask]
        ^ precomputed_parity[(x >> mask_size) & bitmask]
        ^ precomputed_parity[x & bitmask]
    )
