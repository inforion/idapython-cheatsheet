''' Work with enums


'''

import re
import os
import sys

def create_enum_from_header(filename, enum_name):
    ''' Parse C header file with defines, make enum from them:

    #define EPERM            1      /* Operation not permitted */

    '''
    h_file_data = open(filename).read()
    defines = re.findall(r'#define\s+(\w+)\s+(\d+)\s+\/\*([\w\s]+)\*\/', h_file_data)
    enum_id = add_enum(idaapi.BADNODE, enum_name, 0)

    for m_name, m_value, m_comment in defines:
        add_enum_member(enum_id, m_name, int(m_value), ida_enum.DEFMASK)
        m_id = get_enum_member_by_name(m_name)
        set_enum_member_cmt(m_id, m_comment, repeatable=1)


def create_linux_errno_enum():
    path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(path, 'errno.h')
    create_enum_from_header(filename, 'LINUX_ERRNO')


def make_arg_enum_member(ea, enum_id):
    ''' Suggest we have instruction like this:

        push    0x18

    Let's make it more pretty:
        
        push    EMFILE          ;  Too many open files

    '''
    op_enum(ea, 0, enum_id, 0)

