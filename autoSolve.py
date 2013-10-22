__author__ = 'archlevi'


def rule_1(s):
    if s[-1] == 'I':
        return s+'U'
    else:
        return s


def rule_2(s):
    try:
        if s[0] == 'M':
            return s + s[1:len(s)]
    except MemoryError:
        return 'MIUIUIUIUIUIU'
    else:
        return s


def rule_3(s):
    if 'III' not in s:
        return s
    else:
        return s.replace('III', 'U')


def rule_4(s):
    if 'UU' in s:
        return s.replace('UU', '')
    else:
        return s


def check_for_mu(l):
    for t in l:
        if t == 'MU':
            print('Found it!')
            assert False


def delete_obsolete(l):
    for element in l:
        if element.count('UU') == 0 and element.count('III') == 0 and element.endswith('U') and len(element) > 2:
            l.remove(element)
    return l


def solve():
    all_theorems = ['MUI']
    while True:
        for theorem in all_theorems:
            tmp = rule_1(theorem)
            if all_theorems.count(tmp) <= 0:
                all_theorems.append(tmp)
            tmp = rule_2(theorem)
            if all_theorems.count(tmp) <= 0:
                all_theorems.append(tmp)
            tmp = rule_3(theorem)
            if all_theorems.count(tmp) <= 0:
                all_theorems.append(tmp)
            tmp = rule_4(theorem)
            if all_theorems.count(tmp) <= 0:
                all_theorems.append(tmp)
            all_theorems.remove(all_theorems[0])
            delete_obsolete(all_theorems)
            check_for_mu(all_theorems)


solve()