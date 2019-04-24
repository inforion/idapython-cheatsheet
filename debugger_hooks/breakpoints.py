
def set_python_bpt(ea, cond):
    ''' Set conditional breakpoint with Python function 
    
        Usage:
        set_python_bpt(0x08000688, 'view_regs()')    
    '''
    idaapi.add_bpt(ea, 4, BPT_DEFAULT)
    bpt = idaapi.bpt_t()
    idaapi.get_bpt(ea, bpt)
    bpt.elang = 'Python'
    bpt.condition = cond
    idaapi.update_bpt(bpt)

