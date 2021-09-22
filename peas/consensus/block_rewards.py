from peas.util.ints import uint32, uint64

# 1 Peas coin = 1,000,000,000,000 = 1 trillion mojo.
_mojo_per_peas = 1000000000000
_blocks_per_year = 1681920  # 32 * 6 * 24 * 365


def calculate_pool_reward(height: uint32) -> uint64:
    """
    Returns the pool reward at a certain block height. The pool earns 7/8 of the reward in each block. If the farmer
    is solo farming, they act as the pool, and therefore earn the entire block reward.
    These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """ 
    if height == 0:
        return uint64(int((7 / 8) * 666666 * _mojo_per_peas))
    elif height < 0.003 * _blocks_per_year:
        return uint64(int((7 / 8) * 89 * _mojo_per_peas))
    elif height < 0.004 * _blocks_per_year:
        return uint64(int((7 / 8) * 55 * _mojo_per_peas))
    elif height < 0.008 * _blocks_per_year:
        return uint64(int((7 / 8) * 34 * _mojo_per_peas))
    elif height < 0.016 * _blocks_per_year:
        return uint64(int((7 / 8) * 21 * _mojo_per_peas))
    elif height < 0.03 * _blocks_per_year:
        return uint64(int((7 / 8) * 13 * _mojo_per_peas))
    elif height < 0.052 * _blocks_per_year:
        return uint64(int((7 / 8) * 8 * _mojo_per_peas))
    elif height < 0.087 * _blocks_per_year:
        return uint64(int((7 / 8) * 5 * _mojo_per_peas))
    elif height < 0.145 * _blocks_per_year:
        return uint64(int((7 / 8) * 3 * _mojo_per_peas))
    elif height < 0.238 * _blocks_per_year:
        return uint64(int((7 / 8) * 2 * _mojo_per_peas))
    elif height < 0.389 * _blocks_per_year:
        return uint64(int((7 / 8) * 1 * _mojo_per_peas))
    elif height < 0.633 * _blocks_per_year:
        return uint64(int((7 / 8) * 0.8 * _mojo_per_peas))
    elif height < 1 * _blocks_per_year:
        return uint64(int((7 / 8) * 0.5 * _mojo_per_peas))
    elif height < 1.6 * _blocks_per_year:
        return uint64(int((7 / 8) * 0.3 * _mojo_per_peas))
    elif height < 2.5 * _blocks_per_year:
        return uint64(int((7 / 8) * 0.2 * _mojo_per_peas)) 
    else:
        return uint64(int((7 / 8) * 0.1 * _mojo_per_peas))


def calculate_base_farmer_reward(height: uint32) -> uint64:
    """
    Returns the base farmer reward at a certain block height.
    The base fee reward is 1/8 of total block reward

    Returns the coinbase reward at a certain block height. These halving events will not be hit at the exact times
    (3 years, etc), due to fluctuations in difficulty. They will likely come early, if the network space and VDF
    rates increase continuously.
    """
 
    if height == 0:
        return uint64(int((1 / 8) * 666666 * _mojo_per_peas))
    elif height < 0.003 * _blocks_per_year:
        return uint64(int((1 / 8) * 89 * _mojo_per_peas))
    elif height < 0.004 * _blocks_per_year:
        return uint64(int((1 / 8) * 55 * _mojo_per_peas))
    elif height < 0.008 * _blocks_per_year:
        return uint64(int((1 / 8) * 34 * _mojo_per_peas))
    elif height < 0.016 * _blocks_per_year:
        return uint64(int((1 / 8) * 21 * _mojo_per_peas))
    elif height < 0.03 * _blocks_per_year:
        return uint64(int((1 / 8) * 13 * _mojo_per_peas))
    elif height < 0.052 * _blocks_per_year:
        return uint64(int((1 / 8) * 8 * _mojo_per_peas))
    elif height < 0.087 * _blocks_per_year:
        return uint64(int((1 / 8) * 5 * _mojo_per_peas))
    elif height < 0.145 * _blocks_per_year:
        return uint64(int((1 / 8) * 3 * _mojo_per_peas))
    elif height < 0.238 * _blocks_per_year:
        return uint64(int((1 / 8) * 2 * _mojo_per_peas))
    elif height < 0.389 * _blocks_per_year:
        return uint64(int((1 / 8) * 1 * _mojo_per_peas))
    elif height < 0.633 * _blocks_per_year:
        return uint64(int((1 / 8) * 0.8 * _mojo_per_peas))
    elif height < 1 * _blocks_per_year:
        return uint64(int((1 / 8) * 0.5 * _mojo_per_peas))
    elif height < 1.6 * _blocks_per_year:
        return uint64(int((1 / 8) * 0.3 * _mojo_per_peas))
    elif height < 2.5 * _blocks_per_year:
        return uint64(int((1 / 8) * 0.2 * _mojo_per_peas)) 
    else:
        return uint64(int((1 / 8) * 0.1 * _mojo_per_peas))


