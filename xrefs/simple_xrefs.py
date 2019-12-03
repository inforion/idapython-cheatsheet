''' Work with cross-references (add, delete, iterate)


#      Flow types (combine with XREF_USER!):
fl_CF   = 16              # Call Far
fl_CN   = 17              # Call Near
fl_JF   = 18              # jumpto Far
fl_JN   = 19              # jumpto Near
fl_F    = 21              # Ordinary flow

XREF_USER = 32            # All user-specified xref types
                          # must be combined with this bit


# Data reference types (combine with XREF_USER!):
dr_O    = ida_xref.dr_O  # Offset
dr_W    = ida_xref.dr_W  # Write
dr_R    = ida_xref.dr_R  # Read
dr_T    = ida_xref.dr_T  # Text (names in manual operands)
dr_I    = ida_xref.dr_I  # Informational


'''


def add_data_xref(from_ea, to_ea):
    ''' Add simple xref from `from_ea` address to data at `to_ea` address '''
    add_dref(from_ea, to_ea, XREF_USER | dr_O)


def add_code_xref(from_ea, to_ea):
    ''' Add simple xref from `from_ea` address to code at `to_ea` address '''
    add_cref(from_ea, to_ea, XREF_USER | fl_CF)

