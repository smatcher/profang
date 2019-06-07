import ctypes
import ctypes.wintypes
import os
import re

_lib = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'Everything64.dll'))

def _solvetype(type):
    return {
        'void': ctypes.c_void_p,
        'BOOL': ctypes.wintypes.BOOL,
        'DWORD': ctypes.wintypes.DWORD,
        'LPCWSTR': ctypes.wintypes.LPCWSTR
    }[type]

def _reg(signature):
    m = re.match(r'(?P<return_type>\w+)\s+(?P<function_name>\w+)\((?P<args_list>.*)\)', signature)
    args_list = m.group('args_list') and m.group('args_list').split(',') or []
    argtypes = [m.group('return_type')]
    paramflags = []
    for arg in args_list:
        m2 = re.match(r'''(?P<arg_type>\w+)\s+(?P<arg_name>\w+)\s+=\s+(?P<arg_default>["']?\w*["']?)''', arg)
        argtypes.append(m2.group('arg_type'))
        paramflags.append((1, m2.group('arg_name'), eval(m2.group('arg_default'))))
    argtypes = list(map(_solvetype, argtypes))
    prototype = ctypes.WINFUNCTYPE(*argtypes)
    return prototype((m.group('function_name'), _lib), tuple(paramflags))

SetSearch         = _reg('void Everything_SetSearchW(LPCWSTR pattern = "")')
Query             = _reg('void Everything_QueryW(DWORD wait = True)')
GetNumResults     = _reg('DWORD Everything_GetNumResults()')
GetResultPath     = _reg('LPCWSTR Everything_GetResultPathW(DWORD index = 0)')
GetResultFileName = _reg('LPCWSTR Everything_GetResultFileNameW(DWORD index = 0)')
SetRequestFlags   = _reg('void Everything_SetRequestFlags(DWORD requestFlags = 3)')

def listFiles(pattern):
    """
        Find files using everything
        see everything documentation for pattern syntax
    """
    SetSearch(pattern)
    SetRequestFlags()
    Query()
    return list(map(lambda i: os.path.join(GetResultPath(i), GetResultFileName(i)), range(GetNumResults())))
