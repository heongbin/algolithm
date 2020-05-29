def split(p):
    check = 0
    cnt = 0
    for i in p:
        if i == '(':
            check += 1
            cnt += 1
            if check == 0:
                break
        else:
            check -= 1
            cnt += 1
            if check == 0:
                break
    return p[:cnt], p[cnt:]


def is_correct(p):
    cnt = 0
    for i in p:
        if cnt < 0:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    return True


def make_correct(u, v):
    ret = '(%s)' % recursion(v)
    for i in u[1:-1]:
        if i == '(':
            ret += ')'
        else:
            ret += '('

    return ret


def recursion(p):
    if not p:
        return p
    u, v = split(p)
    if is_correct(u):
        return u + recursion(v)
    return make_correct(u, v)


def solution(p):
    return recursion(p)