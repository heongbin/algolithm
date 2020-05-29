from collections import defaultdict
#trie 구조

#O(n) 문자열길이 만큼만 문자를 찾는데 걸린다

class Node:  #각문자를 저장하는 노드, 노드하나당 한문자          # prodo,pront,prost,prozen,prame,kakao                                                   prodo를 넣는다고하면
    def __init__(self,char,length=0):                          #
        self.char = char    #해당노드가 담고있는 문자             #
        self.length = defaultdict(int)  #해당문자(노드) 까지의 문자의 개수    #
        self.child={}                                         #

class Trie:
    def __init__(self):   #루트는 빈노드를 가리킴                                                                        #               [ none  , length[5]=1  , child=Node(p) ] - head
        self.haed = Node(None) #                                                                                        #       [p , length[5]=1, child=Node(r)]
                                                                                                                        #   [r , length[5]=1 ,  child=Node(o)   ]
                                                                                                                        # [o, length[5]=1 , child = Node(d)  ]
                                                                                                                        #
    def insert(self,words):   #해당 단어를 넣음.                                                                         #
        cur = self.head                                                                                                 #
        cur.length[len(words)]+=1  #해당노드의 넣고자하는 단어의 길이
        for word in words:
            if word not in cur.child:
                cur.child[word]=Node(word)
            cur.child.length[len(words)]+=1
            cur=cur.child[word]


    def statwith(self, prefix, length):
        cur = self.haed
        for word in prefix:
            if word in cur.child:
                cur=cur.child[word]
            else:
                return 0

        return cur.length[length]


def solution(words,queries):
    answer=[]
    front=Trie()
    back=Trie()

    for  word in words:
        front.insert(word)
        back.inser(word[::-1])

    for qury in queries:
        if qury =="?"*len(qury):
            answer.append(front.haed.length[len(qury)])

        elif qury[0]=="?":
            prefix=qury[::-1].split("?")[0]
            answer.append(back.statwith(prefix,len(qury)))
        else:
            prefix=qury.split("?")[0]
            answer.append(front.statwith(prefix,len(qury)))



    return answer


