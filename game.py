__author__ = 'archlevi'


def rule_1(s):
    if s[-1] == 'I':
        return s+'U'
    else:
        print('Not appliable')
    return s


def rule_2(s):
    if s[0] == 'M':
        return s + s[1:len(s)]
    else:
        print('Not appliable')
    return s


def rule_3(s):
    if 'III' not in s:
        print('Not appliable')
        return s
    print\
        (
            'String:  ' + s +
            '\nIndexes: ', end=''
        )
    for i in range(1, len(s)+1):
        if i % 5 == 0:
            print(5, end='')
        else:
            print(' ', end='')
    print()
    rep = []
    for c in s:
        rep.append(c)
    while True:
        i = input('Replace "III" from index x onward: x=')
        if i.isdigit():
            i = int(i) - 1
        else:
            continue
        if s[i:i+3] == 'III':
            break
        else:
            print('Invalid Input')
    rep[i:i+3] = 'U'
    s = ''
    for i in rep:
        s += i
    return s


def rule_4(s):
    if 'UU' in s:
        return s.replace('UU', '')
    else:
        print('Not appliable')
    return s


def the_mu_puzzle(s):
    print('Try to produce MU.')
    memory = [s]
    while True:
        print\
        (
            'rule1: If last letter "I" add on "U" \n'
            'rule2: If you have Mx you can add Mxx \n'
            'rule3:"III" can be replaced with "U" \n'
            'rule4: "UU" can be dropped \n'
        )
        print('Current string: ' + s)
        c = input('Which rule would you like to use? (r to reset, u to undo)\n')
        if c == 'r':
            s = 'MI'
            continue
        if c == 'u':
            if len(memory) == 1:
                print('Nothing to undo!')
                continue
            s = memory[-2]
            memory.pop()
            continue
        if not c.isdigit():
            print('Invalid Input!')
            continue
        if int(c) == 1:
            s = rule_1(s)
        elif int(c) == 2:
            s = rule_2(s)
        elif int(c) == 3:
            s = rule_3(s)
        elif int(c) == 4:
            s = rule_4(s)
        memory.append(s)

the_mu_puzzle('MI')