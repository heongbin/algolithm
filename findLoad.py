class Node:
    def __init__(self,x,y,idx):
        self.x=x
        self.y=y
        self.idx=idx
        self.left=self.right=None

def SearchandInsert(root,insertNode):
    if root.x>insertNode.x:
        if root.left!=None:
            SearchandInsert(root.left, insertNode)
        else:
            root.left=insertNode

    else:
        if root.right!=None:
            SearchandInsert(root.right,insertNode)
        else:
            root.right=insertNode

def preSearch(root,prelist): #전위순회
    prelist.append(root.idx)
    if root.left!=None:
        preSearch(root.left,prelist)
    if root.right!=None:
        preSearch(root.right,prelist)



def postSearch(root,postlist): #후위순회
    if root.left!=None:
        postSearch(root.left,postlist)
    if root.right!=None:
        postSearch(root.right,postlist)

    postlist.append(root.idx)

def solution(nodeinfo):
    answer=[]
    nodelist=[]

    for idx,node in enumerate(nodeinfo):
        nodelist.append(Node(node[0],node[1],idx+1))
    copylist=sorted(nodelist,key=lambda x: (x.y, x.x),reverse=True)
    seeinglist=[]
    for copy in copylist:
        seeinglist.append([copy.x,copy.y,copy.idx])
    root=copylist[0]
    for i in range(1,len(copylist)):
        SearchandInsert(root,copylist[i])
    prelst=[]
    postlst=[]

    preSearch(root,prelst)
    postSearch(root,postlst)
    answer.append(prelst)
    answer.append(postlst)
    #print(answer)

nodeinfo=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfo)


