'''
Script for parsing Global Descriptor Table (x86) inside IDA Pro database

https://wiki.osdev.org/Global_Descriptor_Table
'''

from struct import pack, unpack


def parse_access_byte(acc):
    pr = (acc & 0x80) >> 7
    privl = (acc & 0x60) >> 5
    ex = (acc & 0x8) >> 3
    dc = (acc & 0x4) >> 2
    rw = (acc & 0x2) >> 1
    ac = (acc & 0x1)
    res = "      Access: Pr {:b} Privl {:02x} Ex {:b} DC {:b} RW {:b} Ac {:b}".format(pr, privl, ex, dc, rw, ac)
    return res


def parse_GDT_record(bytes):
    limit_0_15, base_0_15 = unpack("HH", bytes[:4])
    base_16_23, acc, flags_limit, base_24_31 = unpack("BBBB", bytes[4:])
    base = pack("HBB", base_0_15, base_16_23, base_24_31)
    base = unpack("<I", base)[0]
    lim = flags_limit & 0x0F
    limit = pack("HBB", limit_0_15, lim, 0)
    limit = unpack("I", limit)[0]
    flags = flags_limit & 0xF0
    acc_str = parse_access_byte(acc)
    base_str = "Base {:08x} Limit {:08x} Access {:02x} Flags {:02x}".format(base, limit, acc, flags)
    return base_str, acc_str

    
def parse_GDT_table(start_ea, end_ea):
    ''' 
    Parse raw GDT-data and make comments in IDA Pro database
    Usage:
    parse_IDT_table(0x0011D7E8, 0x0011D940)       # GDT
    '''
    for n, ea in enumerate(range(start_ea, end_ea, 8), 0):
        record = idc.get_bytes(ea, 8)
        base, acc = parse_GDT_record(record)
        
        idc.set_cmt(ea, "0x{:02x} |0x{:04x}| {}".format(n, n*8, base), 0)
        idc.set_cmt(ea+4, acc + '\n', 0)
            
