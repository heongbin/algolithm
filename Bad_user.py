
def dfs(tmp,idx,tmplist):
    global answerlist
    if idx==len(tmplist): #일단 후보군 다고른후
        listtoset=set(tmp)
        if len(listtoset)==len(tmplist): #고른 후보명단에 duplicate가 있으면
            if list(listtoset) not in answerlist:
                answerlist.append(list(listtoset))
                return
        return

    for j in range(len(tmplist[idx])):
        tmp.append(tmplist[idx][j]) #각 banid가 갖고있는 후보키들.
        dfs(tmp,idx+1,tmplist)
        tmp.pop()



user_id=["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id=["fr*d*", "*rodo", "******", "******"]

tmplist=[]
final_list=[]

for i in range(len(banned_id)): #pr*d*
    tmp_ban_list=[]
    isfullstar=True #해당 단어가 전체가 *인지 확인
    for j in range(len(banned_id[i])):
        if banned_id[i][j]!="*":
            isfullstar=False
            break

    for j in range(len(user_id)): #prodo
        if isfullstar==True and len(banned_id[i])==len(user_id[j]): #전체가 *면 길이만 같으면 후보단어가됨.
            tmp_ban_list.append(user_id[j]) #후보에 넣기


        elif len(banned_id[i])==len(user_id[j]) and isfullstar==False: #길이가 같고 전체가 *가 x면 비교
            flag=0
            for k in range(len(banned_id[i])):
                if banned_id[i][k]!="*" and banned_id[i][k]!=user_id[j][k]: #pr*d*o에서 *가 x면서, 같으면 비교
                    flag=1 #다른 문자가 있으면
                    break
            if flag==0: #*가 아닌 문자와 비교하여 다 같다면.
                tmp_ban_list.append(user_id[j]) #후보에 넣음

    tmplist.append(tmp_ban_list)





#tmplist 후보군이 생성되면.
#prodo , pradi , crodo , abc123, prodoc
#pr*d*, *rodo , ****** , ******




#pr*d*= prodo, pradi
#*rodo= prodo, crodo
#******= abc123 ,prodoc
#******= abc123, prodoc



check_list=[]
answerlist=[]
dfs(check_list,0,tmplist)
return len(answerlsit)









