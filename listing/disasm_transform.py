''' Short and simple transformations in disassembler view
'''

def make_offsets32(start_ea, end_ea):
    ''' Transform data to offsets (using 32-bit length) '''
    for addr in range(start_ea, end_ea, 4): 
        OpOff(addr, 0, 0)


def make_dwords(start_ea, end_ea):
    ''' Transform data to dwords in hex (using 32-bit length) '''
    for addr in range(start_ea, end_ea, 4): 
        OpHex(addr, 0)

