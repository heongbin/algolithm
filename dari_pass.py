import copy
class Node:
    def __init__(self,idx,stor):
        self.idx = idx #인덱스
        self.storage = stor #얼마나 여유가 있는지
        self.next = None #해당 돌이 가리키는 다음돌.

def dfs(idx):
    global flag
    global answer
    #for i in range(len(stone_info)):
        #print("[idx는 {},해당 storage: {}, next는 {}]".format(stone_info[i].idx,stone_info[i].storage,stone_info[i].next))
    #print("end")
    cur_stone = stone_info[idx] #현재 확인하는
    if idx==0:
        cur_stone.next=dfs(cur_stone.next)
        if cur_stone.next - cur_stone.idx >k:
            flag=1
            return
        return

    if cur_stone.idx == len(stones)+1: #마지막 돌이면
        answer+=1
        #print("마지막돌옮 {}".format(answer))
        return cur_stone.idx

    if cur_stone.storage!=0: #그돌이 밟을 수 있다면.
        cur_stone.storage-=1 #밟고
        if cur_stone.storage == 0: #진행하고 그게 그돌이 다밟은거면.
            cur_stone.next = dfs(cur_stone.next)
            if cur_stone.next - cur_stone.idx > k: #그리고 그 돌과 그가리키는 다음돌차이가 k이상이면
                flag=1
                return cur_stone.next

            return cur_stone.next

        cur_stone.next=dfs(cur_stone.next) #그 돌이 가리키는 다음돌로
        if cur_stone.next - cur_stone.idx > k: #만약 진행해서
            flag=1
            return cur_stone.idx

        return cur_stone.idx

    else:#해당 돌을 밟을 수x
        return dfs(idx+1)










stones=[200000000,200000000,200000000]
k=3
stone_info = []
answer=0
flag=0
copy_stones = copy.deepcopy(stones)
copy_stones.append(Node(len(stones),0))

for idx, stone in enumerate(copy_stones):
    stone_info.append(Node(idx+1,stone))

for i in range(len(stone_info)):
    stone_info[i].next = stone_info[i].idx+1

stone_info.insert(0,Node(0,0))
stone_info[0].next = 1


while True:
    if flag==1:
        #for i in range(len(stone_info)):
            #print("[idx는 {},해당 storage: {}, next는 {}]".format(stone_info[i].idx, stone_info[i].storage,stone_info[i].next))
        break
    dfs(0)



print(answer)


