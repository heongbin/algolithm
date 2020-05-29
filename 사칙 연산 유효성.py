class Node:
    def __init__(self,idx):
        self.idx=idx
        self.value=""
        self.left=None
        self.right=None



def post_order(index):
    if nodelist[index].left==None and nodelist[index].right==None: #숫자임.
        q.append(nodelist[index].value)



    else:
        post_order(nodelist[index].left)
        post_order(nodelist[index].right)
        q.append(nodelist[index].value)







def calculate():
    while q:
        curr=q.pop(0)
        if curr in op:
            if curr=="+":
                a=number.pop()
                b=number.pop()
                tmp=b+a
                number.append(tmp)

            elif curr=="-":
                a = number.pop()
                b = number.pop()
                tmp = b-a
                number.append(tmp)


            elif curr=="/":
                a = number.pop()
                b = number.pop()
                tmp = b//a
                number.append(tmp)

            else:
                a = number.pop()
                b = number.pop()
                tmp = b*a
                number.append(tmp)

        else: #숫자라면
            number.append(int(curr))


    return number[0]







for test_case in range(1,11):
    number=[]
    q=[]
    op=["+","-","*","/"]

    n=int(input())
    nodelist=[Node(i) for i in range(n+1)]

    for i in range(1,n+1):
        tmp=list(input().split())
        if tmp[1]=="+" or tmp[1]=="-" or tmp[1]=="*" or tmp[1]=="/":
            nodelist[i].value=tmp[1]
            nodelist[i].left=int(tmp[2])
            nodelist[i].right=int(tmp[3])

        else:
            nodelist[i].value=tmp[1]









    post_order(1)
    print("#{} {}".format(test_case,calculate()))










