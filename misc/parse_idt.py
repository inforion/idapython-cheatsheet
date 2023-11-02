'''
Script for parsing Interrupt Descriptor Table (x86) inside IDA Pro database

http://wiki.osdev.org/Interrupt_Descriptor_Table

'''

from struct import pack, unpack


GATE_TYPE = {0x5: "32 bit task gate", 
             0x6: "16-bit interrupt gate", 
             0x7: "16-bit trap gate", 
             0xE: "32-bit interrupt gate", 
             0xF: "32-bit trap gate", 
            }


def parse_type_attr(type_attr):
    p = (type_attr & 0x80) >> 7
    dpl = (type_attr & 0x60) >> 5
    s = (type_attr & 0x10) >> 4
    gt = (type_attr & 0x0F)
    res = "   cType -->   Pr {:b}, Privl {:02x}, Storage {:b}, Gate: {}".format(p, dpl, s, 
                                                                  GATE_TYPE.get(gt, "None"))
    return res


def parse_IDT_record(bytes):
    offset_0_15, selector = unpack("HH", bytes[:4])
    zero, type_attr, offset_16_31 = unpack("BBH", bytes[4:])   
    offset = pack("HH", offset_0_15, offset_16_31)
    offset = unpack("<I", offset)[0]
    record_str = "Offset {:08x} Selector {:04x} Type {:02x}".format(offset, selector, type_attr)
    type_str = parse_type_attr(type_attr)
    return record_str, type_str

    
def parse_IDT_table(start_ea, end_ea):
    '''
    Parse raw IDT-data and make comments in IDA Pro database
    Usage:
    parse_IDT_table(0x0011CFE0, 0x0011D7E0)       # IDT
    '''
    for n, ea in enumerate(range(start_ea, end_ea, 8), 0):
        record = idc.get_bytes(ea, 8)
        base, acc = parse_IDT_record(record)
        
        idc.set_cmt(ea, "0x{:02x} |0x{:04x}| {}".format(n, n*8, base), 0)
        idc.set_cmt(ea+4, acc + '\n', 0)
        
        
        
    
# print(parse_GDT_record('\xDF\xFF\x00\xD0\x10\x92\x00\x00'))
