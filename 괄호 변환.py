def seperate_word(w):
    sums=0
    for i in range(len(w)):
        if w[i]=="(":
            sums+=1

        else:
            sums-=1

        if sums==0:
            return i+1

def check_correct(u):
    sums=0
    for i in range(len(u)):
        if u[i]=="(":
            sums+=1
        else:
            sums-=1
        if sums < 0:
            return False

    return True








def entire_method(w):
    if w == "":
        return ""

    else:
        border=seperate_word(w)
        u= w[:border]
        v= w[border:]


        print(u)
        print(v)
        print("!!!!")
        if check_correct(u)==True:
            return u + entire_method(v)

        else:
            tmp="("
            tmp+=entire_method(v)+")"
            u=u[1:len(u)-1]
            ret=""
            for i in u:
                if i=="(":
                    ret+=")"
                else:
                    ret+="("
            tmp+=ret

            return tmp






def solution(p):
    return entire_method(p)

p="()))((()"
print(solution(p))