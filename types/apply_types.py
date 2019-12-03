''' Work with type information (set/change type for object)


## T_INFO* constants

idc.TINFO_GUESSED   = 0x0000 # this is a guessed type
idc.TINFO_DEFINITE  = 0x0001 # this is a definite type
idc.TINFO_DELAYFUNC = 0x0002 # if type is a function and no function exists at ea,
                             # schedule its creation and argument renaming to
                             # auto-analysis otherwise try to create it immediately

ida_typeinf.TINFO_STRICT = _ida_typeinf.TINFO_STRICT

'''

def set_type(ea, type_str):
    _type = parse_decl(type_str, 0)  
    apply_type(ea, _type, 0)


# Usage:
# Set type to printf-like function
# set_type(0x000105E0, "int printf(const char *fmt, ...)")
