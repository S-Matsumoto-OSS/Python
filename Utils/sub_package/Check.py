"""
=======================================================
Project Name : Python
File Name : Check.py
Encoding : UTF-8
Creation Date : 2020/9/13

Operation Confirmation by Python 3.8.2

Copyright (c) 2020 Shogo Matsumoto. All rights reserved.
=======================================================
"""
#coding:utf-8

"""
Transform string 'True' into bool True
"""
def istrue(s):
    try:
        if s != 'True' or s != 'true':
            raise Exception
    except:
        return False
    else:
        return True

"""
Confirm that s is only numerical value, or 
Transform s into float type variable
"""
def isnum(s, return_float = False):
    try:
        float(s)
    except ValueError:
        return False
    else:
        if return_float:
            return float(s)
        else:
            return True

"""
* This function is used in special case (e.g. s = '"apple"')
Remove "" or '' from s (e.g. '"apple"' --> 'apple')
"""
def isstr(s, return_str = False):
    try:
        if (s[0] == "'" and s[-1] == "'") or (s[0] == '"' and s[-1] == '"'):
            s = s[1:-1]
        else:
            raise Exception
    except:
        return False
    else:
        if return_str:
            return s
        else:
            return True

"""
* This function is used in special case (e.g. s = '["1.0", "5.0"]')
Transform string type list (whose element is numerical value) into list type 
(e.g. '["1.0", "5.0"]' --> [1.0, 5.0])
"""
def isnumlist(s, return_list = False):
    try:
        if s[0] == '[' and s[-1] == ']':
            l = s[1:-1].split(',')
            l = [float(v) for v in l]
        else:
            raise Exception
    except:
        return False
    else:
        if return_list:
            return l
        else:
            return True

"""
* This function is used in special case (e.g. s = '["at", "in"]')
Transform string type list (whose element is string value) into list type 
(e.g. '["at", "in"]' --> ["at", "in"])
"""
def isstrlist(s, return_list = False):
    try:
        if s[0] == '[' and s[-1] == ']':
            s = s.replace(' ', '')
            s = s.replace('"', '')
            s = s.replace("'", "")
            l = s[1:-1].split(',')
        else:
            raise Exception
    except:
        return False
    else:
        empty = [i for i, x in enumerate(l) if x == '']
        for i in range(0, len(empty), 2):
            l[empty[i]] = ','
        while '' in l:
            l.remove('')
        if return_list:
            return l
        else:
            return True