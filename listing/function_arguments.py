''' Make comment to function, using it's argument (using x86 mnemonics)

'''
      
def get_function_arg_value(addr):
    ''' Find first function argument as an argument to PUSH before function call
        From command `PUSH 0x138` it will return integer value 312 (0x138)
        From command `PUSH EBX` it will return integer value 3 (as EBX is 3-rd register)
    '''
    while True:
        addr = PrevHead(addr)
        if GetMnem(addr) == "push":
            break
    res = GetOperandValue(addr, 0)
    return addr, res

                 
def get_function_arg(addr):
    ''' Find first function argument as an argument to PUSH before function call
        From command `PUSH 0x138` it will return string value '0x138'
        From command `PUSH EBX` it will return string value 'EBX'
    '''
    while True:
        addr = PrevHead(addr)
        if GetMnem(addr) == "push":
            break
    res = GetOpnd(addr, 0)
    return addr, res                

  
def comment_func(func_ea):
    ''' Make comment to function
    '''
    i = 0
    for x in XrefsTo(func_ea, flags=0):
        addr, val = get_function_arg_value(x.frm)
        MakeComm(x.frm, "func_name(0x%08x)" % val)
